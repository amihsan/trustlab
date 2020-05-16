from trustlab.lab.connectors.basic_connector import BasicConnector
from django.db import transaction
from django.db.models import F, Sum
from trustlab.models import Supervisor


class ChannelsConnector(BasicConnector):
    def sums_agent_numbers(self):
        return Supervisor.objects.aggregate(sum_max_agents=Sum('max_agents'), sum_agents_in_use=Sum('agents_in_use'))

    def list_supervisors_with_free_agents(self):
        return list(set(Supervisor.objects.filter(agents_in_use__lt=F('max_agents'))))

    @transaction.atomic
    def reserve_agents(self, distribution):
        for channel_name in distribution.keys():
            supervisor = Supervisor.objects.get(channel_name=channel_name)
            supervisor.agents_in_use += len(distribution[channel_name])
            supervisor.save()
            # init agents at supervisors

