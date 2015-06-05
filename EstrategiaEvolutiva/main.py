# -*- encoding: utF-8 -*-
__author__ = 'fredy'
import random
from math import cos,sin
from math import pi
import shutil
from funciones import *
import os
from GeneraAleatorios import aleatorios
from Mutacion import Mutar
from VerificarExitos import modificar_exitos
from Comparacion import comparar
from Salida import Escribir


def main():
    dest="padres/"
    # [numero_de_variables,X,Y,r,sigma,generaciones]
    original="imagenes/perrito.jpg"
    fondo="imagenes/white.jpg"
    variables = [6,300,300,25,50]
    GENERACIONES = 10000
    TAMANO_POBLACION = 20
    numerito = 20 #PARA VER CADA CUANTAS VECES GUARDAR. %
    exitos = 0
    d=variables[0] #numero de variables del problema
    Q=[] # LISTA DE SIGMAS.

    fun  = 0
    W=variables[1]
    H=variables[2]
    r=variables[3]
    sigma=variables[4]
    #bandera para saber si son padres o mutaciones
    bandera = True
    #generaciones = variables[5]
    #En este paso agregamos todas nuestras sigmas
    for b in range(0,TAMANO_POBLACION):
        Q.append(sigma)
    #Comienza la población aleatoria
    poblacion = []
    for t in range(0,TAMANO_POBLACION):
        poblacion.append(aleatorios(W,H,r,fondo))
    aptitudes=evaluar(poblacion,original,bandera)
    mutaciones = []
    bandera = False
    for f in range(0,len(poblacion)):
        mutaciones.append(Mutar(poblacion[f],Q[f]))
    #print "================"
    for gg in mutaciones:
        gg.append(fondo)
    aptitudeshijos = evaluar(mutaciones,original,bandera)
    arregloexitos=[]
    #print poblacion
    for s in range(0,len(poblacion)):
        if comparar(aptitudes[s],aptitudeshijos[s]):
            arregloexitos.append(1)
            m = mutaciones[s]
            ap = aptitudeshijos[s]
            poblacion[s] = m[:] #sustituimos al padre
            aptitudes[s]=ap
            ima="mutadas/"+str(s)+".jpg"
            shutil.copy(ima,dest)
        else:
            arregloexitos.append(0)
        poblacion[s][6]="padres/"+str(s)+".jpg"
    g=0
    bandera=False
    print "Calculando...."
    while g != GENERACIONES:
        for f in range(0,len(poblacion)):
            mutaciones[f]=Mutar(poblacion[f],Q[f])
            mutaciones[f].append("mutadas/"+str(f)+".jpg")
        aptitudeshijos = evaluar(mutaciones,original,bandera)
        for s in range(0,len(poblacion)):
            if comparar(aptitudes[s],aptitudeshijos[s]):
                arregloexitos.append(1)
                m = mutaciones[s]
                ap = aptitudeshijos[s]
                poblacion[s] = m[:] #sustituimos al padre
                aptitudes[s]=ap
                ima="mutadas/"+str(s)+".jpg"
                shutil.copy(ima,dest)
            else:
                arregloexitos.append(0)
            poblacion[s][6]="padres/"+str(s)+".jpg"
            if g%numerito ==0:
                Q[s]=modificar_exitos(exitos,Q[s],numerito)
                exitos=0
        g = g+1
    raw_input("Espera")
    dic = {}
    a= "Poblacion Final:"
    raw_input("essss")
    Escribir(outfile,a)

    for  l in range(0,len(poblacion)):
        a= "Indiviuo: " +str(l)
        print a
        Escribir(outfile,a)
        a= "\tVector: "+ str(poblacion[l])
        print a
        Escribir(outfile,a)
        a= "\tAptitud: " + str(aptitudes[l])
        print a
        Escribir(outfile,a)
        a ="\tSigma: " + str(Q[l])
        print a
        Escribir(outfile,a)
        dic[str(l)] = aptitudes[l]
    print dic
    diccionario = dic.items()
    diccionario.sort(key=lambda x: x[1])
    a= "================================El Mejor es==========================================================="
    Escribir(outfile,a)
    a= "Indiviuo: " + str(diccionario[0][0])
    Escribir(outfile,a)
    a= "\tVector: "+ str(poblacion[int(diccionario[0][0])])
    Escribir(outfile,a)
    a= "\tAptitud: " + str(aptitudes[int(diccionario[0][0])])
    Escribir(outfile,a)
    a= "\tSigma: " + str(Q[int(diccionario[0][0])])
    Escribir(outfile,a)
    outfile.close()
main()