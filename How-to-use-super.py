import collections
import logging

logging.basicConfig(level='INFO')

# --- 1. LoggingDict with super() ---

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)

class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

ld = LoggingDict([('red', 1), ('green', 2), ('blue', 3)])
print(ld)
ld['red'] = 10

ld = LoggingOD([('red', 1), ('green', 2), ('blue', 3)])
print(ld)
ld['red'] = 10
print('-' * 20)

# --- 2. Show MRO Call Order ---

def show_call_order(cls, methname):
    classes = [cls for cls in cls.__mro__ if methname in cls.__dict__]
    print('  ==>  '.join('%s.%s' % (cls.__name__, methname) for cls in classes))

show_call_order(LoggingOD, '__setitem__')
show_call_order(LoggingOD, '__iter__')
print('-' * 20)

# --- 3. Validate Call Order Requirements ---

position = LoggingOD.__mro__.index
assert position(LoggingDict) < position(collections.OrderedDict)
assert position(collections.OrderedDict) < position(dict)

# --- 4. Matching Argument Signatures ---

class Shape:
    def __init__(self, *, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self, *, color, **kwds):
        self.color = color
        super().__init__(**kwds)

cs = ColoredShape(color='red', shapename='circle')

# --- 5. Ensuring Root Exists ---

class Root:
    def draw(self):
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, *, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()

class ColoredShape(Shape):
    def __init__(self, *, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()

ColoredShape(color='blue', shapename='square').draw()
print('-' * 20)

# --- 6. Incorporating a Non-Cooperative Class ---

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)

class MoveableAdapter(Root):
    def __init__(self, *, x, y, **kwds):
        self.moveable = Moveable(x, y)
        super().__init__(**kwds)
    def draw(self):
        self.moveable.draw()
        super().draw()

class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass

MovableColoredShape(color='red', shapename='triangle', x=10, y=20).draw()

print('-' * 20)

# --- 7. Complete Example: OrderedCounter ---

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter('abracadabra')
print(oc)
