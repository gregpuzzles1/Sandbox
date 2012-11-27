"""
File: teststudent.py
Unit test suite for the Student class.
"""

from student import Student
import unittest

class TestStudent(unittest.TestCase):
    """Defines a unit test suite for the Student class."""

    def setUp(self):
        """Sets up the test fixture. Scores are 1-5."""
        self._student = Student("TEST", 5)
        for index in xrange(1, 6):
            score = self._student.setScore(index, index)

    def tearDown(self):
        """Cleans up the test fixture after testing."""
        pass

    def testGetAverage(self):
        """Unit test for getAverage."""
        average = self._student.getAverage()
        self.assertEquals(3, average)
    
    def testGetHighScore(self):
        """Unit test for getHighScore."""
        high = self._student.getHighScore()
        self.assertEquals(5, high)

    def testGetName(self):
        """Test case for getName."""
        self.assertEquals("TEST", self._student.getName()) 

    def testGetScore(self):
        """Unit test for getScore."""
        for index in xrange(1, 6):
            score = self._student.getScore(index)
            self.assertEquals(index, score)
        self.assertRaises(IndexError,
                          self._student.getScore,
                          0)
        self.assertRaises(IndexError,
                          self._student.getScore,
                          6)
  
    def testSetScore(self):
        """Unit test for setScore."""
        for index in xrange(1, 6):
            score = self._student.setScore(index, index + 1)
        for index in xrange(1, 6):
            score = self._student.getScore(index)            
            self.assertEquals(index + 1, score) 

# Creates a suite and runs the text-based test on it
suite = unittest.makeSuite(TestStudent)
unittest.TextTestRunner().run(suite)


 


