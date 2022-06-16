# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:15:34 2022

@author: panna
"""

class shape:
    def __init__(self,a,b=1):
        self.a = a
        self.b = b
        
    def circle_area(self):
        return self.a**2*3.142
    def rec_area(self):
        return self.a*self.b