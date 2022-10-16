from trustlab.consumers.chunk_consumer import ChunkAsyncJsonWebsocketConsumer
from trustlab.models import Supervisor
from trustlab.serializers.mogno_db_connector import MongoDbConnector
from trustlab.lab.config import CONNECTIONSTRING
import time


class SupervisorsConsumer(ChunkAsyncJsonWebsocketConsumer):
    async def connect(self):
        Supervisor.objects.create(channel_name=self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        Supervisor.objects.filter(channel_name__exact=self.channel_name).delete()

    async def scenario_registration(self, event):
        print(event["scenario_name"])
        self.get_database().set_all_observations_not_done(event["scenario_name"], event["scenario_run_id"])
        self.get_database().set_all_agents_nothing_to_do(event["scenario_name"], event["scenario_run_id"])
        await self.send_websocket_message({
            "type": "scenario_registration",
            "scenario_run_id": event["scenario_run_id"],
            "scenario_name": event["scenario_name"],
            "agents_at_supervisor": event["agents_at_supervisor"]
        })

    async def scenario_discovery(self, event):
        await self.send_websocket_message({
            "type": "scenario_discovery",
            "scenario_run_id": event["scenario_run_id"],
            "discovery": event["discovery"]
        })

    async def scenario_start(self, event):
        #await self.send_websocket_message({
        #    "type": "scenario_start",
        #    "scenario_run_id": event["scenario_run_id"],
        #    "scenario_status": event["scenario_status"],
        #    "scenario_name": event["scenario_name"]
        #})
        await self.send_new_agent_data(event["scenario_run_id"], event["scenario_name"])

    async def observation_done(self, event):
        await self.send_websocket_message({
            "type": "observation_done",
            "scenario_run_id": event["scenario_run_id"],
            "observations_done": event["observations_done"]
        })

    async def scenario_end(self, event):
        await self.send_websocket_message({
            "type": "scenario_end",
            "scenario_run_id": event["scenario_run_id"],
            "scenario_status": event["scenario_status"]
        })

    async def send_new_agent_data(self, scenario_id, scenario_name):
        agents = self.get_database().get_agents_nothing_to_do(scenario_name, scenario_id)

        if agents is not None and len(agents) > 0:
            observations = self.get_database().get_observations(scenario_name, scenario_id, agents)

            if observations is not None:
                for observation in observations:
                    del(observation["_id"])
                    del(observation["Type"])

                    answer = {
                        "type": "new_observation",
                        "scenario_run_id": scenario_id,
                        "scenario_name": scenario_name,
                        "data": observation}
                    await self.send_websocket_message(answer)
                    self.get_database().set_agent_has_something_todo(scenario_name, scenario_id, observation["sender"])

    async def receive_json(self, content, **kwargs):
        handled, new_content = await super().receive_chunk_traffic(content)
        content = new_content if new_content else content
        if not handled:
            if content["type"] and content["type"] == "max_agents":
                supervisor = Supervisor.objects.get(channel_name=self.channel_name)
                supervisor.max_agents = content["max_agents"]
                supervisor.ip_address = content["ip_address"]
                if 'hostname' in content:
                    supervisor.hostname = content["hostname"]
                supervisor.save()
                answer = {"type": "max_agents", "status": 200}
                await self.send_json(answer)
            elif content["type"] and content["type"] == "get_scales_per_agent":
                agent = content["agent"]
                data = self.get_database().get_scales(content["scenario_name"], agent)
                del data['_id']
                del data['parent']
                del data['Type']
                answer = {
                    "type": "get_scales_per_agent",
                    "scenario_run_id": content["scenario_run_id"],
                    "scenario_name": content["scenario_name"],
                    "agent": agent,
                    "data": data}
                await self.send_websocket_message(answer)
            elif content["type"] and content["type"] == "get_history_per_agent":
                agent = content["agent"]
                data = self.get_database().get_history(content["scenario_name"], agent)
                for entry in data:
                    del entry['_id']
                    del entry['parent']
                    del entry['Type']
                answer = {
                    "type": "get_history_per_agent",
                    "scenario_run_id": content["scenario_run_id"],
                    "scenario_name": content["scenario_name"],
                    "agent": agent,
                    "data": data}
                await self.send_websocket_message(answer)
            elif content["type"] and content["type"] == "get_all_agents":
                data = self.get_database().get_agents(content["scenario_name"])
                for entry in data:
                    del entry['_id']
                    del entry['Type']
                answer = {
                    "type": "get_all_agents",
                    "scenario_run_id": content["scenario_run_id"],
                    "scenario_name": content["scenario_name"],
                    "data": data}
                await self.send_websocket_message(answer)
            elif content["type"] and content["type"] == "agent_free":
                self.get_database().set_agent_nothing_todo(content["scenario_name"], content["scenario_run_id"], content["agent"])
                await self.send_new_agent_data(content["scenario_run_id"], content["scenario_name"])
            elif content["type"] and content["type"] == "get_metrics_per_agent":
                agent = content["agent"]
                data = self.get_database().get_metrics(content["scenario_name"], agent)
                answer = {
                    "type": "get_metrics_per_agent",
                    "scenario_run_id": content["scenario_run_id"],
                    "scenario_name": content["scenario_name"],
                    "agent": agent,
                    "data": data}
                await self.send_websocket_message(answer)
            elif content["type"] and (content["type"] == "agent_discovery" or content["type"] == "scenario_end"):
                await self.channel_layer.send(content["scenario_run_id"], content)
            elif content["type"] and content["type"] == "observation_done":
                #print(content['observation_id'])
                self.get_database().set_observation_done(content["scenario_name"], content["scenario_run_id"], content["observation_id"])
                content["channel_name"] = self.channel_name
                await self.channel_layer.send(content["scenario_run_id"], content)
                await self.send_new_agent_data(content["scenario_run_id"], content["scenario_name"])
            else:
                print("Could not resolve message and pinged back.")
                await self.send_websocket_message(content)

    def get_database(self):
        if not hasattr(self, "db_connector"):
            self.db_connector = MongoDbConnector(CONNECTIONSTRING)
        return self.db_connector