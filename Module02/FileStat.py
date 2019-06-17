import os, time
from stat import *

def state(Fname):
    print "\n\n------ File Information ------"
    file_size = os.stat(Fname).st_size
    uid = os.stat(Fname).st_uid
    gid = os.stat(Fname).st_gid
    absPath = os.path.realpath(Fname)
    mtime = time.ctime(os.path.getmtime(Fname))
    created = time.ctime(os.path.getctime(Fname))
    accessTime = time.ctime(os.stat(Fname).st_atime)

    print "File size: " + str(file_size) + " bytes"
    print "UID of owner: " + str(uid)
    print "GID of owner: " + str(gid)
    print "Absolute Path: " + absPath
    print "Last modified: " + str(mtime)
    print "Created: " + str(created)
    print "Last access: " + str(accessTime)

filename = raw_input("Enter filename: ")
state(filename)
