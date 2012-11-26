## {{{ http://code.activestate.com/recipes/578277/ (r2)
import uuid
print ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
## end of http://code.activestate.com/recipes/578277/ }}}
