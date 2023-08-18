set terminal post eps enhanced solid color "Helvetica" 20
set output "phonon_dispersion.eps"
set xrange [0:3.7802]
set yrange [0:430]
set arrow from 1.0607,0. to 1.0607,430 nohead  lw 3
set arrow from 1.4142,0. to 1.4142,430 nohead  lw 3
set arrow from 1.9142,0. to 1.9142,430 nohead  lw 3
set arrow from 2.9142,0. to 2.9142,430 nohead  lw 3
set arrow from 3.7802,0. to 3.7802,430 nohead  lw 3
set ylabel "{/Symbol w} (cm^{-1})"
unset xtics
set label "{/Symbol G}" at -0.05,-15
set label "K" at 1.0607,-15
set label "W" at 1.4142,-15
set label "X" at 1.9142,-15
set label "{/Symbol G}" at 2.9142,-15
set label "L" at 3.7802-15

plot "freq.plot" u 1:2 w l lw 4 title 'q-grid: 4x4x4'

