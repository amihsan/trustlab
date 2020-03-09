###############################################
# Authority check
# If the Node is in a list of Authoritynodes
# a weight is added to its baselevel of trust

from trustlab.lab.artifacts.directxp import directxp

def authority(ID, entity, scenario_authorities):
    weight = 1.2
    authority_add = float(directxp(ID, entity))
    if entity in scenario_authorities:
        authority_add = weight*float(directxp(ID, entity))
    return authority_add
