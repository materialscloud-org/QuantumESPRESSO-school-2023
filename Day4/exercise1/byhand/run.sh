#!/bin/bash

sh clean.sh
echo "  init (DFT run)   ..."
cd init
sh run.sh
cd ../calc_alpha
echo "  calc alpha      ..."
sh run.sh
cd ../
cd final
echo "  KI final        ..."
sh run.sh
