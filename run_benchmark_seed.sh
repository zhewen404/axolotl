#!/usr/bin/env bash

# check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 RANDSEED NUMCHUNK BENCHMARK"
  echo "Example: $0 0 50 2dconv"
  exit 1
fi

# same RANDSEED/NUMCHUNK/BENCHMARK, many Xs
RANDSEED="${1:?RANDSEED}"; NUMCHUNK="${2:?NUMCHUNK}"; BENCHMARK="${3:?BENCHMARK}"
for X in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do
  ./run_dag.sh "$X" "$RANDSEED" "$NUMCHUNK" "$BENCHMARK"
  sleep 10 # wait a bit before launching more jobs
done
