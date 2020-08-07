#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:23:32 2020

@author: benjaminguajardo
"""
from numpy import *
import scipy as sp

A=matrix(sp.rand(3,3))
B=matrix(sp.rand(3,3))
C=A*B

print (f'A=\n{A}')
print (f'B=\n{B}')
print (f'C=\n{C}')