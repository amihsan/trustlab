# The fianl trustresult is combined through the sum of the 
# values in the logfiles and the corresponding weight given by the scenario file


from trustlab.lab.config import LOG_PATH

turstDict = {
}

def finalTrust(ID, entity):
    file_name = ID + "trust.txt"
    log_path = LOG_PATH / file_name
    fo = open(log_path.absolute(), "r+")
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