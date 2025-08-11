#!/bin/bash
uname -m


cd pin/source/tools/approx
# ls
# make obj-intel64/bucketbitflip.so TARGET=intel64


../../../pin -t obj-intel64/bucketbitflip.so -- ../../../../perfect/suite/pa1/kernels/ser/2d_convolution/2d_convolution \
  0 0 1 2dconv_meminfo.out 0

python3 error_script.py 2dconv_output.small.0.mat.0.0 ../../../../perfect/suite/pa1/output/2dconv_output.small.mat


echo "done"
