from trustlab_host.models import Scenario
from django.db import models
import re
import importlib
import importlib.util
import inspect
from os import listdir
from os.path import isfile, join, dirname, abspath
import pprint
from trustlab.lab.config import SCENARIO_PATH, SCENARIO_PACKAGE, RESULT_PATH


class Supervisor(models.Model):
    channel_name = models.CharField(max_length=120)
    max_agents = models.IntegerField(default=0)
    agents_in_use = models.IntegerField(default=0)


class ObjectFactory:
    def save_object(self, object_args):
        # all attr
        all_args = [a.upper() for a in object_args.args[1:]]

    def __init__(self):
        self.project_path = abspath(dirname(__name__))


class ScenarioFactory:
    # load all scenarios in /trustlab/lab/scenarios with dynamic read of parameters from Scenario.__init__
    def load_scenarios(self):
        scenarios = []
        scenario_file_names = [file for file in listdir(self.scenario_path)
                               if isfile(join(self.scenario_path, file)) and file.endswith("_scenario.py")]
        for file_name in scenario_file_names:
            # python package path
            import_package = SCENARIO_PACKAGE + '.' + file_name.split(".")[0]
            # ensure package is accessible
            implementation_spec = importlib.util.find_spec(import_package)
            if implementation_spec is not None:
                # check if module was imported during runtime to decide if reload is required
                scenario_spec = importlib.util.find_spec(import_package)
                # import scenario config to variable
                scenario_config_module = importlib.import_module(import_package)
                # only reload module after importing if spec was found before
                if scenario_spec is not None:
                    scenario_config_module = importlib.reload(scenario_config_module)
                # get all parameters of scenario init
                scenario_args = inspect.getfullargspec(Scenario.__init__)
                # get only args without default value and not self parameter and capitalize them
                mandatory_args = [a.upper() for a in scenario_args.args[1:-len(scenario_args.defaults)]]
                all_args = [a.upper() for a in scenario_args.args[1:]]
                # check if all mandatory args are in scenario config
                if all(hasattr(scenario_config_module, attr) for attr in mandatory_args):
                    scenario_attrs = []
                    for attr in all_args:
                        # check if attr is in config as some are optional with default value
                        if hasattr(scenario_config_module, attr):
                            scenario_attrs.append(getattr(scenario_config_module, attr))
                    try:
                        # add all attrs which are in config to scenario object
                        scenario = Scenario(*scenario_attrs)
                    except ValueError as value_error:
                        # TODO log value_error
                        continue
                    if any(scen.name == scenario.name for scen in scenarios):
                        # TODO log non-loading of scenario due to name is already given
                        continue
                    scenario.file_name = file_name
                    scenarios.append(scenario)
        return scenarios

    def stringify_arg_value(self, obj, arg):
        value = getattr(obj, arg.lower())
        # add surrounding " if variable is of type string
        # if isinstance(getattr(obj, arg.lower()), str):
        #     value = '"' + value + '"'

        # Prettifying the value for better human readability.
        value_prettified = pprint.pformat(value)
        return value_prettified

    def save_scenarios(self):
        for scenario in self.scenarios:
            # get all parameters of scenario init
            scenario_args = inspect.getfullargspec(Scenario.__init__)
            # all attr
            all_args = [a.upper() for a in scenario_args.args[1:]]
            if hasattr(scenario, "file_name"):
                config_path = self.scenario_path + "/" + scenario.file_name
                with open(config_path, 'r+') as scenario_file:
                    # read in file
                    config_data = scenario_file.read()
                    # exchange all args which are in config file data
                    for arg in all_args:
                        # create regex to find argument with value.
                        replacement = re.compile(arg + r' = .*\n\n', re.DOTALL)  # variables ends with double new lines
                        value = self.stringify_arg_value(scenario, arg)
                        if re.search(replacement, config_data):
                            # substitute current value in config_data. Double new lines are added to help parsing
                            config_data = replacement.sub(arg + ' = ' + value + '\n\n', config_data)
                        else:
                            # get position of last non whitespace char in config data
                            position = config_data.rfind(next((char for char in reversed(config_data) if char != "\n"
                                                               and char != "\t" and char != " "))) + 1
                            arg_value = "\n\n" + arg + " = " + value  # Double new lines are added to help parsing
                            # append argument configuration at position -> end of file + whitespace tail
                            config_data = config_data[:position] + arg_value + config_data[position:]
                    # jump back to begin of file and write new data
                    scenario_file.seek(0)
                    scenario_file.write(config_data)
                    scenario_file.truncate()
            else:
                # create file name without spaces _ and alphanumeric chars only
                file_name = re.sub('[^A-Za-z0-9_ ]+', '', scenario.name).replace(" ", "_").lower()
                if file_name.endswith("scenario"):
                    file_name += ".py"
                else:
                    file_name += "_scenario.py"
                config_path = self.scenario_path + "/" + file_name
                with open(config_path, 'w+') as scenario_file:
                    scenario_file.write('"""\n')
                    scenario_file.write('This file was auto-generated by ScenarioFactory of aTLAS\n')
                    scenario_file.write('"""\n')
                    scenario_file.write("\n\n")
                    for arg in all_args:
                        value = self.stringify_arg_value(scenario, arg)
                        scenario_file.write(arg + " = " + value + "\n\n")  # Double new lines are added to help parsing
                    scenario_file.write("\n\n\n\n")

    def __init__(self):
        project_path = abspath(dirname(__name__))
        # path of scenario_config_module files
        self.scenario_path = project_path + SCENARIO_PATH
        self.scenarios = self.load_scenarios()
        self.init_scenario_number = len(self.scenarios)

    def __del__(self):
        self.save_scenarios()


class ScenarioResult:
    def __init__(self, trust_log, agent_trust_logs):
        self.trust_log = trust_log
        self.agent_trust_logs = agent_trust_logs


class ResultsFactory:
    def list_known_scenario_run_ids(self):
        pass

    def get_results(self, scenario_run_id):
        pass

    def save_results(self, scenario_run_id, scenario_result):
        # get all parameters of ScenarioResult init
        scenario_result_args = inspect.getfullargspec(ScenarioResult.__init__)
        # all attr
        all_args = [a.upper() for a in scenario_result_args.args[1:]]
        file_name = ""
        pass

    def __init__(self):
        project_path = abspath(dirname(__name__))
        # path of scenario_config_module files
        self.scenario_path = project_path + RESULT_PATH

