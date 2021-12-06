import math
import pprint
import random
import string
import uuid
from datetime import datetime

context_levels = ['relaxed', 'important', 'critical']
max_seconds_time_delay = 63072000
max_lifetime_delay = 31536000

factors = [
    'content_trust.bias',
    'content_trust.specificity',
    'content_trust.likelihood',
    'content_trust.incentive',
    'content_trust.deception',
    'content_trust.age',
    'content_trust.authority',
    'content_trust.topic',
    'content_trust.provenance',
    'content_trust.direct_experience',
    'content_trust.recommendation',
    'content_trust.related_resources',
    'content_trust.user_expertise',
    'content_trust.popularity',
]

scales = {
    'marsh_briggs': {
        'cooperation': 0.5,
        'default': 0.0,
        'forgivability': -0.5,
        'maximum': 1.0,
        'minimum': -1.0,
        'name': 'Trust Scale by Marsh and Briggs (2009)',
        'package': 'marsh_briggs_scale'
    }
}


class Scenario(object):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Random_' + str(datetime.now().timestamp())
        self.description = ''
        self.agents = []
        self.observations = []
        self.history = {}
        self.scales = {}
        self.metrics = {}
        self.__topics__ = []
        self.__uris__ = []

    def generate(self, observations, agents):
        self.__uris__ = [str(uuid.uuid4()) for _ in range(observations)]
        self.description = f'Randomly generated Scenario with {str(observations)} observations and {str(agents)} agents'
        self.__generateAgentNames__(agents)
        self.__generateTopics__(observations)
        self.__generateObservations__(observations, agents)
        self.__generateHistory__()
        self.__generateScalesPerAgent__()
        self.__generateMetricsPerAgent__()

    def __generateAgentNames__(self, agents):
        for i in range(agents):
            self.agents.append(add_to_string_recursive('', i))

    def __generateTopics__(self, observations, max_length=20):
        letters = string.ascii_letters
        for _ in range(math.ceil(observations * (1 + random.random()))):
            self.__topics__.append(''.join(random.choice(letters) for i in range(random.randint(1, max_length))))

    def __generateObservations__(self, observations, agents_count):
        for i in range(observations):
            observation = {'observation_id': i,
                           'authors': random.sample(self.agents, random.randint(1, min(agents_count, 5))),
                           'before': [i - 1] if i > 0 else [], 'message': generate_message(),
                           'receiver': random.choice(self.agents), 'sender': random.choice(self.agents)}
            # avoid cases where sender equals receiver
            while observation['sender'] == observation['receiver']:
                observation['sender'] = random.choice(self.agents)
            # details
            observation['details'] = {
                'uri': self.__uris__[i],
                'content_trust.context_level': random.choice(context_levels),
                'content_trust.bias': random.random() * 2 - 1,
                'content_trust.deception': random.random() * 2 - 1,
                'content_trust.incentive': random.random() * 2 - 1,
                'content_trust.likelihood': random.random() * 2 - 1,
                'content_trust.specificity': random.random() * 2 - 1,
                'content_trust.topics': random.sample(self.__topics__, random.randint(1, min(len(self.__topics__), 5))),
                'content_trust.related_resources': random.sample(self.__uris__,
                                                                 random.randint(0, min(len(self.__uris__), 10))),
                'content_trust.publication_date': datetime.now().timestamp() - (max_seconds_time_delay *
                                                                                random.random())
            }
            self.observations.append(observation)

    def __generateHistory__(self):
        for agent in self.agents:
            agent_history = []
            for other_agent in self.agents:
                if other_agent != agent:
                    agent_history.append((other_agent, random.choice(self.__uris__), random.random() * 2 - 1))

            if len(agent_history) > 0:
                self.history[agent] = agent_history

    def __generateScalesPerAgent__(self):
        for agent in self.agents:
            self.scales[agent] = scales['marsh_briggs']

    def __generateMetricsPerAgent__(self):
        for agent in self.agents:
            thresholds = sorted([random.random() for _ in range(3)])
            # generate trusted topics
            trusted_topics = {}
            for other_agent in random.sample(self.agents, random.randint(0, len(self.agents))):
                agent_dict = {}
                for topic in random.sample(self.__topics__, random.randint(1, len(self.__topics__))):
                    agent_dict[topic] = random.random() * 2 - 1
                trusted_topics[other_agent] = agent_dict
            # generate weights
            weights = {}
            for factor in factors:
                weights[factor] = random.random()
            prefs = {
                '__final__': {
                    'name': 'weighted_average',
                    'weights': weights
                },
                'content_trust.age_grace_period_seconds': random.random() * 5260000,  # 2 months * random
                'content_trust.authority': random.sample(self.agents, random.randint(0, len(self.agents))),
                'content_trust.context_values': {'critical': thresholds[2], 'important': thresholds[1],
                                                 'relaxed': thresholds[0]},
                'content_trust.deception': random.random() - 1,
                'content_trust.direct_experience': {},
                'content_trust.max_lifetime_seconds': datetime.now().timestamp() - max_lifetime_delay * random.random(),
                'content_trust.popularity': {'peers': random.sample(self.agents, random.randint(1, len(self.agents)))},
                'content_trust.provenance': random.sample(self.agents, random.randint(0, len(self.agents))),
                'content_trust.recency_age_limit': datetime.now().timestamp() - max_lifetime_delay * random.random(),
                'content_trust.recommendation': {},
                'content_trust.related_resources': {},
                'content_trust.topic': trusted_topics,
                'content_trust.user_expertise': {}
            }
            # add enforce lifetime
            if random.random() < 0.3:
                prefs['content_trust.enforce_lifetime'] = {}
            self.metrics[agent] = prefs

    def save(self, filename):
        # name
        file_string = add_to_file_string('NAME', self.name)
        # agents    
        file_string = add_to_file_string('AGENTS', self.agents, file_string)
        # observations
        file_string = add_to_file_string('OBSERVATIONS', self.observations, file_string)
        # history
        file_string = add_to_file_string('HISTORY', self.history, file_string)
        # scales
        file_string = add_to_file_string('SCALES_PER_AGENT', self.scales, file_string)
        # metrics
        file_string = add_to_file_string('METRICS_PER_AGENT', self.metrics, file_string)
        # description
        file_string = add_to_file_string('DESCRIPTION', self.description, file_string)
        open(filename, 'w+').write(file_string)


def add_to_file_string(name, object2add, file_string='\n'):
    return file_string + f'{name} = {pprint.pformat(object2add)}\n\n'


def generate_message(max_length=50):
    letters = string.ascii_lowercase + ' '
    return ''.join(random.choice(letters) for i in range(random.randint(1, max_length)))


def add_to_string_recursive(name, i, letters=string.ascii_uppercase):
    if i < len(letters):
        name += letters[i]
        return name
    else:
        name += letters[0]
        return add_to_string_recursive(name, i - len(letters), letters)
