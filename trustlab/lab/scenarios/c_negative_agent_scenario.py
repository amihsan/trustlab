#scenario with one heavily negative agent
NAME = "Negative Agent Scenario"
DESCRIPTION = "This is a scenario with one heavily negative Agent."

AGENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

#F is negative

AUTHORITY = ['B', 'E']

OBSERVATIONS = ['A,B,a,k1,apple', 'B,C,g,k1,banana', 'C,D,e,k3,car', 'D,E,g,k2,cauliflower', 'E,F,a,k1,apricot', 'F,G,b,k3,house', 'G,A,d,k1,artichoke', 'A,G,c,k1,cherries', 'B,F,g,k1,apple', 'C,E,e,k3,knive', 'D,C,f,k1,banana', 'E,B,a,k1,pineapple', 'F,C,b,k3,house', 'G,B,e,k2,cauliflower', 'A,F,b,k1,apricot', 'B,E,c,k2,artichoke', 'C,F,d,k3,brick', 'D,B,e,k1,pineapple', 'E,A,f,k1,cherries', 'F,B,g,k3,car', 'G,C,a,k1,apricot', 'A,E,b,k2,artichoke', 'B,D,c,k1,apricot', 'C,B,d,k3,hammer', 'D,A,e,k1,cherries', 'E,C,f,k1,banana', 'F,A,g,k3,brick', 'G,D,a,k2,onion', 'A,C,g,k1,banana', 'B,G,f,k2,artichoke', 'C,G,e,k3,house', 'D,F,c,k2,cauliflower', 'E,G,d,k1,banana', 'F,D,a,k3,stone', 'G,E,b,k1,apricot', 'A,D,c,k1,banana', 'B,A,d,k1,cheriies', 'C,A,e,k3,house', 'D,G,f,k2,onion', 'E,D,g,k2,onion', 'F,E,a,k3,brick', 'G,F,b,k2,cauliflower']



INSTANT_FEEDBACK = {'k0': 0, 'k1': 0.6, 'k2': 0.3, 'k3': -0.7}


TRUST_THRESHOLD = {'UpperLimit': 0.75, 'LowerLimit': -0.75}


WEIGHTS = {'direct': 1.2, 'recom': 1.2, 'popul': 1.2, 'age_check': 1.2, 'agreement': 1.2, 'authority': 1.2, 'prov': 1.2, 'recency': 1.2, 'related': 1.2, 'specificity': 1.2, 'topic': 1.2}


#The more importent/focused artifacts for this scenario
TRUST_BEHAVIOR_1 = {'A': ['direct', 'recom', 'popul', 'authority'], 'B': ['direct', 'recom', 'popul', 'authority'], 'C': ['direct', 'recom', 'popul', 'authority'], 'D': ['direct', 'recom', 'popul', 'authority'], 'E': ['direct', 'recom', 'popul', 'authority'], 'F': ['direct', 'recom', 'popul', 'authority'], 'G': ['direct', 'recom', 'popul', 'authority']}

#he secondary artifacts fpr this scenario
TRUST_BEHAVIOR_2 = {'A': ['age', 'agree', 'provenance', 'recency', 'related', 'specificity', 'topic'], 'B': ['age', 'agree', 'provenance', 'recency', 'related', 'specificity', 'topic'], 'C': ['age', 'agree', 'provenance', 'recency', 'related', 'specificity', 'topic'], 'D': ['age', 'agree', 'provenance', 'recency', 'related', 'specificity', 'topic'], 'E': ['age', 'agree', 'provenance', 'recency', 'related', 'specificity', 'topic'], 'F': ['age', 'agree', 'provenance', 'recency', 'related', 'specificity', 'topic'], 'G': ['age', 'agree', 'provenance', 'recency', 'related', 'specificity', 'topic']}

