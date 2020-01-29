#!/usr/bin/env python

import mmap
import sys
import os
from multiprocessing import Pool, Lock, Value
import multiprocessing
import ctypes

def print_usage():
    SCRIPTNAME=os.path.basename(__file__)
    print("Usage: %s search_pattern filename use_no_threads" % (SCRIPTNAME))
    sys.exit(1)

# FILENAME,SKIP,CHUNK,SEARCH
def searchfile(file_name, start, size, search, RESULT, lock):
    chunk=10*1024*1024
    readed=0
    with open(file_name) as f:
        print "seek %s start %s size %s" % (start,start,size)
        f.seek(start)
        while readed <= size:
            lines = f.read(chunk).splitlines()
            readed=readed+chunk
            for line in lines:
                if search in line:
                    #lock.acquire()
                    with lock:
                        RESULT.value += 1
                        print "Find %d" % (RESULT.value)
                    #lock.release()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_usage()

    FILENAME=sys.argv[2]
    SEARCH=sys.argv[1]
    CORES=sys.argv[3]
    SIZE_BYTES=os.path.getsize(FILENAME)
    RESULT = Value('i', 0)
    print "Search file %s for string %s, use %s cores, file size: %s" % (FILENAME, SEARCH, CORES, SIZE_BYTES)

    pool = Pool(int(CORES))
    jobs = []
    manager = multiprocessing.Manager()
    counter = manager.Value(ctypes.c_ulonglong, 0)
    counter_lock = manager.Lock()  # pylint: disable=no-member

    # open file
    #CHUNK=int(100*1024*1024)
    CHUNK=int(int(SIZE_BYTES)/int(CORES))
    SKIP=int(0)

    while SKIP <= SIZE_BYTES:
        print("job SKIP %d CHUNK %d" % (SKIP, CHUNK))
        jobs.append( pool.apply_async(searchfile, (FILENAME,SKIP,CHUNK,SEARCH,counter,counter_lock)) )
        SKIP=SKIP+CHUNK+1

    for job in jobs:
        job.get()

    pool.close()

    print("Search result: %d" % (counter.value))


