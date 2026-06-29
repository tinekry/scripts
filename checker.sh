#!/bin/bash

# compile
g++ a.cpp -o a.out || { echo "compile error in a.cpp"; exit 1; }
g++ b.cpp -o b.out || { echo "compile error in b.cpp"; exit 1; }

# input in.txt & output
./a.out < in.txt > out_a.txt || { echo "run error in a.out"; exit 1; }
./b.out < in.txt > out_b.txt || { echo "run error in b.out"; exit 1; }

# output comparison
if ! diff -q -wB out_a.txt out_b.txt > /dev/null; then
    echo "Outputs are different!"
    diff out_a.txt out_b.txt
    exit 1
else
    echo "Outputs match."
fi
