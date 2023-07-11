set terminal pdfcairo color dashed enhanced font "Times,25" fontscale 0.4 size 12,3 lw 2
set out "fig5.pdf"
set multiplot
set border lw 2


set lmargin screen 0.06
set rmargin screen 0.31
set tmargin screen 0.94
set bmargin screen 0.30
set xlabel "{/=30 {λ_{nk, mk+q}}}" offset 0, 0.5
set tics font ",30"
set xtics 1
set ytics 5
set mxtics 5
set key font ",20"
set xrange [0:4]
set yrange [0:1.2]
set label 1 "ρ(λ_{nk, mk+q})" font ",30"
set label 1 at graph 0.2, 0.7
plot "mgb2.lambda_pairs" w l lw 2 lt 1 lc rgb "black" notitle

reset
set border lw 2

set lmargin screen 0.39
set rmargin screen 0.64
set tmargin screen 0.94
set bmargin screen 0.30
set xlabel "{/=30 {λ_{nk}}}" offset 0, 0.5
set tics font ",30"
set xtics 0.5
set ytics 5
set mxtics 5
set key font ",20"
set xrange [0:1.6]
set yrange [0:1.2]
set label 1 "ρ(λ_{nk})" font ",30"
set label 1 at graph 0.3, 0.7
plot "mgb2.lambda_k_pairs" w l lw 2 lt 1 lc rgb "black" notitle

reset
set border lw 2

set lmargin screen 0.72
set rmargin screen 0.97
set tmargin screen 0.94
set bmargin screen 0.30
set xlabel "{/=30 {ω (meV)}}" offset 0, 0.5
set tics font ",30"
set xtics 20
set ytics 1
set mxtics 4
set mytics 5
set key font ",25"
set xrange [0:100]
set yrange [0:2]
set key at graph 0.4, 0.9
plot "< tail -n +2  mgb2.a2f | head -n 500"  w l lw 2 lt 1 lc rgb "black" title "α^2F(ω)", \
     "" u ($1):($12) w l lw 4 lt 1 lc rgb "red" title "λ"

unset multiplot
reset