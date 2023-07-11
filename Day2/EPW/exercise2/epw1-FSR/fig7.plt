set terminal pdfcairo color dashed enhanced font "Times,25" fontscale 0.4 size 8,3 lw 2
set out "fig7.pdf"
set multiplot
set border lw 2


set lmargin screen 0.09
set rmargin screen 0.48
set tmargin screen 0.94
set bmargin screen 0.20
set ylabel "{/=30 {Δ_{nk} (meV)}" offset 1, 0
set xlabel "{/=30 {iω (meV)}}" offset 0, 0.5
set tics font ",25"
set xtics 40
set ytics 3
set mxtics 2
set mytics 3
set key font ",20"
set xrange [0:180]
set yrange [-2:15]
plot "mgb2.imag_aniso_010.00" u ($1*1000):($4*1000) with points pt 7 ps 0.2 lt 1 lc rgb "black" notitle

reset
set border lw 2

set lmargin screen 0.59
set rmargin screen 0.98
set tmargin screen 0.94
set bmargin screen 0.20
set ylabel "{/=30 {Δ_{nk} (meV)}" offset 1, 0
set xlabel "{/=30 {ω (meV)}}" offset 0, 0.5
set tics font ",25"
set xtics 40
set ytics 10
set mxtics 2
set mytics 2
set key font ",20"
set xrange [0:180]
set yrange [-20:45]
set label 1 "ReΔ - Pade approx." font ",20"
set label 1 at graph 0.6, 0.9
plot "mgb2.pade_aniso_010.00" u ($1*1000):($5*1000) with points pt 7 ps 0.1 lt 1 lc rgb "black" notitle

unset multiplot
reset