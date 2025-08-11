1. git clone https://github.com/zhewen404/axolotl.git
2. cd axolotl
3. git clone https://github.com/eys29/perfect.git
4. git clone https://github.com/zhewen404/pin.git
5. ./run_benchmark_seed.sh 0 50 debayer # 0: random seed of error injection; 50: 50 cpus per taks; 2dconv: benchmark name
6. ./run_benchmark_seed.sh 1 50 debayer # run a different random seed
7. ./run_benchmark_seed.sh 2 50 debayer # run a different random seed
8. ./run_benchmark_seed.sh 3 50 debayer # run a different random seed
9. ./run_benchmark_seed.sh 4 50 debayer # run a different random seed
10. ls csv_debayer dir # check that it should contain x[1-16]-z[0-4].csv; if we have time, we can run z[5-9] too
11. TODO: aggregate across 5 (z0-z4) runs