###############################################
# Popularity check
# The popularity is calculated by averagingthe recommendation

from trustlab.lab.config import Logging

def popularity(ID):
    log_path = Logging.LOG_PATH / "observerlog.txt"
    fo = open(log_path.absolute(), "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    result_count = 0
    trustvalue = 0
    while fo.tell() < filesize:
        timelog_line = fo.readline()
        if timelog_line[26:27] == ID:
            if timelog_line[65:69] == '0 |m':
                continue
            popul = float(timelog_line[65:69])

            result_count = result_count + 1

            trustvalue = format(popul/result_count, '.2f')
    fo.close()
    return trustvalue