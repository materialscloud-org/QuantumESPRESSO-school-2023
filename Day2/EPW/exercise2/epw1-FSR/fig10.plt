set terminal pdfcairo color dashed enhanced font "Times,25" fontscale 0.4 size 4,3 lw 2
set ylabel "{/=30 {N_s(ω)/N_F}"
set xlabel "{/=30 {ω (meV)}}"
set lmargin screen 0.18
set rmargin screen 0.96
set tmargin screen 0.94
set bmargin screen 0.20
set tics font ",30"
set xtics 3
set ytics 1
set mxtics 3
set mytics 5
set key font ",20"
set xrange [0:15]
set yrange [0:2.2]
set out "fig10.pdf"
set key at graph 0.9, 0.9
NF=0.324589885287221           # DOS in the normal state
plot "mgb2.qdos_010.00" u ($1*1000):($2/NF) w l lw 2 lt 1 lc rgb "black" notitle
reset