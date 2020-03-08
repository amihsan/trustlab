###############################################
#Provenance check

from trustlab.lab.artifacts.directxp import directxp

def provenance(ID, author):
    fo = open(ID + ".txt", "r+")
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
