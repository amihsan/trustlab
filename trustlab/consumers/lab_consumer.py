from channels.generic.websocket import WebsocketConsumer
import json
from trustlab.models import *
from trustlab.serializers.scenario_serializer import ScenarioSerializer
from trustlab.lab.director import Director


class LabConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        serializer = ScenarioSerializer(data=text_data_json)
        if serializer.is_valid():
            try:
                scenario_factory = ScenarioFactory()
                scenario = serializer.create(serializer.data)
            except ValueError as value_error:
                self.send(text_data=json.dumps({
                    'message': str(value_error),
                    'status': 400
                }))
                return
            if scenario not in scenario_factory.scenarios:
                scenario_factory.scenarios.append(scenario)
            # self.send(text_data=json.dumps({
            #     'message': "Starting Lab Runtime according to Scenario",
            #     'status': 200
            # }))
            director = Director()
            director_log_path, trust_log_path = director.run_scenario(scenario)
            with open(director_log_path.absolute(), 'r+') as director_log_file,\
                    open(trust_log_path.absolute(), 'r+') as trust_log_file:
                director_log = director_log_file.readlines()
                trust_log = trust_log_file.readlines()
                self.send(text_data=json.dumps({
                    'director_log': "".join(director_log),
                    'trust_log': "".join(trust_log),
                    'message': "Execution finished",
                    'status': 200
                }))
        else:
            self.send(text_data=json.dumps({
                'message': serializer.errors,
                'status': 400
            }))



