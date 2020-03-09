from datetime import *
from trustlab.lab.artifacts.recommendation import recommendation
from trustlab.lab.artifacts.directxp import directxp
from trustlab.lab.artifacts.popularity import popularity
from trustlab.lab.artifacts.agreement import agreement
from trustlab.lab.artifacts.age import age_check
from trustlab.lab.artifacts.recency import recency
from trustlab.lab.artifacts.relatedRecources import related
from trustlab.lab.artifacts.specificity import specifi
from trustlab.lab.artifacts.provenance import provenance
from trustlab.lab.artifacts.authority import authority
from trustlab.lab.artifacts.topic import topic
from trustlab.lab.config import LOG_PATH

############################################################################
#######---The trust_initilaization function starts with the imported behaviormodels
#######---and checks them for behavior-keywords. Those keywords trigger the specific
#######---function call to calculate the coresponding value from the artifacts.
#######---This is needed to calculate the final trust value

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def trust_initialization(nodelog, logrecord, scenario):
    credibility_initialization = scenario.trust_behavior_1[nodelog]
    reliability_initialization = scenario.trust_behavior_2[nodelog]
    file_name = nodelog + "trust.txt"
    log_path = LOG_PATH / file_name


    ############################Frist Initialization of Trust#################################################

    if 'direct' in credibility_initialization:
        if logrecord[2:3] in scenario.authority:
            credibility_value = str(format(float(scenario.weights["direct"]) * float(authority(nodelog, logrecord[2:3], scenario.authority)), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()
        else:
            credibility_value = str(format(float(scenario.weights["direct"]) * float(directxp(nodelog, logrecord[2:3])), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()

    if 'recom' in credibility_initialization:
        credibility_value = str(format(float(scenario.weights["recom"]) * float(recommendation(nodelog, logrecord[2:3],
                                                                                      directxp(nodelog,
                                                                                               logrecord[2:3]))),
                                       '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'popul' in credibility_initialization:
        credibility_value = str(format(float(scenario.weights["popul"]) + float(popularity(logrecord[2:3])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'age' in credibility_initialization:
        credibility_value = str(format(
            float(scenario.weights["age_check"]) * age_check(nodelog, logrecord[2:3], logrecord[23:26]),
            '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'agree' in credibility_initialization:
        credibility_value = str(format(float(scenario.weights["agreement"]) * float(
            agreement(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'provenance' in credibility_initialization:
        credibility_value = str(
            format(float(scenario.weights["prov"]) * float(provenance(nodelog, logrecord[16:18])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'recency' in credibility_initialization:
        credibility_value = str(
            format(float(scenario.weights["recency"]) * float(recency(nodelog, logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'related' in credibility_initialization:
        credibility_value = str(
            format(float(scenario.weights["related"]) * float(related(nodelog, logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'specificity' in credibility_initialization:
        credibility_value = str(format(float(scenario.weights["specificity"]) * float(
            specifi(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'topic' in credibility_initialization:
        credibility_value = str(format(
            float(scenario.weights["topic"]) * float(topic(nodelog, logrecord[2:3], logrecord[23:26])),
            '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    #################################################

    ############################Second Initialization of Trust#################################################
    if 'direct' in reliability_initialization:
        if logrecord[2:3] in scenario.authority:
            reliability_value = str(format(float(scenario.weights["direct"]) * float(authority(nodelog, logrecord[2:3], scenario.authority)), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
                bytes(' ' + reliability_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()
        else:
            reliability_value = str(format(float(scenario.weights["direct"]) * float(directxp(nodelog, logrecord[2:3])), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
                bytes(' ' + reliability_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()

    if 'recom' in reliability_initialization:
        reliability_value = str(format(float(scenario.weights["recom"]) * float(recommendation(nodelog, logrecord[2:3],
                                                                                      directxp(nodelog,
                                                                                               logrecord[2:3]))),
                                       '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'popul' in reliability_initialization:
        reliability_value = str(format(float(scenario.weights["popul"]) + float(popularity(logrecord[2:3])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'age' in reliability_initialization:
        reliability_value = str(
            format(float(scenario.weights["age_check"]) * age_check(nodelog, logrecord[2:3], logrecord[23:26]), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'agree' in reliability_initialization:
        reliability_value = str(
            format(float(scenario.weights["agreement"]) * float(agreement(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'provenance' in reliability_initialization:
        reliability_value = str(format(float(scenario.weights["prov"]) * float(provenance(nodelog, logrecord[16:18])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'recency' in reliability_initialization:
        reliability_value = str(format(float(scenario.weights["recency"]) * float(recency(nodelog, logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'related' in reliability_initialization:
        reliability_value = str(format(float(scenario.weights["related"]) * float(related(nodelog, logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'specificity' in reliability_initialization:
        reliability_value = str(
            format(float(scenario.weights["specificity"]) * float(specifi(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'topic' in reliability_initialization:
        reliability_value = str(
            format(float(scenario.weights["topic"]) * float(topic(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()


