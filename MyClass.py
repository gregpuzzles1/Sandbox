class MyClass (object):
    def __init__(self, i):
        self._i = i
    def get(self):
        return self._i
    def set(self, i):
        self._i = i
    def __str__(self):
        return str(self._i)
    def __eq__(self, other):
        return self._i == other._i
    def __ne__(self, other):
        return self._i != other._i
    def __hash__(self):
        return hash(self._i) # weak
if __name__ == '__main__':
    myObj1 = MyClass(5)
    print myObj1._i # No privacy!!!
    myObj1.set(10)
    print myObj1.get()
    print str(myObj1) # calls myObj1.__str__()
    print myObj1 # calls myObj1.__str__()
    myObj2 = MyClass(10)
    if (myObj1 == myObj2): # calls myObj1.__eq__(myObj2)
         print 'equal'
    if (myObj1 != myObj2): # calls myObj1.__ne__(myObj2)
        print 'not equal'
    dict = {myObj1:myObj2} # calls myObj1.__hash__()
    del(myObj2)
    del(myObj1)
