# Some scripts searching string in big file
You can take big file from https://archive.org/details/stackexchange

##
```
z@wspolnyxl:/mnt/big2/root/tmp/multisearch/ > ls -lh
total 8.4G
-rw-rw-r-- 1 z z 8.4G Sep 11  2018 StackOverflow2010.mdf
-rwxrw-r-- 1 z z  975 Jan 29 13:25 multisearch_dd.sh
-rwxrw-r-- 1 z z 1.4K Jan 29 17:52 multisearch_multiprocess.py
-rwxrw-r-- 1 z z 1.6K Jan 29 17:51 multisearch_multiprocess_2.py
-rwxrw-r-- 1 z z  846 Jan 29 14:48 multisearch_single_python2.py
-rwxrw-r-- 1 z z  842 Jan 29 15:23 multisearch_single_readline.py
```


##
```
z@wspolnyxl:/mnt/big2/root/tmp/multisearch/ > time grep -c OMG StackOverflow2010.mdf
2
grep --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn} -c OMG    49.59s  user 5.08s system 71% cpu 1:16.34 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                5 MB
page faults from disk:     0
other page faults:         140
```


##
```
z@wspolnyxl:/mnt/big2/root/tmp/multisearch/ > time ./multisearch_dd.sh OMG StackOverflow2010.mdf 4
Searching OMG in file StackOverflow2010.mdf
Size: 8980398080 Sectorsize: 4096 Size_bs: 2192480 Chunk_size: 548120
...
2
real    0m31.580s
user    0m12.564s
sys     0m4.463s
```


##
```
z@wspolnyxl:/mnt/big2/root/tmp/multisearch/ > time ./multisearch_single_python2.py OMG StackOverflow2010.mdf
Search file StackOverflow2010.mdf for string OMG
1334938524
8747160211
Search result: 2
./multisearch_single_python2.py OMG StackOverflow2010.mdf   13.50s  user 4.19s system 34% cpu 51.058 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                7154 MB
page faults from disk:     86
other page faults:         159703
```


##
```
z@wspolnyxl:/mnt/big2/root/tmp/multisearch/ > time ./multisearch_single_readline.py OMG StackOverflow2010.mdf
Search file StackOverflow2010.mdf for string OMG
Find 1
Find 2
Search result: 2
./multisearch_single_readline.py OMG StackOverflow2010.mdf   6.36s  user 6.65s system 32% cpu 40.300 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                7 MB
page faults from disk:     14
other page faults:         1891
```


##
```
z@wspolnyxl:/mnt/big2/root/tmp/multisearch/ > time ./multisearch_multiprocess.py OMG StackOverflow2010.mdf 4
Search file StackOverflow2010.mdf for string OMG, use 4 cores, file size: 8980398080
Find 1
Find 1
Search result: 0
./multisearch_multiprocess.py OMG StackOverflow2010.mdf 4   34.65s  user 23.10s system 106% cpu 54.033 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                292 MB
page faults from disk:     47
other page faults:         3660901
```


##
```
z@wspolnyxl:/mnt/big2/root/tmp/notsobigdata/multisearch/ > time ./multisearch_multiprocess_2.py OMG StackOverflow2010.mdf 4
Search file StackOverflow2010.mdf for string OMG, use 4 cores, file size: 8980398080
job SKIP 0 CHUNK 2245099520
job SKIP 2245099521 CHUNK 2245099520
job SKIP 4490199042 CHUNK 2245099520
job SKIP 6735298563 CHUNK 2245099520
seek 0 start 0 size 2245099520
seek 2245099521 start 2245099521 size 2245099520
seek 4490199042 start 4490199042 size 2245099520
seek 6735298563 start 6735298563 size 2245099520
Find 1
Find 2
Search result: 2
./multisearch_multiprocess_2.py OMG StackOverflow2010.mdf 4   38.63s  user 10.23s system 126% cpu 38.560 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                57 MB
page faults from disk:     4
other page faults:         192436
```


