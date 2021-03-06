"""Handle interaction with keyboard and mouse"""

import pygame
import common
pymunk = common.pymunk

#These represet mouse states we can query.
M_LEFT = 0
M_MIDDLE = 1
M_RIGHT = 2
M_WHEEL_UP = 4
M_WHEEL_DOWN = 5

#Represents the Keyboard and Mouse enums
KEYBOARD = 0
MOUSE = 1

class KeyState(object):
    """Represents the state of keyboard keys"""
    
    def __init__(self):
        """Initialise the state"""
        self.key_states = []

    def getCopy(self):
        """Return a new copy of the key states"""
        new_keys = []
        for key in self.key_states:
            new_keys.append(key)
        state_cpy = KeyState()
        state_cpy.key_states = new_keys
        return state_cpy

    def getState(self, key):
        """Return the state of a specific key"""
        try:
            return self.key_states[key]
        except IndexError:
            return None



class Keyboard(common.Loggable):
    """Represents the state of the keyboard"""
    
    def __init__(self):
        """Initialise the keyboard"""
        super(Keyboard, self).__init__()
        self.current_state = KeyState()
        self.previous_state = KeyState()
        self.current_state.key_states = pygame.key.get_pressed()

    def isDown(self, key):
        return self.current_state.getState(key)

    def isUp(self, key):
        return not self.current_state.getState(key)

    def isClicked(self, key):
        return self.previous_state.getState(key) and (not self.current_state.getState(key))

    def areAnyDown(self):
        """Is any button depressed?"""
        for key in range(len(self.current_state.key_states)):
            if self.isDown(key):
                return True
        return False

    def areAnyClicked(self):
        """Is any button clicked?"""
        for key in range(len(self.current_state.key_states)):
            if self.isClicked(key):
                return True
        return False

    def update(self, interval):
        keys = pygame.key.get_pressed()
        self.previous_state = self.current_state.getCopy()
        self.current_state.key_states = keys

    
class MouseState(object):
    """A structure that contains the states of our mouse buttons."""
    def __init__(self):
        #Stores the pressed value of the left mouse button.
        self.left_pressed = False

        #Stores the pressed value of the middle mouse button.
        self.middle_pressed = False

        #Stores the pressed value of the right mouse button.
        self.right_pressed = False

        #Stores the pressed value of the wheel up button.
        self.wheel_up_pressed = False

        #Stores the pressed value of the wheel down button.
        self.wheel_down_pressed = False

        #The location of the mouse pointer on the screen.
        self.mouse_pos = pymunk.Vec2d()

    def getCopy(self):
        """Return a copy of this state"""
        ms = MouseState()
        ms.left_pressed = self.left_pressed
        ms.middle_pressed = self.middle_pressed
        ms.right_pressed = self.right_pressed
        ms.wheel_up_pressed = self.wheel_up_pressed
        ms.wheel_down_pressed = self.wheel_down_pressed
        ms.mouse_pos = self.mouse_pos
        return ms

    def getState(self, StateType):
        """Return True if the specified button is pressed"""
        if(StateType == M_LEFT):
            #Checking left mouse button
            return self.left_pressed
        elif(StateType == M_MIDDLE):
            #Checking middle mouse button
            return self.middle_pressed
        elif(StateType == M_RIGHT):
            #Checking right mouse button
            return self.right_pressed
        elif(StateType == M_WHEEL_UP):
            #Checking wheel up mouse button
            return self.wheel_up_pressed
        elif(StateType == M_WHEEL_DOWN):
            #Checking wheel down mouse button
            return self.wheel_down_pressed
        
    def setState(self, StateType, state):
        """Set the state of a specific key"""
        if(StateType == M_LEFT):
            #Checking left mouse button
            self.left_pressed = state
        elif(StateType == M_MIDDLE):
            #Checking middle mouse button
            self.middle_pressed = state
        elif(StateType == M_RIGHT):
            #Checking right mouse button
            self.right_pressed = state
        elif(StateType == M_WHEEL_UP):
            #Checking wheel up mouse button
            self.wheel_up_pressed = state
        elif(StateType == M_WHEEL_DOWN):
            #Checking wheel down mouse button
            self.wheel_down_pressed = state
        
        
class Mouse(object):
    """Represents the state of the mouse"""
    
    def __init__(self, engine):
        """Initialise the mouse"""
        super(Mouse, self).__init__()
        self.current_mouse_state = MouseState()
        self.previous_mouse_state = MouseState()
        self.engine = engine

    def isDown(self, MouseStateType):
        """Return True if the mouse button is down"""
        return self.current_mouse_state.getState(MouseStateType)

    def isUp(self, MouseStateType):
        """Return True if the mouse button is up"""
        return not self.current_mouse_state.getState(MouseStateType)

    def isClicked(self, MouseStateType):
        """Return True if the mouse button is pressed"""
        return self.previous_mouse_state.getState(MouseStateType) and (not self.current_mouse_state.getState(MouseStateType))

    def update(self, interval):
        #Update our mouse states.
        self.previous_mouse_state = self.current_mouse_state.getCopy()

        #Get the mouse buttons currently down.
        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
        self.current_mouse_state.left_pressed = mouse1
        self.current_mouse_state.middle_pressed = mouse2
        self.current_mouse_state.right_pressed = mouse3
        self.current_mouse_state.mouse_pos = pygame.mouse.get_pos

    def getScreenPos(self):
        """Return the pixel location relative to the screen and camera"""
        absolute = pymunk.Vec2d(*pygame.mouse.get_pos())/self.engine.getRenderer().getCamera().zoom
        x, y, _, _ = self.engine.getRenderer().getCamera().getSpatial()
        return absolute+pymunk.Vec2d(x, y)

    def XXXget_screen_rel(self):
        """Return the pixel location relative to the screen center"""
        width, height = Ragnarok.get_world().get_backbuffer_size()
        pos = Vector2(*pygame.mouse.get_pos()) - Vector2(width/2, height/2)
        return pos
        
    def getActorEvents(self, world, layers=None):
        """Return the type of events for each actor that we have hit
        
        The optional parameter layers can be a list of layers that we are interested in. Only
        actors on the given layers will be returned.
        
        """
        x, y = self.getScreenPos()
        actors = world.findActorsAt(x, y)
        #
        # Get list of applying events
        events = []
        if self.isClicked(M_LEFT):
            events.append('left-click')
        elif self.isDown(M_LEFT):
            events.append('left-mouse-down')
        #
        if self.isClicked(M_RIGHT):
            events.append('right-click')
        elif self.isDown(M_RIGHT):
            events.append('right-mouse-down')
        #
        all = []
        for actor in actors:
            if layers is None or actor.layer in layers:
                for event in events:
                    all.append((event, actor))
        return all

