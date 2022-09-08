from pymongo import MongoClient
import pymongo

class MongoDbConnector:

    def __init__(self, connectionString):
        self.client = MongoClient(connectionString)

        try:
            self.client.server_info()
        except pymongo.errors.ServerSelectionTimeoutError:
            raise TimeoutError("Invalid API")

        print(pymongo.version)

        self.database = self.client["testdatabase"]

    def add_data(self, type, data):
        collection = self.database["aTLAS"]
        data["Type"] = type.lower()
        collection.insert_one(data)

    def get_data(self):
        agents = self.database["aTLAS"]

        finds = agents.find({
            "Type": "observations",
            "before": {
                "$nin": [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
            }
        })

        for x in finds:
            print(x)


if __name__ == "__main__":
    CONNECTIONSTRING = "mongodb://ma-sosmos-mongodb:ebQCT5S2XaGsVXX5VTQg7Ih2NEXBRguApReu6ASXOVvfj5HX7Vmb7qoHiC84GSqth3evm7Za8yYbXMbP1Z7d1w==@ma-sosmos-mongodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@ma-sosmos-mongodb@"

    connector = MongoDbConnector(CONNECTIONSTRING)
    #connector.add_data("agents", {"name": "A"})
    #connector.add_data("agents", {"name": "B"})
    #connector.add_data("agents", {"name": "D"})

    #connector.add_data("observation", {"observadion_id": 0, "message": "Das ist ein Test", "sender": "A", "receiver": "B", "before": []})
    #connector.add_data("observation", {"observadion_id": 1, "message": "Das ist ein Test", "sender": "A", "receiver": "B", "before": [0]})

    connector.get_data()
