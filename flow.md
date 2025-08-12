# note: before your run
- change line 33 in csv_concact.sub
# TODO:
1. ``git clone https://github.com/zhewen404/axolotl.git``
2. ``cd axolotl``
3. ``git clone https://github.com/eys29/perfect.git``
4. ``git clone https://github.com/zhewen404/pin.git``
5. ``./run_benchmark_seed.sh 5 100 debayer`` 
    - 5: random seed of error injection (zhewen's running 0-4, elise can run 5-9);
    - 100: 100 cpus per taks; 
    - debayer: benchmark name \{2dconv, histeq, dwt53, debayer\}
6. ``./run_benchmark_seed.sh 6 50 debayer # run a different random seed``
7. ``./run_benchmark_seed.sh 7 50 debayer # run a different random seed``
8. ``./run_benchmark_seed.sh 8 50 debayer # run a different random seed``
9. ``./run_benchmark_seed.sh 9 50 debayer # run a different random seed``
10. ``ls csv_debayer # check that it should contain x{1-16}-z{5-9}.csv; we can keep all these csvs since they are raw data, we can do any form of aggregation (gmean/amean/max/min) across z that makes sense in the next step``
11. TODO: script to aggregate across 10 (z0-z9) runs; if 10 is too many, we can do 5 runs (z0-z4)
