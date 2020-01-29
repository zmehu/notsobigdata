#!/usr/bin/env python

import mmap
import sys
import os

def print_usage():
    SCRIPTNAME=os.path.basename(__file__)
    print("Usage: %s search_pattern filename" % (SCRIPTNAME))
    sys.exit(1)

def searchall(s, d, offset=0):
    return d.find(s,offset)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()

    FILENAME=sys.argv[2]
    SEARCH=sys.argv[1]
    RESULT=0
    print "Search file %s for string %s" % (FILENAME, SEARCH)

    # open file
    with open(FILENAME) as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        start=0
        while True:
            A=searchall(SEARCH, s, start)
            if A == -1:
                break
            if A != -1:
                print A
                start=start+A+1
                RESULT=RESULT+1

    print("Search result: %d" % (RESULT))

