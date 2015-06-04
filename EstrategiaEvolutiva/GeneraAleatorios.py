import random

__author__ = 'fredy'

#Primer generacion aleatoria.
'''Vector = []
    R= random.randint(0,255)
    G= random.randint(0,255)
    B= random.randint(0,255)
    X= random.randint(0,HIGH)
    Y= random.randint(0,WIDTH)
    r= random.randint(0,10)'''

def aleatorios(w,h,r,fondo):
    vector = []
    vector.append(random.randint(0,255))
    vector.append(random.randint(0,255))
    vector.append(random.randint(0,255))
    vector.append(random.randint(0,w-100))
    vector.append(random.randint(0,h-100))
    vector.append(r)
    vector.append(fondo)
    return vector