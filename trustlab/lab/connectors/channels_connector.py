import json
from asgiref.sync import async_to_sync, sync_to_async
from trustlab.lab.connectors.basic_connector import BasicConnector
from django.db import transaction
from django.db.models import F, Sum
from trustlab.models import Supervisor
from channels.layers import get_channel_layer


class ChannelsConnector(BasicConnector):
    @sync_to_async
    def sums_agent_numbers(self):
        return Supervisor.objects.aggregate(sum_max_agents=Sum('max_agents'), sum_agents_in_use=Sum('agents_in_use'))

    @sync_to_async
    def list_supervisors_with_free_agents(self):
        return list(set(Supervisor.objects.filter(agents_in_use__lt=F('max_agents'))))

    async def send_message_to_supervisor(self, channel_name, message):
        channel_layer = get_channel_layer()
        await channel_layer.send(channel_name, message)

    async def receive_with_scenario_run_id(self, scenario_run_id):
        channel_layer = get_channel_layer()
        response = await channel_layer.receive(scenario_run_id)
        return response

    @sync_to_async
    @transaction.atomic
    def reserve_agents_in_db(self, distribution):
        for channel_name in distribution.keys():
            supervisor = Supervisor.objects.get(channel_name=channel_name)
            supervisor.agents_in_use += len(distribution[channel_name])
            supervisor.save()

    async def reserve_agents(self, distribution, scenario_run_id, scenario_data):
        discovery = {}
        for channel_name in distribution.keys():
            # init agents at supervisors
            registration_message = {
                "type": "scenario.registration",
                "scenario": scenario_data,
                "scenario_run_id": scenario_run_id,
                "agents_at_supervisor": distribution[channel_name]
            }
            await self.send_message_to_supervisor(channel_name, registration_message)
            agent_discovery = await self.receive_with_scenario_run_id(scenario_run_id)
            discovery = {**discovery, **agent_discovery["discovery"]}
        self.reserve_agents_in_db(distribution)
        # after registration and discovery knowledge share discovery with all involved supervisors
        for channel_name in distribution.keys():
            discovery_message = {
                "type": "scenario.discovery",
                "scenario_run_id": scenario_run_id,
                "discovery": discovery
            }
            await self.send_message_to_supervisor(channel_name, discovery_message)
        return discovery
