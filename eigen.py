# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:53:44 2018
/tak wczytac/
@author: Mateusz
"""
import json
import math
import numpy as np
from numpy import linalg as LA
with open('example.json', 'r') as f:
    data=json.load(f)
    def myprint(data):
     for k, v in data.items():
         if isinstance(v, dict):
             myprint(v)
         else:
             if k!='alternatives':
                 sqrt=int(math.sqrt(len(v)))
                 v=np.asmatrix(v)
                 v=v.reshape(sqrt,sqrt)
                 v=LA.eig(v)
                 print(v[0])
    myprint(data)
             