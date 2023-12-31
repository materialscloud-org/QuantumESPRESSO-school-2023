set terminal pngcairo enhanced solid color font "Helvetica, 24" size 1400,900 
set output "Si_dft_bands_proj.png" 

ymin=-13
ymax=8

set palette rgb 33,13,10
unset colorbox

set xrange [0: 3.7173]
set yrange [ ymin :  ymax]
set arrow from  0.8660,  ymin to  0.8660,   ymax nohead
set arrow from  1.8660,  ymin to  1.8660,   ymax nohead
set arrow from  2.6566,  ymin to  2.6566,   ymax nohead
set xtics ("L"  0.00000,"{/Symbol G}"  0.8660,"X"  1.8660,"K"  2.6566,"{/Symbol G}"  3.7173)
set ylab "E[eV]"
plot  'si_bands_proj_pbe.gnu' u 1:($2-6.2302):3 w l lw 4 palette notit

