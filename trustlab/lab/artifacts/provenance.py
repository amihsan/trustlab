###############################################
#Provenance check

from trustlab.lab.config import Logging
from trustlab.lab.artifacts.directxp import directxp

def provenance(ID, author):
    file_name = ID + ".txt"
    log_path = Logging.LOG_PATH / file_name
    fo = open(log_path.absolute(), "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    expresult = 0
    AUTHOR = author.upper()
    while fo.tell() < filesize:
        timelog_line = fo.readline()
        if timelog_line[48:49] == author:
            expresult = directxp(ID, AUTHOR)
            #print(expresult)
        expresult = expresult
    fo.close()
    return format(expresult, '.2f')
