NAME = 'Travos Test Scenario'

AGENTS = ['A', 'B', 'C', 'D']

OBSERVATIONS = [{'authors': ['A'],
                 'before': [],
                 'details': {'uri': 'http://example.com/Redecentralization_of_the_Web'},
                 'message': 'Redecentralization of the Web',
                 'observation_id': 1,
                 'receiver': 'B',
                 'sender': 'A'},
                {'authors': ['A'],
                 'before': [1],
                 'details': {'uri': 'http://example.com/Web_of_Things'},
                 'message': 'Web of Things',
                 'observation_id': 2,
                 'receiver': 'B',
                 'sender': 'A'},
                {'authors': ['A'],
                 'before': [2],
                 'details': {'uri': 'http://example.com/Web_Assembly'},
                 'message': 'Web Assembly',
                 'observation_id': 3,
                 'receiver': 'B',
                 'sender': 'A'},
                {'authors': ['C'],
                 'before': [3],
                 'details': {'uri': 'http://example.com/Semantic_Web_and_Linked_Open_Data'},
                 'message': 'Semantic Web and Linked Open Data',
                 'observation_id': 4,
                 'receiver': 'B',
                 'sender': 'C'},
                {'authors': ['C'],
                 'before': [4],
                 'details': {'uri': 'http://example.com/Redecentralization_of_the_Web'},
                 'message': 'Redecentralization of the Web',
                 'observation_id': 5,
                 'receiver': 'B',
                 'sender': 'C'},
                {'authors': ['C'],
                 'before': [5],
                 'details': {'uri': 'http://example.com/Web-based_learning'},
                 'message': 'Web-based learning',
                 'observation_id': 6,
                 'receiver': 'B',
                 'sender': 'C'}]

HISTORY = {'A': [['B', 'http://example.com/Semantic_Web_and_Linked_Open_Data', 0.55],
                 ['C', 'http://example.com/Web-based_learning', 0.66],
                 ['D', 'http://example.com/Redecentralization_of_the_Web', 0.70]],
           'B': [['A', 'http://example.com/Redecentralization_of_the_Web', 0.60],
                 ['C', 'http://example.com/Web-based_learning', 0.65],
                 ['D', 'http://example.com/Web_Assembly', 0.75]],
           'C': [['A', 'http://example.com/Semantic_Web_and_Linked_Open_Data', 0.80],
                 ['B', 'http://example.com/Web-based_learning', 0.75],
                 ['D', 'http://example.com/Web_of_Things', 0.74]],
           'D': [['A', 'http://example.com/Redecentralization_of_the_Web', 0.50],
                 ['B', 'http://example.com/Redecentralization_of_the_Web', 0.85],
                 ['C', 'http://example.com/Redecentralization_of_the_Web', 0.45]]}



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

METRICS_PER_AGENT = {'A': {'__final__': {'name': 'travos'},
                           'travos.experience': {},
                           'travos.opinion': {}},
                     'B': {'__final__': {'name': 'travos'},
                           'travos.experience': {},
                           'travos.opinion': {}},
                     'C': {'__final__': {'name': 'travos'},
                           'travos.experience': {},
                           'travos.opinion': {}},
                     'D': {'__final__': {'name': 'travos'},
                           'travos.experience': {},
                           'travos.opinion': {}}}

DESCRIPTION = 'This is a basic scenario with four agents.'