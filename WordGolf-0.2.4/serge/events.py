"""Events that can occur

Use the constants rather than the text to avoid
breaking things in future releases.

"""


# Occurs when one object collides with another
E_COLLISION = 'collision'

# Mouse events related to the left mouse button
#  - down is when the button is held down (fires continuously)
#  - up is when the button is released
#  - click is the mouse was down and then released
E_LEFT_MOUSE_DOWN = 'left-mouse-down'
E_LEFT_MOUSE_UP = 'left-mouse-up'
E_LEFT_CLICK = 'left-click'

# Mouse events related to the right mouse button
#  - down is when the button is held down (fires continuously)
#  - up is when the button is released
#  - click is the mouse was down and then released
E_RIGHT_MOUSE_DOWN = 'right-mouse-down'
E_RIGHT_MOUSE_UP = 'right-mouse-up'
E_RIGHT_CLICK = 'right-click'

# Events related to actor and the world
E_ADDED_TO_WORLD = 'added-to-world'
E_REMOVED_FROM_WORLD = 'remove-from-world'

# Events related to the world
#
# The world is activated when it 
# becomes the current world for the engine.
# The previously activated world is deactivated.
#
# Before and after render are triggered relative
# to rendering the whole world
E_ACTIVATE_WORLD = 'activate-world'
E_DEACTIVATE_WORLD = 'deactivate-world'
E_BEFORE_RENDER = 'before-render'
E_AFTER_RENDER = 'after-render'


