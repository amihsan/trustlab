###############################################
# Recommendations
from trustlab.lab.artifacts.directxp import direct_experience


# TODO realize recommendation via network requests
def recommendation(current_agent, other_agent, agents):
    agents_to_ask = [agent for agent in agents if agent != current_agent and agent != other_agent]
    recommendations = [direct_experience(agent, other_agent) for agent in agents_to_ask]
    recommendation_value = sum(recommendations)/len(recommendations) if len(recommendations) > 0 else 0.00
    return recommendation_value


