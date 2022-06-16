# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:45:19 2022

@author: panna
"""
import re

S = "1.1..1.2"

print((re.findall(r'\b(\.?[0-1][0-9][0-9]\.?|\.?[2][0-5][0-5]\.?|.\?[0-9].\?|\.?[0-9][0-9]\.?)\b',S)))