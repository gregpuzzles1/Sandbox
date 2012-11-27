"""
File: pc2.py

Illustrates the producer/consumer problem with
thread synchronization.
"""

import time, random
from threading import Thread, currentThread, Condition

class SharedCell(object):
    """Shared data for the producer/consumer problem."""
    
    def __init__(self):
        self._data = -1
        self._writeable = True
        self._condition = Condition()

    def setData(self, data):
        """Producer's method to write to shared data."""
        self._condition.acquire()
        while not self._writeable:
            self._condition.wait()
        print "%s setting data to %d" % \
              (currentThread().getName(), data)
        self._data = data
        self._writeable = False
        self._condition.notify()
        self._condition.release()

    def getData(self):
        """Consumer's method to read from shared data."""
        self._condition.acquire()
        while self._writeable:
            self._condition.wait()
        print "%s accessing data %d" % \
              (currentThread().getName(), self._data)
        self._writeable = True
        self._condition.notify()
        self._condition.release()
        return self._data

class Producer(Thread):
    """Represents a producer."""

    def __init__(self, cell, accessCount, sleepMax):
        """Create a producer with the given shared cell,
        number of accesses, and maximum sleep interval."""
        Thread.__init__(self, name = "Producer")
        self._accessCount = accessCount
        self._cell = cell
        self._sleepMax = sleepMax

    def run(self):
        """Announce startup, sleep and write to shared cell
        the given number of times, and announce completion."""
        print "%s starting up" % self.getName()
        for count in range(self._accessCount):
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
    cell = SharedCell()
    producer = Producer(cell, accessCount, 4)
    consumer = Consumer(cell, accessCount, 4)
    print "Starting the threads"
    producer.start()
    consumer.start()

main()
