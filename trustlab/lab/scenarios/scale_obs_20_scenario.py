
NAME = 'Scale Obs 20'

AGENTS = ['A', 'B', 'C', 'D']

OBSERVATIONS = [{'authors': ['A'],
  'before': [],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 0,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [0],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 1,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [1],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 2,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [2],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 3,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [3],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 4,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [4],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 5,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [5],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 6,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [6],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 7,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [7],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 8,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [8],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 9,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [9],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 10,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [10],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 11,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [11],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 12,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [12],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 13,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [13],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 14,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [14],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 15,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [15],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 16,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [16],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 17,
  'receiver': 'B',
  'sender': 'C'},
 {'authors': ['A'],
  'before': [17],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 18,
  'receiver': 'B',
  'sender': 'A'},
 {'authors': ['C'],
  'before': [18],
  'details': {'content_trust.topics': ['Web Engineering']},
  'message': 'Redecentralization of the Web',
  'observation_id': 19,
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
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'B': {'__final__': {'name': 'weighted_average', 'weights': {}},
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'C': {'__final__': {'name': 'weighted_average', 'weights': {}},
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}},
 'D': {'__final__': {'name': 'weighted_average', 'weights': {}},
       'content_trust.direct_experience': {},
       'content_trust.popularity': {},
       'content_trust.recommendation': {}}}

DESCRIPTION = 'Scalability Test with observation upscaling for WI 2020'
