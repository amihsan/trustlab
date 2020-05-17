from channels.generic.websocket import JsonWebsocketConsumer
from trustlab.models import Supervisor
from asgiref.sync import async_to_sync


class SupervisorsConsumer(JsonWebsocketConsumer):
    def connect(self):
        Supervisor.objects.create(channel_name=self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        Supervisor.objects.filter(channel_name=self.channel_name).delete()

    def scenario_registration(self, event):
        self.send_json({
            "type": "scenario_registration",
            "scenario": event["scenario"],
            "scenario_run_id": event["scenario_run_id"],
            "agents_at_supervisor": event["agents_at_supervisor"]
        })

    def receive_json(self, content, **kwargs):
        if content["type"] and content["type"] == "max_agents":
            supervisor = Supervisor.objects.get(channel_name=self.channel_name)
            supervisor.max_agents = content["max_agents"]
            supervisor.save()
            answer = {"type": "max_agents", "status": 200}
            self.send_json(answer)
        elif content["type"] and content["type"] == "scenario_discovery":
            async_to_sync(self.channel_layer.send)(self.channel_name, content["discovery"])
        else:
            self.send_json(content)


