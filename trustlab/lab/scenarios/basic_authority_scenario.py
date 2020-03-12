# basic scenario for initialization
NAME = "Basic Authority Scenario"
DESCRIPTION = "This is a basic scenario with four agents and one authority."

AGENTS = ['A', 'B', 'C', 'D']

AUTHORITIES = {'A': ['C'], 'B': ['C'], 'C': [], 'D': ['C']}

OBSERVATIONS = ['A,B,A,fruits,apple', 'A,B,A,fruits,banana', 'C,B,C,fruits,apple', 'C,B,C,fruits,banana']

HISTORY = {'A': {'B': 1.0, 'C': 1.0, 'D': 1.0}, 'B': {'A': 0, 'C': 0, 'D': 1.0}, 'C': {'A': 1.0, 'B': 1.0, 'D': 1.0}, 'D': {'A': 1.0, 'B': 1.0, 'C': 1.0}}

INSTANT_FEEDBACK = {'fruits': 0, 'vegetable': 0.6, 'drinks': 0.3}

TRUST_THRESHOLDS = {'cooperation': 0.5, 'forgivability': -0.5}

WEIGHTS = {'direct experience': 1.0, 'recommendation': 1.0, 'popularity': 1.0, 'age': 1.0, 'agreement': 1.0, 'authority': 1.0, 'provenance': 1.0, 'recency': 1.0, 'related resource': 1.0, 'specificity': 1.0, 'topic': 1.0}

METRICS_PER_AGENT = {'A': ['authority', 'direct experience', 'popularity', 'recommendation'], 'B': ['authority', 'direct experience', 'popularity', 'recommendation'], 'C': ['authority', 'direct experience', 'popularity', 'recommendation'], 'D': ['authority', 'direct experience', 'popularity', 'recommendation']}


