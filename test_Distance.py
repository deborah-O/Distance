'Tests for distance.py'
import math
from distance import comp_dist, comp_minimum_distance

def test_compute_distance():
    point1 = (0,0)
    point2 = (1,1)
    assert comp_dist(point1, point2) == math.sqrt(2) # No output using asserts mean 
    assert comp_dist(point1, point1) == 0 #that there are no mistakes

def test_compute_minimum_distance():
    point1 = (0,0)
    point2 = (1,1)
    point3 = (1,0)
    list_of_points = [point1, point2, point3]
    assert comp_minimum_distance(list_of_points) == 1
    
import pytest
pytest.main()