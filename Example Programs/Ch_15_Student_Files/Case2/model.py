"""
File: model.py

Defines the classes ERModel, Patient, and Condition for an
emergency room scheduler.
"""

from queue import LinkedPriorityQueue

class Condition(object):

    def __init__(self, rank):
        self._rank = rank

    def __cmp__(self, other):
        """Used for comparisons."""
        return cmp(self._rank, other._rank)

    def __str__(self):
        if   self._rank == 1: return "critical"
        elif self._rank == 2: return "serious"
        else:                 return "fair"

class Patient(object):

    def __init__(self, name, condition):
        self._name = name
        self._condition = condition

    def __cmp__(self, other):
        """Used for comparisons."""
        return cmp(self._condition, other._condition)

    def __str__(self):
        return self._name + " / " + str(self._condition)

class ERModel(object):

    # Exercise
