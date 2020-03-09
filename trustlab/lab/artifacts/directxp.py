###############################################
# Direct Experience
# The tag values in the logfiles are combined to the Direct XP via the median

from trustlab.lab.config import LOG_PATH

def directxp(ID, entity2):
    file_name = ID + ".txt"
    log_path = LOG_PATH / file_name
    fo = open(log_path.absolute(), "r+")
    logfile = fo.read()
    filesize = len(logfile)
    fo.seek(0)
    result_count = 0
    expresult = 0
    trustvalue = 0
    while fo.tell() < filesize:
        timelog_line = fo.readline()

        if timelog_line[37:38] == entity2:
            service_satisfaction = timelog_line[59:63]
            if timelog_line[59:63] == '0 |m':
                service_satisfaction = timelog_line[59:60]
            result_count = result_count + 1
            expresult += float(service_satisfaction)
            trustvalue = format(expresult/result_count, '.2f')
    fo.close()
    return trustvalue
