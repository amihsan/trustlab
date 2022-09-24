import math
from collections import deque
import time
import threading
#import trustlab.serializers.ParserDefinitions as ParserDefinitions
import ParserDefinitions as ParserDefinitions
#import trustlab.serializers.MongoDbConnector as MongoDbConnector
import MongoDbConnector as MongoDbConnector

class ScenarioReader:

    def __init__(self, scenario_name, scenariopath, connector):
        self.filepath = scenariopath
        self.connector = connector
        self.scenario_name = scenario_name
        self.q = deque()
        self.doneItems = []
        self.definitions = deque()
        print("Evaluating Filelines")
        self.numlines = sum(1 for line in open(self.filepath))
        print("Filelines: " + str(self.numlines))
        self.running = False
        self.threads = []
        self.lock = threading.Lock()

    def uploadData(self):
        while self.running or len(self.doneItems) > 0:
            items = []
            max = 0
            while True:
                with self.lock:
                    if len(self.doneItems) == 0 or max >= 100:
                        break
                    item = self.doneItems.pop()
                if item is not None:
                    item[2]["Type"] = item[1]
                    items.append(item[2])
                max+=1

            if len(items) > 0:
                self.connector.add_many_data(self.scenario_name, items)

    def read(self):
        self.running = True

        for n in range(0, 4):
            x = threading.Thread(target=self.uploadData)
            x.start()
            self.threads.append(x)

        percentage = -1.00
        current_line_index = 0

        with open(self.filepath) as file:
            for line in file:
                current_line_index += 1
                if self.numlines > 100000:
                    new_percentage = round((current_line_index / self.numlines), 2)
                else:
                    new_percentage = math.floor((current_line_index / self.numlines) * 100)

                if new_percentage > percentage:
                    percentage = new_percentage

                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)

                    print("Reading current status: " + str(percentage) + "[" + current_time + "]")

                while line is not None and len(line) > 0:
                    line = self.analyze_line(line)

        while len(self.doneItems) > 0:
            time.sleep(0.5)
        self.running = False
        while len(self.threads) > 0:
            for t in self.threads:
                if not t.is_alive():
                    self.threads.remove(t)
            time.sleep(0.5)
        print("reading done!")

    def analyze_line(self, line):
        line = line.strip()

        if len(line) == 0:
            return

        if len(self.definitions) == 0:
            if '=' in line:
                classificationparts = line.split('=', 1)
                userDefinedClasses = [i for i in dir(ParserDefinitions) if type(getattr(ParserDefinitions, i)) is type.__class__]

                if classificationparts[0].strip() in userDefinedClasses:
                    self.definitions.append(eval("ParserDefinitions." + classificationparts[0].strip()))

                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    print(classificationparts[0] + "[" + current_time + "]")

                    return classificationparts[1]
            return ""
        else:
            currentobject = self.definitions.pop()

            line = currentobject.add_line(currentobject, line)

            doneObjects = currentobject.get_done_objects(currentobject)
            if len(doneObjects) > 0:
                for object in doneObjects:
                    with self.lock:
                        self.doneItems.append([self.scenario_name, currentobject.__name__.lower(), object])
                    #self.connector.add_data(self.scenario_name, currentobject.__name__.lower(), object)
                currentobject.clear_objects(currentobject)
                while len(self.doneItems) > 400:
                    time.sleep(0.00001)

            if not currentobject.is_done(currentobject):
                self.definitions.append(currentobject)

            if not currentobject.get_next_object(currentobject) is None:
                self.definitions.append(currentobject.get_next_object(currentobject))

        return line

if __name__ == "__main__":

    CONNECTIONSTRING = "mongodb://localhost:27017"

    connector = MongoDbConnector.MongoDbConnector(CONNECTIONSTRING)

    connector.reset_scenario("Random_1000A-1000O_74970")
    #connector.reset_scenario("Test")
    #connector.reset_scenario("Basic Scenario")

    #reader = ScenarioReader("Basic Scenario", "trustlab/lab/scenarios/basic_scenario.py", connector)
    reader = ScenarioReader("Random_1000A-1000O_74970", "trustlab/lab/scenarios/1000x1000_scenario_2.py", connector)
    reader.read()

