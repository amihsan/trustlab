# The fianl trustresult is combined through the sum of the 
# values in the logfiles and the corresponding weight given by the scenario file

from trustlab.lab.artifacts.authority import authority
from trustlab.lab.scenarios.h_basic_scenario import WEIGHTS

turstDict = {
}

def finalTrust(ID, entity):
    fo = open(ID + "trust.txt", "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    trust = 0
    result_count = 1
    while fo.tell() < filesize:
        timelog_line = fo.readline()
        if timelog_line[50:51] == entity:
            result_count = result_count + 1

            trust = trust + float(timelog_line[51:-1])
    trust = format((trust)/result_count, '.2f')
    return trust