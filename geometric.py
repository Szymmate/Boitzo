# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:53:44 2018
/tak wczytac/
@author: Mateusz
"""
import json
import math
import numpy as np
from scipy.stats import gmean


def toeigenvalue(data):
    for k, v in data.items():
        if isinstance(v, dict):
            toeigenvalue(v)
        else:
            if k!='alternatives':
                sqrt=int(math.sqrt(len(v)))
#                print(v)
                v=np.asmatrix(v)
                v=v.reshape(sqrt,sqrt)
#                print(v,0)
                v=gmean(v, axis=1)
#                print(v)
                v=(v.T).tolist()
                lista=[]
#                print(lista)
                for x in v:
                    for y in x:
                        lista.append(y)
                lista=np.asarray(lista)
                i=0
#                print(lista)
                suma=sum(lista)
#                print(suma)
                while i<lista.size:
                    lista[i]=lista[i]/suma
                    i=i+1
                data[k]=lista
                del lista
#                print(data[k])
    return data

def sumeigenvalue(data,lista):
    for k, v in data.items():
        if isinstance(v, dict):
           global parent_k
           global finalvector
           finalvector=0
           parent_k=k
           sumeigenvalue(v,lista)
        else:
            if k!='alternatives':
                if k=='matrix':
                    finalvector=0
                    i=0
                    critvector=v
                else:
                    finalvector=finalvector+critvector[i]*v
                    i=i+1
                    if i==critvector.size:
                        lista.append((parent_k, finalvector))
            
def replace_dict(data,lista):
    for k,v in data.items():
        for element in lista:
            if k==element[0]:
                data[k]=element[1]
    if isinstance(v, dict):
        data=v
        replace_dict(data,lista)

            
def choose_alternative(data):    
    new=toeigenvalue(data)
    while isinstance(new['Goal'], dict):    
        sumeigenvalue(new,lista)
        replace_dict(new,lista)
    i=0
    start=new['Goal'][0]
    for element in new['Goal']:
        if element >start:
            start=element
            i=i+1
    print(new['Goal'])
    print("Najlepszą opcją wedlug geo jest: {}".format(new['alternatives'][i]))




f=open('model.json', 'r')
data=json.load(f)
global lista
lista=[]
choose_alternative(data)
