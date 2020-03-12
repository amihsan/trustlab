
NAME = "Basic Topic Scenario"
DESCRIPTION = "This is a basic scenario with four agents, one authority and a topic metric."

AGENTS = ['A', 'B', 'C', 'D']

AUTHORITIES = {'A': ['C'], 'B': ['C'], 'C': [], 'D': ['C']}

OBSERVATIONS = ['A,B,A,fruits,apple', 'A,B,A,fruits,banana', 'C,B,C,vegetable,potato', 'C,B,C,vegetable,cucumber']

HISTORY = {'A': {'B': 1.0, 'C': 1.0, 'D': 1.0}, 'B': {'A': 0, 'C': 0, 'D': 1.0}, 'C': {'A': 1.0, 'B': 1.0, 'D': 1.0}, 'D': {'A': 1.0, 'B': 1.0, 'C': 1.0}}

TOPICS = {'A': {'B': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}, 'C': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}, 'D': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}}, 'B': {'A': {'fruits': 0.5, 'vegetable': 0.5, 'drinks': 0.5}, 'C': {'fruits': 0.5, 'vegetable': 0.5, 'drinks': 0.5}, 'D': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}}, 'C': {'A': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}, 'B': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}, 'D': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}}, 'D': {'A': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}, 'B': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}, 'C': {'fruits': 1.0, 'vegetable': 1.0, 'drinks': 1.0}}}

TRUST_THRESHOLDS = {'cooperation': 0.5, 'forgivability': -0.5}

WEIGHTS = {'direct experience': 1.0, 'recommendation': 1.0, 'popularity': 1.0, 'age': 1.0, 'agreement': 1.0, 'authority': 1.0, 'provenance': 1.0, 'recency': 1.0, 'related resource': 1.0, 'specificity': 1.0, 'topic': 1.0}

METRICS_PER_AGENT = {'A': ['authority', 'direct experience', 'popularity', 'recommendation', 'topic'], 'B': ['authority', 'direct experience', 'popularity', 'recommendation', 'topic'], 'C': ['authority', 'direct experience', 'popularity', 'recommendation', 'topic'], 'D': ['authority', 'direct experience', 'popularity', 'recommendation', 'topic']}


