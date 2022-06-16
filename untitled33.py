# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 09:46:27 2022

@author: panna
"""

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

"""@star
@percent
def printer(msg):
    print(msg)"""

def printer(msg):
    print(msg)
printer = star(percent(printer))
printer("Hello")