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
from trustlab.lab.config import Logging, get_current_time

############################################################################
# ---The trust_initialization function starts with the imported behavior models
# ---and checks them for behavior-keywords. Those keywords trigger the specific
# ---function call to calculate the corresponding value from the artifacts.
# ---This is needed to calculate the final trust value


def calc_trust_metrics(current_agent, current_message, scenario):
    file_name = current_agent + "trust.txt"
    log_path = Logging.LOG_PATH / file_name

    #################################################
    # Artifact Calculation

    if 'direct experience' in scenario.metrics_per_agent[current_agent]:
        if current_message[2:3] in scenario.authority:
            credibility_value = str(format(float(scenario.weights["direct experience"]) * float(authority(current_agent, current_message[2:3], scenario.authority)), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', direct experience trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()
        else:
            credibility_value = str(format(float(scenario.weights["direct experience"]) * float(directxp(current_agent, current_message[2:3])), '.2f'))
            fo = open(log_path.absolute(), "ab+")
            fo.write(
                bytes(get_current_time() + ', direct experience trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()

    if 'recommendation' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(format(float(scenario.weights["recommendation"]) * float(recommendation(current_agent, current_message[2:3],
                                                                                                        directxp(current_agent,
                                                                                                                 current_message[2:3]))),
                                       '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', recommendation trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'popularity' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(format(float(scenario.weights["popularity"]) + float(popularity(current_message[2:3])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', popularity trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'age' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(format(
            float(scenario.weights["age"]) * age_check(current_agent, current_message[2:3], current_message[24:26]),
            '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', age trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'agreement' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(format(float(scenario.weights["agreement"]) * float(
            agreement(current_agent, current_message[2:3], current_message[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', agreement trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'provenance' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(
            format(float(scenario.weights["provenance"]) * float(provenance(current_agent, current_message[16:18])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', provenance trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'recency' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(
            format(float(scenario.weights["recency"]) * float(recency(current_agent, current_message[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', recency trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'related resource' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(
            format(float(scenario.weights["related resource"]) * float(related(current_agent, current_message[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', related resource trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'specificity' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(format(float(scenario.weights["specificity"]) * float(
            specifi(current_agent, current_message[2:3], current_message[24:26])), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', specificity trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'topic' in scenario.metrics_per_agent[current_agent]:
        credibility_value = str(format(
            float(scenario.weights["topic"]) * float(topic(current_message[24:26], scenario.instant_feedback)), '.2f'))
        fo = open(log_path.absolute(), "ab+")
        fo.write(
            bytes(get_current_time() + ', topic trustvalue from: ', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()


