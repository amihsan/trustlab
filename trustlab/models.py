from django.db import models
import importlib
import inspect
from os import listdir
from os.path import isfile, join, dirname, abspath


class Scenario:
    @staticmethod
    def check_consistency(name, agents, schedule, description):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Scenario names must be string and not empty.")
        if not isinstance(agents, list) or len(agents) <= 1:
            raise ValueError("Scenario agents must be list and describe at least 2 agents.")
        if not isinstance(schedule, dict) or not bool(schedule):
            raise ValueError("Scenario schedule must be dict and not empty.")
        if not isinstance(description, str):
            raise ValueError("Description must be string.")
        return True

    def __init__(self, name, agents, schedule, description="No one described this scenario so far."):
        self.check_consistency(name, agents, schedule, description)
        self.name = name
        self.agents = agents
        self.schedule = schedule
        self.description = description

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name


class ScenarioFactory:
    # load all scenarios in /trustlab/lab/scenarios with dynamic read of parameters from Scenario.__init__
    @staticmethod
    def load_scenarios():
        scenarios = []
        project_path = abspath(dirname(__name__))
        # path of scenario_config files
        scenario_path = project_path + '/trustlab/lab/scenarios'
        scenario_file_names = [file for file in listdir(scenario_path)
                               if isfile(join(scenario_path, file)) and file.endswith("_scenario.py")]
        for file_name in scenario_file_names:
            # python package path
            import_package = "trustlab.lab.scenarios" + '.' + file_name.split(".")[0]
            # ensure package is accessible
            implementation_spec = importlib.util.find_spec(import_package)
            if implementation_spec is not None:
                # import scenario config to variable
                scenario_config = importlib.import_module(import_package)
                # get all parameters of scenario init
                scenario_args = inspect.getfullargspec(Scenario.__init__)
                # get only args without default value and not self parameter and capitalize them
                mandatory_args = [a.upper() for a in scenario_args.args[1:-len(scenario_args.defaults)]]
                # all attr
                all_args = [a.upper() for a in scenario_args.args[1:]]
                # check if all mandatory attrs are in scenario config
                if all(hasattr(scenario_config, attr) for attr in mandatory_args):
                    scenario_attrs = []
                    for attr in all_args:
                        # check if attr is in config as some are optional with default value
                        if hasattr(scenario_config, attr):
                            scenario_attrs.append(getattr(scenario_config, attr))
                    try:
                        # add all attrs which are in config to scenario object
                        scenario = Scenario(*scenario_attrs)
                    # catch all ValueErrors, print and continue
                    except ValueError as value_error:
                        print(str(value_error))
                        continue
                    scenarios.append(scenario)
        return scenarios

    def __init__(self):
        self.scenarios = ScenarioFactory.load_scenarios()
        if not self.scenarios:
            raise AssertionError("ScenarioFactory object found no scenarios at init.")


