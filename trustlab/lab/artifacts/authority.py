###############################################
# Authority check
# If the Node is in a list of Authoritynodes
# a weight is added to its baselevel of trust

# TODO this ref...
from trustlab.lab.scenarios.h_basic_scenario import AUTHORITY
from trustlab.lab.artifacts.directxp import directxp

def authority(ID, entity):
    weight = 1.2
    authority_add = float(directxp(ID, entity))
    if entity in AUTHORITY:
        authority_add = weight*float(directxp(ID, entity))
    return authority_add
