#!/usr/bin/env bash
set -euo pipefail

# check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
  echo "Usage: $0 X Z NUMCHUNK BENCHMARK"
  echo "Example: $0 2 0 100 2dconv"
  exit 1
fi

# Usage: ./run_dag.sh X Z NUMCHUNK BENCHMARK   (e.g., ./run_dag.sh 2 0 100 2dconv)
X="${1:?X}"; Z="${2:?Z}"; NUMCHUNK="${3:?NUMCHUNK}"; BENCHMARK="${4:?BENCHMARK}"

DAG="${BENCHMARK}-x${X}-z${Z}-c${NUMCHUNK}.dag"

cat > "$DAG" <<EOF
JOB BATCH run_y_all.sub
VARS BATCH X="${X}" Z="${Z}" NUMCHUNK="${NUMCHUNK}" BENCHMARK="${BENCHMARK}"

JOB CONCAT csv_concat.sub
VARS CONCAT X="${X}" Z="${Z}" NUMCHUNK="${NUMCHUNK}" BENCHMARK="${BENCHMARK}"

PARENT BATCH CHILD CONCAT
EOF

condor_submit_dag -f "$DAG"
