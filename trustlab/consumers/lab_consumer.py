from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
import trustlab.lab.config as config
from trustlab.models import *
from trustlab.serializers.scenario_serializer import ScenarioSerializer
from trustlab.lab.director import Director


class LabConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content, **kwargs):
        serializer = ScenarioSerializer(data=content)
        if serializer.is_valid():
            try:
                scenario_factory = ScenarioFactory()
                scenario = serializer.create(serializer.data)
            except ValueError as value_error:
                await self.send_json({
                    'message': str(value_error),
                    'status': 400
                })
                return
            if scenario not in scenario_factory.scenarios:
                scenario_factory.scenarios.append(scenario)
            # await self.send_json(text_data=json.dumps({
            #     'message': "Starting Lab Runtime according to Scenario",
            #     'status': 200
            # }))
            director = Director(scenario)
            try:
                async with config.PREPARE_SCENARIO_SEMAPHORE:
                    await director.prepare_scenario()
                await director.run_scenario()
                await self.send_json({
                        'director_log': "Currently Empty due to testing",
                        'trust_log': "Currently Empty due to testing",
                        'message': "Execution finished",
                        'status': 200
                    })
                # director_log_path, trust_log_path = director.run_scenario()
                # with open(director_log_path.absolute(), 'r+') as director_log_file, \
                #         open(trust_log_path.absolute(), 'r+') as trust_log_file:
                #     director_log = director_log_file.readlines()
                #     trust_log = trust_log_file.readlines()
                #     await self.send_json({
                #         'director_log': "".join(director_log),
                #         'trust_log': "".join(trust_log),
                #         'message': "Execution finished",
                #         'status': 200
                #     })
            except Exception as exception:
                await self.send_json({
                    'message': str(exception),
                    'status': 400
                })
        else:
            await self.send(text_data=json.dumps({
                'message': serializer.errors,
                'status': 400
            }))



