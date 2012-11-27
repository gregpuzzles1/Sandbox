"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self._name
  
    def setScore(self, i, score):
        """Resets the ith score.
        Preconditions: 1 <= i <= number of scores
                       0 <= score <= 100
        Postcondition: score at ith position is reset to score.
        Raises: IndexError if i < 1 or i > number of scores
                ValueError if score < 0 or score > 100"""
        if i < 1 or i > len(self._scores):
            raise IndexError, "Position out of range"
        if score < 0 or score > 100:
            raise ValueError, "Score out of range"
        self._scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1.
        Precondition: 1 <= i <= number of scores
        Raises: IndexError if i < 1 or i > number of scores"""
        if i < 1 or i > len(self._scores):
            raise IndexError,  "Position out of range"
        return self._scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        sum = reduce(lambda x, y: x + y, self._scores)
        return sum / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return reduce(lambda x, y: max(x, y), self._scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self._name  + "\nScores: " + \
               " ".join(map(str, self._scores))


