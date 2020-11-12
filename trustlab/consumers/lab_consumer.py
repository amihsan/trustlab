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
            result_factory = ResultFactory()
            currentID = content['scenario_run_id']
            if config.validate_scenario_run_id(currentID):
                try:
                    scenario_result = result_factory.get_result(currentID)
                    await self.send_json({
                        'agents_log': json.dumps(scenario_result.agent_trust_logs),
                        'trust_log': "".join(scenario_result.trust_log),
                        'scenario_run_id': scenario_result.scenario_run_id,
                        'type': "scenario_results"
                    })
                except OSError as exception:
                    await self.send_json({
                        'message': "Scenario Result not found",
                        'exception': str(exception),
                        'type': 'scenario_result_error'
                    })
            else:
                await self.send_json({
                    'message': "Scenario Run ID is not valid",
                    'type': 'scenario_result_error'
                })




