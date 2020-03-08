###############################################
# Agreement check
# The logfile is checked for the right tag and 
# corresponding xp value

from trustlab.lab.artifacts.directxp import directxp

def agreement(ID, entity, tag):
    fo = open(ID + ".txt", "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    aggr = 0
    while fo.tell() < filesize:
        timelog_line = fo.readline()
        if float(directxp(ID, entity)) > 0 and tag == timelog_line[56:58]:
            aggr = aggr  + 0.1
        if float(directxp(ID, entity)) < 0 and tag != timelog_line[56:58]:
            aggr  = aggr  -0.1

        if aggr < -1:
            aggr = -1
        if aggr > 1:
            aggr = 1
    fo.close()
    return format(aggr, '.2f')