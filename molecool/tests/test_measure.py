"""
Tests for the measure module
"""

# imports
import molecool
import numpy as np

def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle():
    p1 = np.array([0, 0, -1])
    p2 = np.array([0, 0, 0])
    p3 = np.array([1, 0, 0])

    expected_angle = 90.0

    calculated_angle = molecool.calculate_angle(p1,p2,p3,degrees=True)

    assert expected_angle == calculated_angle
