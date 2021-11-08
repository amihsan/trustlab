
NAME = 'Basic Authority Scenario'

AGENTS = ['A', 'B', 'C', 'D']

OBSERVATIONS = [{'authors': ['A'],
  'before': [],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 1,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['A'],
  'before': [1],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Web of Things',
  'observation_id': 2,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['A'],
  'before': [2],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Web Assembly',
  'observation_id': 3,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [3],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Semantic Web and Linked Open Data',
  'observation_id': 4,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['C'],
  'before': [4],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 5,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['C'],
  'before': [5],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Web-based learning',
  'observation_id': 6,
  'receiver': 'B',
  'sender': 'C'}]

HISTORY = {'A': {'B': 1.0, 'C': 1.0, 'D': 1.0},
 'B': {'A': 0, 'C': 0, 'D': 1.0},
 'C': {'A': 1.0, 'B': 1.0, 'D': 1.0},
 'D': {'A': 1.0, 'B': 1.0, 'C': 1.0}}

SCALES_PER_AGENT = {'A': {'cooperation': 0.5,
       'default': 0.0,
       'forgivability': -0.5,
       'maximum': 1.0,
       'minimum': -1.0,
       'name': 'Trust Scale by Marsh and Briggs (2009)',
       'package': 'marsh_briggs_scale'},
 'B': {'cooperation': 0.5,
       'default': 0.0,
       'forgivability': -0.5,
       'maximum': 1.0,
       'minimum': -1.0,
       'name': 'Trust Scale by Marsh and Briggs (2009)',
       'package': 'marsh_briggs_scale'},
 'C': {'cooperation': 0.5,
       'default': 0.0,
       'forgivability': -0.5,
       'maximum': 1.0,
       'minimum': -1.0,
       'name': 'Trust Scale by Marsh and Briggs (2009)',
       'package': 'marsh_briggs_scale'},
 'D': {'cooperation': 0.5,
       'default': 0.0,
       'forgivability': -0.5,
       'maximum': 1.0,
       'minimum': -1.0,
       'name': 'Trust Scale by Marsh and Briggs (2009)',
       'package': 'marsh_briggs_scale'}}

METRICS_PER_AGENT = {'A': {'__final__': {'name': 'weighted_average', 'weights': {}},
       'content_trust.authority': ['C'],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'B': {'__final__': {'name': 'weighted_average', 'weights': {}},
       'content_trust.authority': ['C'],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'C': {'__final__': {'name': 'weighted_average', 'weights': {}},
       'content_trust.authority': [],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'D': {'__final__': {'name': 'weighted_average', 'weights': {}},
       'content_trust.authority': ['C'],
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}}}

DESCRIPTION = 'This is a basic scenario with four agents and one authority.'
