
NAME = 'Basic Authority Scenario'

AGENTS = ['A', 'B', 'C', 'D']

OBSERVATIONS = [{'author': 'A',
  'before': [],
  'message': 'Redecentralization of the Web',
  'observation_id': 1,
  'receiver': 'B',
  'sender': 'A',
  'topic': 'Web Engineering'},
 {'author': 'A',
  'before': [1],
  'message': 'Web of Things',
  'observation_id': 2,
  'receiver': 'B',
  'sender': 'A',
  'topic': 'Web Engineering'},
 {'author': 'A',
  'before': [2],
  'message': 'Web Assembly',
  'observation_id': 3,
  'receiver': 'B',
  'sender': 'A',
  'topic': 'Web Engineering'},
 {'author': 'C',
  'before': [3],
  'message': 'Semantic Web and Linked Open Data',
  'observation_id': 4,
  'receiver': 'B',
  'sender': 'C',
  'topic': 'Web Engineering'},
 {'author': 'C',
  'before': [4],
  'message': 'Redecentralization of the Web',
  'observation_id': 5,
  'receiver': 'B',
  'sender': 'C',
  'topic': 'Web Engineering'},
 {'author': 'C',
  'before': [5],
  'message': 'Web-based learning',
  'observation_id': 6,
  'receiver': 'B',
  'sender': 'C',
  'topic': 'Web Engineering'}]

HISTORY = {'A': {'B': 1.0, 'C': 1.0, 'D': 1.0},
 'B': {'A': 0, 'C': 0, 'D': 1.0},
 'C': {'A': 1.0, 'B': 1.0, 'D': 1.0},
 'D': {'A': 1.0, 'B': 1.0, 'C': 1.0}}

TRUST_THRESHOLDS = {'cooperation': 0.5, 'forgivability': -0.5}

WEIGHTS = {'content_trust.age': 1.0,
 'content_trust.agreement': 1.0,
 'content_trust.authority': 1.0,
 'content_trust.direct_experience': 1.0,
 'content_trust.popularity': 1.0,
 'content_trust.provenance': 1.0,
 'content_trust.recency': 1.0,
 'content_trust.recommendation': 1.0,
 'content_trust.related resource': 1.0,
 'content_trust.specificity': 1.0,
 'content_trust.topic': 1.0}

METRICS_PER_AGENT = {'A': {'content_trust.authority': ['C'],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'B': {'content_trust.authority': ['C'],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'C': {'content_trust.authority': [],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'D': {'content_trust.authority': ['C'],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}}}

DESCRIPTION = 'This is a basic scenario with four agents and one authority.'

