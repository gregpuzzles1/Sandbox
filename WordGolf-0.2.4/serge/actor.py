"""The actor class"""

import pygame
import math

import common
import serialize
import geometry
import visual 
import events

class InvalidActor(Exception): """The actor supplied was not valid for the operation"""


class Actor(common.Loggable, geometry.Rectangle, common.EventAware):
    """Represents an actor"""
    
    my_properties = (
        serialize.S('tag', 'actor', 'the actor\'s tag'),
        serialize.S('name', '', 'the actor\'s name'),
        serialize.B('active', True, 'whether the actor is active'),
        serialize.S('sprite', '', 'the name of our sprite'),
        serialize.S('layer', '', 'the name of the layer we render to'),
        serialize.O('physical_conditions', '', 'the physical conditions for this object'),
        serialize.F('angle', 0.0, 'the angle for the actor'),
    )
    
    def __init__(self, tag, name=''):
        """Initialise the actor"""
        self.addLogger()
        self.initEvents()
        super(Actor, self).__init__()
        # Whether we respond to updates or not
        self.active = True        
        # Class based tag to locate the actor by
        self.tag = tag
        # Unique name to locate by
        self.name = name
        # Our sprite
        self.sprite = ''
        self._visual = None
        # The layer we render to
        self.layer = ''    
        # Our zoom factor
        self.zoom = 1.0
        # Physics parameters - None means no physics
        self.physical_conditions = None
        # Angle
        self.angle = 0.0
        
    def init(self):
        """Initialize from serialized form"""
        self.addLogger()
        self.initEvents()
        self.log.info('Initializing actor %s:%s:%s' % (self, self.tag, self.name))
        super(Actor, self).init()
        if self.sprite:
            self.setSpriteName(self.sprite)
        else:
            self._visual = None
        self.setLayerName(self.layer)
        self.zoom = 1.0

    def getNiceName(self):
        """Return a nice name for this actor"""
        if self.name:
            name_part = '%s (%s)' % (self.name, self.tag)
        else:
            name_part = self.tag
        return '%s [%s] <%s>' % (self.__class__.__name__, name_part, id(self))
        
    def setSpriteName(self, name):
        """Set the sprite for this actor"""
        self.visual = visual.Register.getItem(name).getCopy()
        self.sprite = name
        
    @property
    def visual(self): return self._visual
    @visual.setter
    def visual(self, value):
        """Set the visual item for this actor"""
        self._visual = value
        self._resetVisual()
        
    def _resetVisual(self):
        """Reset the visual item on the center point"""
        #
        # Adjust our location so that we are positioned and sized appropriately
        cx, cy, _, _ = self.getSpatialCentered()
        self.setSpatialCentered(cx, cy, self._visual.width, self._visual.height)
        #
        # Here is a hack - sometimes the visual width changes and we want to update our width
        # so we let the visual know about us so it can update our width. This is almost 
        # certainly the wrong thing to do, but we have some tests in there so hopefully
        # the right thing becomes obvious later!
        self._visual._actor_parent = self
        
    def getSpriteName(self):
        """Return our sprite"""
        return self.sprite
        
    def setAsText(self, text_object):
        """Set some text as our visual"""
        self.visual = text_object

    def setText(self, text):
        """Set the actual text"""
        self._visual.setText(text)
        
    def setLayerName(self, name):
        """Set the layer that we render to"""
        self.layer = name
    
    def getLayerName(self):
        """Return our layer name"""
        return self.layer
    
    def renderTo(self, renderer, interval):
        """Render ourself to the given renderer"""
        if self._visual:
            coords = renderer.camera.getRelativeLocation(self)
            if self.layer:
                self._visual.renderTo(interval, renderer.getLayer(self.layer).getSurface(), coords)
    
    def updateActor(self, interval, world):
        """Update the actor status"""

    def removedFromWorld(self, world):
        """Called when we are being removed from the world"""
        self.processEvent((events.E_REMOVED_FROM_WORLD, self))

    def addedToWorld(self, world):
        """Called when we are being added to the world"""
        self.processEvent((events.E_ADDED_TO_WORLD, self))
        
    def setZoom(self, zoom):
        """Zoom in on this actor"""
        if self._visual:
            self._visual.scaleBy(zoom/self.zoom)
        self.zoom = zoom

    def setAngle(self, angle, sync_physical=False):
        """Set the angle for the visual"""
        if self._visual:
            self._visual.setAngle(angle)
            self._resetVisual()
        if sync_physical and self.physical_conditions:
            self.physical_conditions.body.angle = math.radians(-angle)
        self.angle = angle
        
    def getAngle(self):
        """Return the angle for the actor"""
        return self.angle
    

    ### Physics ###
    
    def setPhysical(self, physical_conditions):
        """Set the physical conditions"""
        #
        # Watch for if this object already has a shape
        if self.physical_conditions and self.physical_conditions.body:
            self.physical_conditions.updateFrom(physical_conditions)
        else:
            self.physical_conditions = physical_conditions
        
    def getPhysical(self):
        """Return the physical conditions"""
        return self.physical_conditions

    def syncPhysics(self, spatial_only=False):
        """Sync physics when the actors physical properties have been changed"""
        if self.physical_conditions:
            #self.log.debug('Syncing physics for %s to %s, %s' % (self.getNiceName(), self.x, self.y))
            self.physical_conditions.shape.body.position = self.x, self.y
            if not spatial_only:
                self.physical_conditions.shape.body.velocity = self.physical_conditions.velocity

    # Remap x, y properties to allow syncing with the physics engine

    def move(self, x, y):
        """Move by a certain amount"""
        super(Actor, self).move(x, y)
        self.syncPhysics(spatial_only=True)
        
    def moveTo(self, x, y, no_sync=False):
        """Move to a certain place"""
        super(Actor, self).moveTo(x, y)
        if not no_sync:
            self.syncPhysics(spatial_only=True)
          
          
class CompositeActor(Actor):
    """An actor that can have children, which are also actors
    
    World operations on the parent, like adding and removing,
    will also apply to the children.
    
    If the children are removed from the parent then they are
    also removed from the world.
    
    """
    
    my_properties = (
        serialize.L('children', [], 'the child actors that we own'),
        serialize.L('_world', [], 'the world that we belong to'),
    )
    
    def __init__(self, *args, **kw):
        """Initialise the actor"""
        super(CompositeActor, self).__init__(*args, **kw)
        self.children = []
        self._world = None

    ### World events ###
    
    def removedFromWorld(self, world):
        """Called when we are being removed from the world"""
        super(CompositeActor, self).removedFromWorld(world)
        for child in self.getChildren()[:]:
            world.removeActor(child)
        self._world = None
        
    def addedToWorld(self, world):
        """Called when we are being added to the world"""
        super(CompositeActor, self).addedToWorld(world)
        for child in self.getChildren():
            world.addActor(child)
        self._world = world
            
    ### Children ###
            
    def addChild(self, actor):
        """Add a child actor"""
        self.children.append(actor)
        actor.linkEvent(events.E_REMOVED_FROM_WORLD, self._childRemoved)
        
    def removeChild(self, actor):
        """Remove a child actor"""
        try:
            self.children.remove(actor)
        except ValueError:
            raise InvalidActor('The actor %s was not a child of %s' % (actor.getNiceName(), self.getNiceName()))
        #
        # Remove the child from the world
        if self._world:
            self._world.removeActor(actor)
            
    def getChildren(self):
        """Return the list of children"""
        return self.children
    
    def _childRemoved(self, child, arg):
        """A child was removed from the world"""
        if child in self.children:
            self.children.remove(child)
        
