###############################################
# Authority check
# If the Node is in a list of Authoritynodes
# a weight is added to its baselevel of trust

from trustlab.lab.artifacts.directxp import direct_experience

def authority(ID, entity, scenario_authorities):
    weight = 1.2
    authority_add = float(direct_experience(ID, entity))
    if entity in scenario_authorities:
        authority_add = weight*float(direct_experience(ID, entity))
    return authority_add
