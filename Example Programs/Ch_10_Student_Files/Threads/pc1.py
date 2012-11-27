"""
File: pc1.py

Illustrates the producer/consumer problem without
thread synchronization.
"""

import time, random
from threading import Thread, currentThread

class SharedCell(object):
    """Shared data for the producer/consumer problem."""
    
    def __init__(self):
        self._data = -1

    def setData(self, data):
        """Producer's method to write to shared data."""
        print "%s setting data to %d" % \
              (currentThread().getName(), data)
        self._data = data

    def getData(self):
        """Consumer's method to read from shared data."""
        print "%s accessing data %d" % \
              (currentThread().getName(), self._data)
        return self._data

class Producer(Thread):
    """Represents a producer."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a producer with the given shared cell,
        number of accesses, and sleep interval."""
        Thread.__init__(self, name = "Producer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepMax = sleepMax

    def run(self):
        """Announce startup, sleep and write to shared cell
        the given number of times, and announce completion."""
        print "%s starting up" % self.getName()
        for count in xrange(self._accessCount):
            time.sleep(random.randint(1, self._sleepMax))
            self._cell.setData(count + 1)
        print "%s is done producing" % self.getName()

class Consumer(Thread):
    """Represents a consumer."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a consumer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Consumer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepMax = sleepMax

    def run(self):
        """Announce startup, sleep and read from shared cell
        the given number of times, and announce completion."""
        print "%s starting up" % self.getName()
        for count in xrange(self._accessCount):
            time.sleep(random.randint(1, self._sleepMax))
            value = self._cell.getData()
        print "%s is done consuming" % self.getName()

def main():
    """Get numberof accesses from the user, create a shared cell,
    and create and start up a producer and a consumer."""
    accessCount = input("Enter the number of accesses: ")
    sleepMax = 4
    cell = SharedCell()
    producer = Producer(cell, accessCount, sleepMax)
    consumer = Consumer(cell, accessCount, sleepMax)
    print "Starting the threads"
    producer.start()
    consumer.start()

main()
