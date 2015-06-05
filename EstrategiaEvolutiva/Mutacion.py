__author__ = 'fredy'

import random

def Mutar(v,Q):
    hijo = []
    for i in range(len(v)-1):
        n=int(v[i]+random.gauss(0,0.5)*Q)
        if i<=2:
            if n >255:
                hijo.append(255)
            elif n<1:
                hijo.append(0)
            else:
                hijo.append(n)
        else:
            if i==3 or i==4:
                if n<0:
                    hijo.append(1)
                else:
                    hijo.append(n)
            elif i==5:
                if n<0:
                    hijo.append(1)
                elif n>25:
                    hijo.append(25)
                else:
                    hijo.append(n)
    return hijo