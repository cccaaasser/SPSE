#!/usr/bin/env python

import thread
import time

def worker_thread(id):
    print "Thread ID %d now alive"%id

    counter = 1

    while True:
        print "Thread with ID %d has counter value %d"%(id, counter)
        time.sleep(2)
        counter += 1

for i in range(5):
    thread.start_new_thread(worker_thread,(i,))

print "Main thread going for a infinite wait loop."
while True:
    pass
