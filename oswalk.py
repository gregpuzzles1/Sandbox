import os
from os.path import join, getsize

for root, dirs, files in os.walk('C:\Users\GREG\Dropbox\Sandbox\PythonChess_v0.7\PythonChess'):
                                print root, "consumes\n",
                                print "dirs = ", dirs
                                print "files = ", files
                                #print sum([getsize(join(root, name)) for name in files]),
                                #print "bytes in", len(files), "non-directory files"
    #if 'CVS' in dirs:
        #dirs.remove('CVS')  # don't visit CVS directories

