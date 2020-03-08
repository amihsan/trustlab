import random

def specifi(ID, entity, tag):
    fo = open(ID + ".txt", "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    expresult = 0
    trustvalue = 0
    while fo.tell() < filesize:
        timelog_line = fo.readline()
        if timelog_line[56:58] == tag:
            expresult = random.random()
            trustvalue = format(expresult, '.2f')
    fo.close()
    return trustvalue