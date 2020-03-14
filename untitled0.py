# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:29:58 2020

@author: ryanl
"""
import random
"""
n=0
num= n
"""


n=random.randint(1,10)
c=1
while c<5 :
    ans=int((input("請輸入答案:")))

    if ans== n:
        print("答對了 ")  
    if ans > n:
        print(" ") 
    if ans < n:
        print("") 
