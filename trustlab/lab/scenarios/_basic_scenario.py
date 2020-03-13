
NAME = "Basic Scenario"
DESCRIPTION = "This is a basic scenario with four agents."

AGENTS = ['A', 'B', 'C', 'D']

AUTHORITIES = {}

OBSERVATIONS = ['A,B,A,Web Engineering,Redecentralization of the Web', 'A,B,A,Web Engineering,Web of Things', 'A,B,A,Web Engineering,Web Assembly', 'C,B,C,Web Engineering,Semantic Web and Linked Open Data', 'C,B,C,Web Engineering,Redecentralization of the Web', 'C,B,C,Web Engineering,Web-based learning']

HISTORY = {'A': {'B': 1.0, 'C': 1.0, 'D': 1.0}, 'B': {'A': 0, 'C': 0, 'D': 1.0}, 'C': {'A': 1.0, 'B': 1.0, 'D': 1.0}, 'D': {'A': 1.0, 'B': 1.0, 'C': 1.0}}

TOPICS = {}

TRUST_THRESHOLDS = {'cooperation': 0.5, 'forgivability': -0.5}

WEIGHTS = {'direct experience': 1.0, 'recommendation': 1.0, 'popularity': 1.0, 'age': 1.0, 'agreement': 1.0, 'authority': 1.0, 'provenance': 1.0, 'recency': 1.0, 'related resource': 1.0, 'specificity': 1.0, 'topic': 1.0}

METRICS_PER_AGENT = {'A': ['direct experience', 'popularity', 'recommendation'], 'B': ['direct experience', 'popularity', 'recommendation'], 'C': ['direct experience', 'popularity', 'recommendation'], 'D': ['direct experience', 'popularity', 'recommendation']}


