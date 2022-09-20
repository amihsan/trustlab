from pymongo import MongoClient
import pymongo


class MongoDbConnector:

    def __init__(self, connectionString):
        self.client = MongoClient(connectionString)

        try:
            self.client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError:
            raise TimeoutError("Invalid API")

        self.database = self.client["testdatabase"]

    def reset_scenario(self, scenario_name):
        self.database.drop_collection(scenario_name)

    def add_data(self, scenario_name, type, data):
        collection = self.database[scenario_name]
        data["Type"] = type.lower()
        collection.insert_one(data)

    def get_observations(self, scenario_name, scenario_id, agents):
        collection = self.database[scenario_name]

        observations_not_done = collection.find_one({
            "Type": "observations_to_do",
            "scenario_id": scenario_id
        })

        aggregates = collection.aggregate(
            [
                {
                    "$match": {
                        "Type": "observations",
                        "$or": [
                            {
                                "before": {
                                    "$nin": observations_not_done['observations_todo'],
                                }
                            },
                            {
                                "before": []
                            }
                        ],
                        "sender": {
                            "$in": agents
                        },
                        "observation_id": { "$nin": observations_not_done['observations_already_send'] }
                    }
                }, {
                    "$sort": {
                        "_id": 1
                    }
                }, {
                    "$group": {
                        "_id": "$sender",
                        "first": {
                          "$first": "$$ROOT"
                        }
                    }
                }
            ]
        )

        observations = []
        for o in aggregates:
            if (o["_id"] == None):
                continue
            details = self.get_details(scenario_name, o['first']['_id'])
            for d in details:
                del d['_id']
                del d['observation_id']
                del d['Type']

            res = {}
            for sub in details:
                for key in sub:
                    res[key] = sub[key]

            o['first']["details"] = res
            observations.append(o['first'])

            observations_not_done['observations_already_send'].append(o['first']["observation_id"])

        if len(observations) > 0:
            collection.update_one({
                "Type": "observations_to_do",
                "scenario_id": scenario_id
            }, {
                "$set": {'observations_already_send': observations_not_done['observations_already_send']}
            })

        return observations

    def get_details(self, scenario_name, observation_id):
        collection = self.database[scenario_name]

        finds = collection.find(
            {
                "Type": "details",
                "observation_id": observation_id
            })

        return list(finds)

    def set_observation_done(self, scenario_name, scenario_id, observaion_id):
        collection = self.database[scenario_name]

        find = collection.find_one({
            "Type": "observations_to_do",
            "scenario_id": scenario_id
        })

        if observaion_id in find['observations_todo']:
            find['observations_todo'].remove(observaion_id)

            collection.update_one({
                "Type": "observations_to_do",
                "scenario_id": scenario_id
            }, {
                "$set": {'observations_todo': find['observations_todo']}
            })

    def set_all_observations_not_done(self, scenario_name, scenario_id):
        collection = self.database[scenario_name]

        finds = collection.find(
            {
                "Type": "observations",
            },
            {
                "_id": 0,
                "observation_id": 1
            }
        )

        ids = []
        for i in finds:
            ids.append(i['observation_id'])

        collection.delete_one({
            "Type": "observations_to_do",
            "scenario_id": scenario_id
        })

        data = {
            "Type": "observations_to_do",
            "scenario_id": scenario_id,
            "observations_todo": ids,
            "observations_already_send": []
        }

        collection.insert_one(data)

    def set_all_agents_nothing_to_do(self, scenario_name, scenario_id):
        collection = self.database[scenario_name]

        finds = collection.find(
            {
                "Type": "agents",
            },
            {
                "_id": 0,
                "name": 1
            }
        )

        ids = []
        for i in finds:
            ids.append(i['name'])

        collection.delete_one({
            "Type": "agents_nothing_to_do",
            "scenario_id": scenario_id
        })

        data = {
            "Type": "agents_nothing_to_do",
            "scenario_id": scenario_id,
            "agents": ids
        }

        collection.insert_one(data)

    def get_metrics(self, scenario_name, agent):
        agents = self.database[scenario_name]

        finds = agents.find({
            "Type": "metrics_per_agent",
            "parent": agent
        })

        if finds:
            return finds[0]
        return None

    def get_agents_nothing_to_do(self, scenario_name, scenario_id):
        agents = self.database[scenario_name]

        find = agents.find_one({
            "Type": "agents_nothing_to_do",
            "scenario_id": scenario_id
        })

        return list(find['agents'])

    def set_agent_has_something_todo(self, scenario_name, scenario_id, agent):
        collection = self.database[scenario_name]

        find = collection.find_one({
            "Type": "agents_nothing_to_do",
            "scenario_id": scenario_id
        })

        if agent in find['agents']:
            find['agents'].remove(agent)

            collection.update_one({
                "Type": "agents_nothing_to_do",
                "scenario_id": scenario_id
            }, {
                "$set": {'agents': find['agents']}
            })

    def set_agent_nothing_todo(self, scenario_name, scenario_id, agent):
        collection = self.database[scenario_name]

        find = collection.find_one({
            "Type": "agents_nothing_to_do",
            "scenario_id": scenario_id
        })

        if agent not in find['agents']:
            find['agents'].append(agent)

            collection.update_one({
                "Type": "agents_nothing_to_do",
                "scenario_id": scenario_id
            }, {
                "$set": {'agents': find['agents']}
            })

    def get_scales(self, scenario_name, agent):
        agents = self.database[scenario_name]

        finds = agents.find({
            "Type": "scales_per_agent",
            "parent": agent
        })

        if finds:
            return finds[0]
        return None

    def get_history(self, scenario_name, agent):
        agents = self.database[scenario_name]

        finds = agents.find({
            "Type": "history",
            "parent": agent
        })

        if finds:
            return list(finds)
        return None

    def get_agents(self, scenario_name):
        agents = self.database[scenario_name]

        finds = agents.find({
            "Type": "agents"
        })

        if finds:
            return list(finds)
        return None

    def get_agents_list(self, scenario_name):
        all_agents = []
        for agentdefinition in self.get_agents(scenario_name):
            all_agents.append(agentdefinition['name'])

        return all_agents

    def get_observations_count(self, scenario_name):
        collection = self.database[scenario_name]

        count = collection.count_documents(
            {
                "Type": "observations",
            }
        )

        return count


if __name__ == "__main__":

    CONNECTIONSTRING = "mongodb://localhost:27017"

    connector = MongoDbConnector(CONNECTIONSTRING)
    # connector.add_data("agents", {"name": "A"})
    # connector.add_data("agents", {"name": "B"})
    # connector.add_data("agents", {"name": "D"})

    # connector.add_data("observation", {"observadion_id": 0, "message": "Das ist ein Test", "sender": "A", "receiver": "B", "before": []})
    # connector.add_data("observation", {"observadion_id": 1, "message": "Das ist ein Test", "sender": "A", "receiver": "B", "before": [0]})

    print(connector.set_all_observations_not_done("aTLAS", "test"))
    print(connector.set_all_agents_nothing_to_do("aTLAS", "test"))
    # print(connector.set_observation_done("test", 1))
    # print(connector.set_observation_done("test", 2))

    agents = connector.get_agents_nothing_to_do("aTLAS", "test")

    for o in agents:
        print(o)

    connector.set_agent_has_something_todo("aTLAS", "test", "A")
    connector.set_agent_has_something_todo("aTLAS", "test", "B")
    connector.set_agent_nothing_todo("aTLAS", "test", "B")
    connector.set_agent_nothing_todo("aTLAS", "test", "C")

    agents = connector.get_agents_nothing_to_do("aTLAS", "test")

    for o in agents:
        print(o)

    observations = connector.get_observations("aTLAS", "test", ['A'])

    for o in observations:
        print(o)
