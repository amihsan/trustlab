from django.db import models


class Scenario:
    @staticmethod
    def consistency_checker(name, agent_list, schedule):
        if isinstance(name, str) or len(name) == 0:
            raise ValueError("Scenario names must be a string and not empty.")
        if not isinstance(agent_list, list) or len(agent_list) <= 1:
            raise ValueError("Scenario agent_list must be a list and describe at least 2 agents.")
        if not isinstance(schedule, dict) or not bool(schedule):
            raise ValueError("Scenario schedule must be a dict and not empty.")
        return True

    def __init__(self, name, agent_list, schedule, description=""):
        self.consistency_checker(name, agent_list, schedule)
        self.name = name
        self.agent_list = agent_list
        self.schedule = schedule
        self.description = description

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name


class ScenarioFactory:
    scenarios = {}

    def load_scenarios(self):
        #load magically all python files
        pass