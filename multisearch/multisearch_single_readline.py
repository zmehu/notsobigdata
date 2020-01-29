#!/usr/bin/env python

import mmap
import sys
import os

def print_usage():
    SCRIPTNAME=os.path.basename(__file__)
    print("Usage: %s search_pattern filename" % (SCRIPTNAME))
    sys.exit(1)

def read_in_chunks(file_object, chunk_size=1024*1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def searchall(l):
    global RESULT
    if SEARCH in l:
        RESULT=RESULT+1
        print "Find %d" % (RESULT)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()

    FILENAME=sys.argv[2]
    SEARCH=sys.argv[1]
    global RESULT
    RESULT=0
    print "Search file %s for string %s" % (FILENAME, SEARCH)

    # open file
    f = open(FILENAME)
    for l in read_in_chunks(f):
        searchall(l)

    print("Search result: %d" % (RESULT))

