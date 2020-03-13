
NAME = "Basic Authority Scenario"
DESCRIPTION = "This is a basic scenario with four agents and one authority."

AGENTS = ['A', 'B', 'C', 'D']

AUTHORITIES = {'A': ['C'], 'B': ['C'], 'C': [], 'D': ['C']}

OBSERVATIONS = ['A,B,A,Web Engineering,Redecentralization of the Web', 'A,B,A,Web Engineering,Web of Things', 'A,B,A,Web Engineering,Web Assembly', 'C,B,C,Web Engineering,Semantic Web and Linked Open Data', 'C,B,C,Web Engineering,Redecentralization of the Web', 'C,B,C,Web Engineering,Web-based learning']

HISTORY = {'A': {'B': 1.0, 'C': 1.0, 'D': 1.0}, 'B': {'A': 0, 'C': 0, 'D': 1.0}, 'C': {'A': 1.0, 'B': 1.0, 'D': 1.0}, 'D': {'A': 1.0, 'B': 1.0, 'C': 1.0}}

TOPICS = {}

TRUST_THRESHOLDS = {'cooperation': 0.5, 'forgivability': -0.5}

WEIGHTS = {'direct experience': 1.0, 'recommendation': 1.0, 'popularity': 1.0, 'age': 1.0, 'agreement': 1.0, 'authority': 1.0, 'provenance': 1.0, 'recency': 1.0, 'related resource': 1.0, 'specificity': 1.0, 'topic': 1.0}

METRICS_PER_AGENT = {'A': ['authority', 'direct experience', 'popularity', 'recommendation'], 'B': ['authority', 'direct experience', 'popularity', 'recommendation'], 'C': ['authority', 'direct experience', 'popularity', 'recommendation'], 'D': ['authority', 'direct experience', 'popularity', 'recommendation']}


