#!/bin/bash
while getopts "b:x:z:c:d:" opt; do
  case $opt in
    b) BENCHMARK=$OPTARG ;;
    x) X=$OPTARG ;;
    z) Z=$OPTARG ;;
    c) NUMCHUNK=$OPTARG ;;
    d) CHUNKID=$OPTARG ;;
    *) echo "Usage: $0 [-b value] [-x value] [-z value] [-c value] [-d value]..." >&2
       exit 1 ;;
  esac
done

cd pin/source/tools/approx
# uname -m
# make obj-intel64/bucketbitflip.so TARGET=intel64

python3 run_all_y.py \
    --benchmark ${BENCHMARK} \
    --outputfile_id x${X}-z${Z}-yc${CHUNKID}-${NUMCHUNK} \
    --num_bitflip ${X} \
    --rand_seed ${Z} \
    --ychunk_total_num ${NUMCHUNK} \
    --ychunk_id ${CHUNKID}


ls ${BENCHMARK}-x${X}-z${Z}-yc${CHUNKID}-${NUMCHUNK}.csv

echo "done"
