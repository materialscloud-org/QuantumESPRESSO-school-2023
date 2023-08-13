#!/bin/bash

infile="README.md"
outfile="sscha_tutorial.pdf"

pandoc "$infile" \
	--highlight-style pygments.theme \
    --include-in-header header.tex \
    -V linkcolor:blue \
    -V geometry:a4paper \
    -V geometry:margin=2cm \
    -V mainfont="DejaVu Serif" \
    -V monofont="DejaVu Sans Mono" \
    --pdf-engine=xelatex \
    -o "$outfile"
