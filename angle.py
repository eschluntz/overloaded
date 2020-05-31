#!/usr/bin/env python3

"""
Angle Class that supports "wrapping around" the zero -> 2pi mark.
Always represents angles in the smallest magnitude possible.
"""

class AngleWrap(object):

    def __init__(self, angle=0, mode="radians"):
        self.angle = angle
        self.mode = mode
