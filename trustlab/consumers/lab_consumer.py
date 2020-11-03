from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
import trustlab.lab.config as config
import time
from trustlab.models import *
from trustlab.serializers.scenario_serializer import ScenarioSerializer
from trustlab.lab.director import Director


class LabConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content, **kwargs):
        if content['type'] == 'run_scenario':
            serializer = ScenarioSerializer(data=content['scenario'])
            if serializer.is_valid():
                try:
                    scenario_factory = ScenarioFactory()
                    scenario = serializer.create(serializer.data)
                except ValueError as value_error:
                    await self.send_json({
                        'message': str(value_error),
                        'type': 'error'
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
                    await self.send_json({
                        'scenario_run_id': director.scenario_run_id,
                        'type': "scenario_run_id"
                    })
                    trust_log, agent_trust_logs = await director.run_scenario()
                    await director.end_scenario()
                    for agent in agent_trust_logs:
                        agent_trust_logs[agent] = "".join(agent_trust_logs[agent])
                    await self.send_json({
                            'agents_log': json.dumps(agent_trust_logs),
                            'trust_log': "".join(trust_log),
                            'scenario_run_id': director.scenario_run_id,
                            'type': "scenario_results"
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
                        'type': 'error'
                    })
            else:
                await self.send(text_data=json.dumps({
                    'message': serializer.errors,
                    'type': 'error'
                }))
        elif content['type'] == 'get_scenario_results':
            # await self.send(text_data=json.dumps({
            #     'message': 'Requesting saved scenario run results is not yet implemented',
            #     'type': 'error'
            # }))
            result_factory = ResultFactory()
            try:
                scenario_result = result_factory.get_result(content['scenario_run_id'])
                await self.send_json({
                    'agents_log': json.dumps(scenario_result.agent_trust_logs),
                    'trust_log': "".join(scenario_result.trust_log),
                    'scenario_run_id': scenario_result.scenario_run_id,
                    'type': "scenario_results"
                })
            except OSError as exception:
                await self.send_json({
                    'message': str(exception),
                    'type': 'scenario_result_not_found'
                })



