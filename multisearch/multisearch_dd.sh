#!/bin/bash
# -----------------------------------------------------------
# Search file and count pattern in multiple jobs
#
# (C) 2020 Lukasz Sokolik, Poland
# Released under GNU Public License (GPL)
# email lukasz.sokolik@gmail.com
# -----------------------------------------------------------

usage () {
    echo "$0 pattern_search filename number_of_threads"
    exit 1
}

# Check arguments
[[ $# -ne 3 ]] && usage

FILENAME=$2
SEARCH=$1
THREADS=$3
SKIP=0

echo "Searching ${SEARCH} in file ${FILENAME}"

read SIZE SIZE_BS <<< `stat -c '%s %o' ${FILENAME}`
SIZE_INBS=$(( $SIZE / $SIZE_BS ))
CHUNK_SIZE=$(( $SIZE_INBS / $THREADS ))
echo "Size: ${SIZE} Sectorsize: ${SIZE_BS} Size_bs: ${SIZE_INBS} Chunk_size: ${CHUNK_SIZE}"


while [ $SKIP -le $SIZE_INBS ]; do
    echo "dd if=$FILENAME bs=$SIZE_BS count=$CHUNK_SIZE skip=$SKIP"
    time dd if="$FILENAME" bs="$SIZE_BS" count="$CHUNK_SIZE" skip="$SKIP" | grep -cE "${SEARCH}" &
    SKIP=$(( $SKIP + $CHUNK_SIZE ))
done


