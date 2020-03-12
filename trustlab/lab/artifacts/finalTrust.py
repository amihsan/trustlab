# The fianl trustresult is combined through the sum of the 
# values in the logfiles and the corresponding weight given by the scenario file
from trustlab.lab.config import Logging


def final_trust(ID, entity):
    file_name = ID + "_trust_log.txt"
    log_path = Logging.LOG_PATH / file_name
    fo = open(log_path.absolute(), "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    trust = 0
    result_count = 1
    while fo.tell() < filesize:
        timelog_line = fo.readline()
        line_elements = timelog_line.split(" ")
        if line_elements[-2] == entity:
            result_count = result_count + 1

            trust = trust + float(line_elements[-1])
    trust = format((trust)/result_count, '.2f')
    return trust