# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:29:16 2020

@author: ryanl
"""

import pygame
class CAR():
    def __init__(self,bewheels,windows,name,afwheels):
     self.bewheels=bewheels
     self.windows=windows
     self.name=name
     self.afwheels=afwheels
    def wheelSum(self) :   
        return self.bewheels+self.afwheels        
class moto(CAR):
     def __init__(name,windows,bewheels,afwheels):   
        super.__init__(bewheels,windows,name,afwheels):
        self.seat=seat             
        self.handleBar=handleBar