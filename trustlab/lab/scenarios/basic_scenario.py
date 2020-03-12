# basic scenario for initialization
NAME = "Basic Scenario"
DESCRIPTION = "This is a basic scenario with four agents."

AGENTS = ['A', 'B', 'C', 'D']

AUTHORITY = ['B', 'E']

OBSERVATIONS = ['A,B,a,fruits,apple', 'A,B,g,fruits,banana',]

HISTORY = {'A': {'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}, 'B': {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}, 'C': {'A': 0, 'B': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}, 'D': {'A': 0, 'B': 0, 'C': 0, 'E': 0, 'F': 0, 'G': 0}}

INSTANT_FEEDBACK = {'fruits': 0, 'vegetable': 0.6, 'drinks': 0.3}

TRUST_THRESHOLDS = {'upper_limit': 0.75, 'lower_limit': -0.75}

WEIGHTS = {'direct experience': 1.0, 'recommendation': 1.0, 'popularity': 1.0, 'age': 1.0, 'agreement': 1.0, 'authority': 1.0, 'provenance': 1.0, 'recency': 1.0, 'related resource': 1.0, 'specificity': 1.0, 'topic': 1.0}

METRICS_PER_AGENT = {'A': ['direct experience', 'recommendation'], 'B': ['direct experience', 'recommendation'], 'C': ['direct experience', 'recommendation'], 'D': ['direct experience', 'recommendation']}


