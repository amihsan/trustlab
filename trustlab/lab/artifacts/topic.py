###############################################
# Topic check

from trustlab.lab.artifacts.directxp import directxp
from trustlab.lab.config import LOG_PATH

def topic(ID, entity, tag):
    file_name = ID + ".txt"
    log_path = LOG_PATH / file_name
    fo = open(log_path.absolute(), "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    result_count = 0
    res_top = 0
    while fo.tell() < filesize:
        timelog_line = fo.readline()
        if timelog_line[56:58] == tag and timelog_line[37:38] == entity:
            res_top = directxp(ID,entity)
            result_count += result_count
    fo.close()
    return format(res_top, '.2f')