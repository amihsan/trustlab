###############################################
# Topic check

from trustlab.lab.artifacts.directxp import directxp
from trustlab.lab.config import Logging


def topic(tag, topic_dict):
    return format(topic_dict[tag], '.2f')