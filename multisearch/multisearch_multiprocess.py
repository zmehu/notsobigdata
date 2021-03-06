#!/usr/bin/env python

import mmap
import sys
import os
from multiprocessing import Pool, Lock

lock = Lock()

def print_usage():
    SCRIPTNAME=os.path.basename(__file__)
    print("Usage: %s search_pattern filename use_no_threads" % (SCRIPTNAME))
    sys.exit(1)

def searchfile(file_name, start, size, search):
    global RESULT
    with open(file_name) as f:
        f.seek(start)
        lines = f.read(size).splitlines()
        for line in lines:
            if search in line:
                lock.acquire()
                RESULT=RESULT+1
                print "Find %d" % (RESULT)
                lock.release()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_usage()

    FILENAME=sys.argv[2]
    SEARCH=sys.argv[1]
    CORES=sys.argv[3]
    SIZE_BYTES=os.path.getsize(FILENAME)
    global RESULT
    RESULT=0
    print "Search file %s for string %s, use %s cores, file size: %s" % (FILENAME, SEARCH, CORES, SIZE_BYTES)

    pool = Pool(int(CORES))
    jobs = []

    # open file
    CHUNK=int(100*1024*1024)
    SKIP=int(0)

    while SKIP <= SIZE_BYTES:
        #print("job SKIP %d CHUNK %d" % (SKIP, CHUNK))
        jobs.append( pool.apply_async(searchfile, (FILENAME,SKIP,CHUNK,SEARCH)) )
        SKIP=SKIP+CHUNK

    for job in jobs:
        job.get()

    pool.close()

    print("Search result: %d" % (RESULT))


