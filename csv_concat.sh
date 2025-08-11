#!/bin/bash
while getopts "b:x:z:c:" opt; do
  case $opt in
    b) BENCHMARK=$OPTARG ;;
    x) X=$OPTARG ;;
    z) Z=$OPTARG ;;
    c) NUMCHUNK=$OPTARG ;;
    *) echo "Usage: $0 [-b value] [-x value] [-z value] [-c value]..." >&2
       exit 1 ;;
  esac
done

INPUT_DIR=${BENCHMARK}-x${X}-z${Z}-yc${NUMCHUNK}

python3 csv_concat.py \
    --benchmark ${BENCHMARK} \
    --num_bitflip ${X} \
    --rand_seed ${Z} \
    --ychunk_total_num ${NUMCHUNK} \
    --input_dir ${INPUT_DIR}


ls ${INPUT_DIR}/${BENCHMARK}-x${X}-z${Z}.csv

echo "done"
