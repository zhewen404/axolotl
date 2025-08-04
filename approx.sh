#!/bin/bash

#clone repos
git clone https://github.com/eys29/perfect.git
git clone https://github.com/eys29/pin.git
#perfect setup
cd perfect
git switch main -q
#pin setup
cd ../pin
git switch master -q
#run script
cd source/tools/approx
python3 run_every.py $1 
