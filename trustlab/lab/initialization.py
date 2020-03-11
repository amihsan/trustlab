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
from trustlab.lab.config import Logging

############################################################################
# ---The trust_initialization function starts with the imported behavior models
# ---and checks them for behavior-keywords. Those keywords trigger the specific
# ---function call to calculate the corresponding value from the artifacts.
# ---This is needed to calculate the final trust value


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def trust_initialization(nodelog, logrecord, scenario):
    file_name = nodelog + "trust.txt"
    log_path = Logging.LOG_PATH / file_name

    #################################################
    # Artifact Calculation

    if 'direct experience' in scenario.trust_behavior_1[nodelog]:
        if logrecord[2:3] in scenario.authority:
            credibility_value = str(format(float(scenario.weights["direct experience"]) * float(authority(nodelog, logrecord[2:3], scenario.authority)), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', direct experience trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()
        else:
            credibility_value = str(format(float(scenario.weights["direct experience"]) * float(directxp(nodelog, logrecord[2:3])), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', direct experience trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()

    if 'recommendation' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(format(float(scenario.weights["recommendation"]) * float(recommendation(nodelog, logrecord[2:3],
                                                                                      directxp(nodelog,
                                                                                               logrecord[2:3]))),
                                       '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', recommendation trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'popularity' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(format(float(scenario.weights["popularity"]) + float(popularity(logrecord[2:3])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', popularity trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'age' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(format(
            float(scenario.weights["age"]) * age_check(nodelog, logrecord[2:3], logrecord[24:26]),
            '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', age trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'agreement' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(format(float(scenario.weights["agreement"]) * float(
            agreement(nodelog, logrecord[2:3], logrecord[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', agreement trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'provenance' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(
            format(float(scenario.weights["provenance"]) * float(provenance(nodelog, logrecord[16:18])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', provenance trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'recency' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(
            format(float(scenario.weights["recency"]) * float(recency(nodelog, logrecord[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', recency trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'related resource' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(
            format(float(scenario.weights["related resource"]) * float(related(nodelog, logrecord[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', related resource trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'specificity' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(format(float(scenario.weights["specificity"]) * float(
            specifi(nodelog, logrecord[2:3], logrecord[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', specificity trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'topic' in scenario.trust_behavior_1[nodelog]:
        credibility_value = str(format(
            float(scenario.weights["topic"]) * float(topic(logrecord[24:26], scenario.instant_feedback)), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', topic trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()


