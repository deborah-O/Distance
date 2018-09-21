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
    '''Compute the distance between two points, the points should be given as a 
    tuple with x and y co-ords. The function returns the distance, which is 
    computed with pythagoras.'''

    return math.sqrt((point1[0] - point2[0]) **2
                     + (point1[1] - point2[1]) **2)    


def comp_minimum_distance(points):
    '''Compute the minimum dsistance between several points. Givern the list 
    of points, compute ditance between all pairs and return the minimum of 
    these distances'''
    
    result = None
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            distance = comp_dist(points[i], points[j])
            if result ==None:
                result = distance
            elif distance < result:
                result = distance
    return result


point1 = (0,0)
point2 = (1,1)
print(comp_dist(point1, point2))
print(comp_dist(point1, point1))

point3 = (1,0)
list_of_points = [point1, point2, point3]
print(comp_minimum_distance(list_of_points))