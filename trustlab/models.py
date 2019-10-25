from django.db import models
from os import listdir
from os.path import isfile, join, dirname, abspath
import importlib


class Scenario:
    @staticmethod
    def consistency_checker(name, agents, schedule):
        if isinstance(name, str) or len(name) == 0:
            raise ValueError("Scenario names must be a string and not empty.")
        if not isinstance(agents, list) or len(agents) <= 1:
            raise ValueError("Scenario agents must be a list and describe at least 2 agents.")
        if not isinstance(schedule, dict) or not bool(schedule):
            raise ValueError("Scenario schedule must be a dict and not empty.")
        return True

    def __init__(self, name, agents, schedule, description=""):
        self.consistency_checker(name, agents, schedule)
        self.name = name
        self.agents = agents
        self.schedule = schedule
        self.description = description

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name


class ScenarioFactory:

    @staticmethod
    def load_scenarios(self):
        scenarios = []
        project_path = abspath(dirname(__name__))
        scenario_path = project_path + '/trustlab/lab/scenarios'
        file_names = [file for file in listdir(scenario_path) if isfile(join(scenario_path, file)) and
                      file.endswith("_scenario.py")]
        for file in file_names:
            import_path = "trustlab.lab.scenarios" + '.' + file.split(".")[0]

            implementation_spec = importlib.util.find_spec(import_path)
            found = implementation_spec is not None
            print(found)
            # if found:
            #     implementation = importlib.import_module(import_path)
            #     if hasattr(implementation, INIT_FUNCTION_NAME):
            #         plugin_init_function = getattr(implementation, INIT_FUNCTION_NAME)
            #         plugin_init_function()
            #     if not hasattr(implementation, function_name):
            #         return 'Implementation required for %s of device %s' % (function_name, device)
            #     method = getattr(implementation, function_name)
        return scenarios

    def __init__(self):
        self.scenarios = self.load_scenarios
