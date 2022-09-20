import time
import types
from collections import deque
import trustlab.lab.connectors.ParserDefinitions as ParserDefinitions
import trustlab.lab.connectors.MongoDbConnector as MongoDbConnector
import importlib

class ScenarioReader:

    def __init__(self, scenario_name, scenariopath, connector):
        self.filepath = scenariopath
        self.connector = connector
        self.scenario_name = scenario_name
        self.q = deque()
        self.definitions = deque()

    def read(self):
        with open(self.filepath) as file:
            for line in file:
                while len(line) > 0:
                    line = self.analyze_line(line)

    def analyze_line(self, line):
        if len(line) == 0:
            return

        line = line.strip()

        if len(self.definitions) == 0:
            if '=' in line:
                classificationparts = line.split('=', 1)
                userDefinedClasses = [i for i in dir(ParserDefinitions) if type(getattr(ParserDefinitions, i)) is type.__class__]

                if classificationparts[0].strip() in userDefinedClasses:
                    self.definitions.append(eval("ParserDefinitions." + classificationparts[0].strip()))
                    return classificationparts[1]
            return ""
        else:
            currentobject = self.definitions.pop()

            line = currentobject.add_line(currentobject, line)

            doneObjects = currentobject.get_done_objects(currentobject)
            if len(doneObjects) > 0:
                for object in doneObjects:
                    self.connector.add_data(self.scenario_name, currentobject.__name__.lower(), object)
                currentobject.clear_objects(currentobject)

            if not currentobject.is_done(currentobject):
                self.definitions.append(currentobject)

            if not currentobject.get_next_object(currentobject) is None:
                self.definitions.append(currentobject.get_next_object(currentobject))

        return line

if __name__ == "__main__":

    CONNECTIONSTRING = "mongodb://localhost:27017"

    connector = MongoDbConnector.MongoDbConnector(CONNECTIONSTRING)

    reader = ScenarioReader("Basic Scenario", "/mnt/volume_intern/Uni/MA/trustlab/trustlab/lab/scenarios/basic_scenario.py", connector)
    reader.read()

