# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:51:36 2018

@author: Mateusz
"""
from multiprocessing.dummy import Pool as ThreadPool 
from math import *
import random
import itertools
def get_input():
    number_func=int(input("podaj liczbe funkcji warunkowych: "))
    number_var=int(input("podaj liczbę zmiennych: "))
    list_func=[None]*number_func #tworzy listę funkcji
    dict_var=dict() #tworzy slownik zmiennych jeden punkt
    for t in range (0,number_func):
        list_func[t]=str(input("podaj wzór {} funkcji: ".format(t+1)))
        list_func[t]=list_func[t].replace("^","**")
    for c in range (0,number_var):
        var=str(input("Podaj nazwe {} zmiennej: ".format(c+1)))
        dict_var[var]=0
    goal_func=str(input("podaj wzór funkcji celu: "))
    goal_func=goal_func.replace("^","**")
    goal_max_min=str(input("max/min? "))
    print(dict_var)
    return((list_func,dict_var,goal_func,goal_max_min))


def random_points(dict_var,size):
    k=100#wielkoć listy
    list_dict_var=[0]*k #o=pusta lista
    for t in range (0,k):
        list_dict_var[t]=dict_var.copy()
    for key in dict_var:
            for element in list_dict_var:
                element[key]=round(random.uniform(-size+dict_var[key],size+dict_var[key]),5)
    return list_dict_var


def check(dictionary,list_func):
#    print(list_func)
    i=dictionary.copy()
    for element in list_func:
        if not eval(element,i):
            return 
    return dictionary


def find_max(list_dict_var,max_dict_var,goal_func):
    max_value=eval(goal_func,max_dict_var)
    for element in list_dict_var:
        e=element.copy()
        if max_value<eval(goal_func,e):
            max_value=eval(goal_func,e)
            max_dict_var=element
    return (max_dict_var,max_value)


def find_min(list_dict_var,min_dict_var,goal_func):
    min_dict_var_copy=min_dict_var.copy()
    min_value=eval(goal_func,min_dict_var_copy)
    for element in list_dict_var:
        e=element.copy()
        if min_value>eval(goal_func,e):
            min_value=eval(goal_func,e)
            min_dict_var=element
    return (min_dict_var,min_value)


def main(): 
#    data=get_input() #(list_func,dict_var,goal_func,goal_max_min)
#    print(data)
#    list_dict_var=[{'x': 111}, {'x': -146}, {'x': -427}, {'x': 94}, {'x': 257}, {'x': -530}, {'x': -60}, {'x': 495}, {'x': -202}, {'x': 686}]
    data=(['x**2-1<y','x-y<0'], {'x': 100,'y': 100,}, 'x+y', 'min')
    dict_var=data[1].copy()
    diff=100
    value_before=0
    value_after=0
    size=100
    while diff>0.001:
        list_dict_var=random_points(dict_var,size)#list_dict_var
        pool = ThreadPool(4) 
        list_dict_var = pool.starmap(check, zip(list_dict_var, itertools.repeat(data[0])))
        pool.close() 
        pool.join()
        list_dict_var = [i for i in list_dict_var if i is not None]
        print(list_dict_var)
        if len(list_dict_var)==0:
            continue
        if data[3]=='max':
            i=find_max(list_dict_var,dict_var,data[2])
            dict_var=i[0]
            if value_after==i[1]:
                continue
            value_before=value_after
            value_after=i[1]
            if abs(value_before)!=abs(value_after):
                diff=abs(value_before-value_after) 
            size=1/2 *size
        if data[3]=='min':
            i=find_min(list_dict_var,dict_var,data[2])
            dict_var=i[0]
            if value_after==i[1]:
                continue
            value_before=value_after
            value_after=i[1]
            if abs(value_before)!=abs(value_after):
                diff=abs(value_before-value_after)
            size=1/2 *size
    return(dict_var,value_after,diff)
            

list_dict_var=[{'x': -43754, 'y': -16419}, {'x': 77137, 'y': -35325}, {'x': 24773, 'y': -56420}, {'x': 73809, 'y': 49738}, {'x': 36913, 'y': 35501}, {'x': 53697, 'y': -532}, {'x': 91539, 'y': -22221}, {'x': -89862, 'y': -44217}, {'x': 691, 'y': 43046}, {'x': -93157, 'y': -30578}]
data=(['x>3','x+y>3','x<1000000'], {'x': 100000,'y': 100000,}, 'x+y', 'min')
print(main())
