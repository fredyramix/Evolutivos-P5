__author__ = 'fredy'

import random

def Mutar(v,Q):
    hijo = []
    for i in range(len(v)-1):
        hijo.append(v[i]+random.gauss(0,0.5)*Q)
    hijo.append(v[6])
    return hijo