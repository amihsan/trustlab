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
from trustlab.lab.scenarios.h_basic_scenario import TRUSTBEHAVIOR_1
from trustlab.lab.scenarios.h_basic_scenario import TRUSTBEHAVIOR_2
from trustlab.lab.scenarios.h_basic_scenario import AUTHORITY
from trustlab.lab.scenarios.h_basic_scenario import WEIGHTS
from trustlab.lab.scenarios.b_authority_scenario import TRUSTBEHAVIOR_1 as authority_TRUSTBEHAVIOR_1
from trustlab.lab.scenarios.b_authority_scenario import TRUSTBEHAVIOR_2 as authority_TRUSTBEHAVIOR_2
from trustlab.lab.scenarios.d_related_scenario import TRUSTBEHAVIOR_1 as related_TRUSTBEHAVIOR_1
from trustlab.lab.scenarios.d_related_scenario import TRUSTBEHAVIOR_1 as related_TRUSTBEHAVIOR_2

############################################################################
#######---The trust_initilaization function starts with the imported behaviormodels
#######---and checks them for behavior-keywords. Those keywords trigger the specific
#######---function call to calculate the coresponding value from the artifacts.
#######---This is needed to calculate the final trust value


def trust_initialization(nodelog, logrecord):
    credibility_initialization = TRUSTBEHAVIOR_1[nodelog]
    reliability_initialization = TRUSTBEHAVIOR_2[nodelog]
    curtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    ############################Frist Initialization of Trust#################################################

    if 'direct' in credibility_initialization:
        if logrecord[2:3] in AUTHORITY:
            credibility_value = str(format(float(WEIGHTS["direct"]) * float(authority(nodelog, logrecord[2:3])), '.2f'))
            fo = open(nodelog + "trust.txt", "ab+")
            fo.write(
                bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                    'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()
        else:
            credibility_value = str(format(float(WEIGHTS["direct"]) * float(directxp(nodelog, logrecord[2:3])), '.2f'))
            fo = open(nodelog + "trust.txt", "ab+")
            fo.write(
                bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                    'UTF-8') +
                bytes(' ' + credibility_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()

    if 'recom' in credibility_initialization:
        credibility_value = str(format(float(WEIGHTS["recom"]) * float(recommendation(nodelog, logrecord[2:3],
                                                                                      directxp(nodelog,
                                                                                               logrecord[2:3]))),
                                       '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'popul' in credibility_initialization:
        credibility_value = str(format(float(WEIGHTS["popul"]) + float(popularity(logrecord[2:3])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'age' in credibility_initialization:
        credibility_value = str(format(
            float(WEIGHTS["age_check"]) * age_check(nodelog, logrecord[2:3], logrecord[23:26]),
            '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'agree' in credibility_initialization:
        credibility_value = str(format(float(WEIGHTS["agreement"]) * float(
            agreement(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'provenance' in credibility_initialization:
        credibility_value = str(
            format(float(WEIGHTS["prov"]) * float(provenance(nodelog, logrecord[16:18])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'recency' in credibility_initialization:
        credibility_value = str(
            format(float(WEIGHTS["recency"]) * float(recency(nodelog, logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'related' in credibility_initialization:
        credibility_value = str(
            format(float(WEIGHTS["related"]) * float(related(nodelog, logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'specificity' in credibility_initialization:
        credibility_value = str(format(float(WEIGHTS["specificity"]) * float(
            specifi(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'topic' in credibility_initialization:
        credibility_value = str(format(
            float(WEIGHTS["topic"]) * float(topic(nodelog, logrecord[2:3], logrecord[23:26])),
            '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', credibility trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + credibility_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    #################################################

    ############################Second Initialization of Trust#################################################
    if 'direct' in reliability_initialization:
        if logrecord[2:3] in AUTHORITY:
            reliability_value = str(format(float(WEIGHTS["direct"]) * float(authority(nodelog, logrecord[2:3])), '.2f'))
            fo = open(nodelog + "trust.txt", "ab+")
            fo.write(
                bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                    'UTF-8') +
                bytes(' ' + reliability_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()
        else:
            reliability_value = str(format(float(WEIGHTS["direct"]) * float(directxp(nodelog, logrecord[2:3])), '.2f'))
            fo = open(nodelog + "trust.txt", "ab+")
            fo.write(
                bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                    'UTF-8') +
                bytes(' ' + reliability_value, 'UTF-8') +
                bytes("\n", 'UTF-8'))
            fo.close()

    if 'recom' in reliability_initialization:
        reliability_value = str(format(float(WEIGHTS["recom"]) * float(recommendation(nodelog, logrecord[2:3],
                                                                                      directxp(nodelog,
                                                                                               logrecord[2:3]))),
                                       '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'popul' in reliability_initialization:
        reliability_value = str(format(float(WEIGHTS["popul"]) + float(popularity(logrecord[2:3])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'age' in reliability_initialization:
        reliability_value = str(
            format(float(WEIGHTS["age_check"]) * age_check(nodelog, logrecord[2:3], logrecord[23:26]), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'agree' in reliability_initialization:
        reliability_value = str(
            format(float(WEIGHTS["agreement"]) * float(agreement(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'provenance' in reliability_initialization:
        reliability_value = str(format(float(WEIGHTS["prov"]) * float(provenance(nodelog, logrecord[16:18])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'recency' in reliability_initialization:
        reliability_value = str(format(float(WEIGHTS["recency"]) * float(recency(nodelog, logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'related' in reliability_initialization:
        reliability_value = str(format(float(WEIGHTS["related"]) * float(related(nodelog, logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'specificity' in reliability_initialization:
        reliability_value = str(
            format(float(WEIGHTS["specificity"]) * float(specifi(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()

    if 'topic' in reliability_initialization:
        reliability_value = str(
            format(float(WEIGHTS["topic"]) * float(topic(nodelog, logrecord[2:3], logrecord[23:26])), '.2f'))
        fo = open(nodelog + "trust.txt", "ab+")
        fo.write(
            bytes(curtime + ', reliability trustvalue from: ', 'UTF-8') + bytes(logrecord[2:3],
                                                                                'UTF-8') +
            bytes(' ' + reliability_value, 'UTF-8') +
            bytes("\n", 'UTF-8'))
        fo.close()