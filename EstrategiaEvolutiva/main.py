# -*- encoding: utF-8 -*-
__author__ = 'fredy'
import random
from math import cos,sin
from math import pi
from funciones import *
from GeneraAleatorios import aleatorios
from Mutacion import Mutar
from VerificarExitos import modificar_exitos
from Comparacion import comparar
from Salida import Escribir


def main():
    # [numero_de_variables,X,Y,r,sigma,generaciones]
    variables = [6,300,300,10,0.1,10000]
    TAMANO_POBLACION = 20
    numerito = 20 #PARA VER CADA CUANTAS VECES GUARDAR. %
    exitos = 0
    d=variables[0]
    Q=[] # LISTA DE SIGMAS.
    fun  = 0
    W=variables[1]
    H=variables[2]
    r=variables[3]
    sigma=variables[4]
    generaciones = variables[5]
    #En este paso agregamos todas nuestras sigmas
    for b in range(0,TAMANO_POBLACION):
        Q.append(sigma)
    #d=int(variables[fun][0])
    #abrimos el archivo con el nombre de la función.
    #outfile=open("Resultados/"+variables[fun][4],'w')

    #Comienza la población aleatoria
    poblacion = []
    for t in range(0,TAMANO_POBLACION):
        poblacion.append(aleatorios(W,H,r,d))
    print poblacion
    raw_input("esperad...")
    aptitudes=Elegir(fun,poblacion)
    a ="Poblacion Inicial:"
    print a
    Escribir(outfile,a)
    for  l in range(0,len(poblacion)):
        a = "Indiviuo: " +str(l)
        Escribir(outfile,a)
        a = "\tVector: "+ str(poblacion[l])
        Escribir(outfile,a)
        a= "\tAptitud: " + str(aptitudes[l])
        Escribir(outfile,a)
    mutaciones = []
    for f in range(0,len(poblacion)):
        mutaciones.append(Mutar(poblacion[f],Q[f]))
    aptitudeshijos = Elegir(fun,mutaciones)
    arregloexitos=[]
    for s in range(0,len(poblacion)):
        if comparar(aptitudes[s],aptitudeshijos[s]):
            arregloexitos.append(1)
            m = mutaciones[s]
            ap = aptitudeshijos[s]
            poblacion[s] = m[:] #sustituimos al padre
            aptitudes[s]=ap
        else:
            arregloexitos.append(0)
    g=0
    a = "======================================================================================================================"
    Escribir(outfile,a)
    print "Calculando...."
    while g != generaciones:
        for f in range(0,len(poblacion)):
            mutaciones[f]=Mutar(poblacion[f],Q[f])
        aptitudeshijos = Elegir(fun,mutaciones)
        for s in range(0,len(poblacion)):
            if comparar(aptitudes[s],aptitudeshijos[s]):
                ar= arregloexitos[s]
                arregloexitos[s] = arregloexitos[s]+1
                m = mutaciones[s]
                ap = aptitudeshijos[s]
                poblacion[s] = m[:] #sustituimos al padre
                aptitudes[s]=ap
            if g%numerito ==0:
                Q[s]=modificar_exitos(exitos,Q[s],numerito)
                exitos=0
        g = g+1
    dic = {}
    a= "Poblacion Final:"
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