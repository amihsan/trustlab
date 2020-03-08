###############################################
# Topic check

from trustlab.lab.artifacts.directxp import directxp

def topic(ID, entity, tag):
    fo = open(ID + ".txt", "r+")
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