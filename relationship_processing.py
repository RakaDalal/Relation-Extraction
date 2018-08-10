#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:47:16 2018

@author: rakadalal
"""

import pickle


with open('processed_tuples.pkl', 'rb') as f:
    data = pickle.load(f)
    
print data[0]