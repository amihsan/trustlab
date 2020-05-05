from channels.generic.websocket import JsonWebsocketConsumer
from trustlab.models import Supervisors


class SupervisorsConsumer(JsonWebsocketConsumer):
    def connect(self):
        Supervisors.objects.create(channel_name=self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        Supervisors.objects.filter(channel_name=self.channel_name).delete()

    def receive_json(self, content, close=False):
        if content["type"] and content["type"] == "max_agents":
            supervisor = Supervisors.objects.get(channel_name=self.channel_name)
            supervisor.max_agents = content["max_agents"]
            supervisor.save()
            answer = {"type": "max_agents", "status": 200}
            self.send_json(answer)
        else:
            self.send_json(content)


