from django.views import generic
from trustlab.models import *
from trustlab.serializers.scenario_serializer import ScenarioSerializer
from rest_framework.renderers import JSONRenderer

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # add saved Scenarios
        try:
            # ScenarioFactory throws AssertionError if no predefined scenarios could be loaded
            scenario_factory = ScenarioFactory()
            context["scenarios"] = scenario_factory.scenarios
            # for manipulation of scenarios via JS, send them also as JSON
            scenario_serializer = ScenarioSerializer(scenario_factory.scenarios, many=True)
            context["scenarios_JSON"] = JSONRenderer().render(scenario_serializer.data).decode('utf-8')
        except AssertionError as assert_error:
            # TODO bring assert_error to scenario_error_msg on index.html
            pass
        return context


