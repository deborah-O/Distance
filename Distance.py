# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:58:09 2018

@author: mm17do
"""
'''Day 5
File for computing the minimum distance between pubs
'''
import math

def comp_dist(point1, point2):
    return math.sqrt((point1[0] - point2[0]) **2
                     + (point1[1] - point2[1]) **2)    