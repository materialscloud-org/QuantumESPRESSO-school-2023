set terminal pdfcairo color dashed enhanced font "Times,25" fontscale 0.4 size 4,3 lw 2
set ylabel "{/=30 {Δ_{nk} (meV)}" offset 1, 0
set xlabel "{/=30 {Temperature (K)}}" offset 0, 0.5
set lmargin screen 0.18
set rmargin screen 0.96
set tmargin screen 0.94
set bmargin screen 0.20
set tics font ",30"
set xtics 10
set ytics 3
set mxtics 5
set mytics 1
set key font ",20"
set xrange [0:60]
set yrange [0:15]
set out "fig9-FBW.pdf"
set key right top
scale=2
set style fill solid
set style fill noborder
set arrow  from 15, 0.0 to 15, 14 nohead
set arrow  from 20, 0.0 to 20, 14 nohead
set arrow  from 25, 0.0 to 25, 14 nohead
set arrow  from 30, 0.0 to 30, 13.5 nohead
set arrow  from 35, 0.0 to 35, 13 nohead
set arrow  from 40, 0.0 to 40, 12 nohead
set arrow  from 45, 0.0 to 45, 11 nohead
set arrow  from 50, 0.0 to 50,  9 nohead
set arrow  from 55, 0.0 to 55,  7 nohead
set label 1 "μ_c^*=0.05" font ",25"
set label 1 at graph 0.75, 0.9
#plot "mgb2.imag_aniso_gap0_015.00" u (($1-15)*scale/2 + 15):($2):(($1-15)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_020.00" u (($1-20)*scale/2 + 20):($2):(($1-20)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_025.00" u (($1-25)*scale/2 + 25):($2):(($1-25)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_030.00" u (($1-30)*scale/2 + 30):($2):(($1-30)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_035.00" u (($1-35)*scale/2 + 35):($2):(($1-35)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_040.00" u (($1-40)*scale/2 + 40):($2):(($1-40)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_045.00" u (($1-45)*scale/2 + 45):($2):(($1-45)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_050.00" u (($1-50)*scale/2 + 50):($2):(($1-50)*scale/2):(0.03) w boxxy lc 0 notitle, \
#     "mgb2.imag_aniso_gap0_055.00" u (($1-55)*scale/2 + 55):($2):(($1-55)*scale/2):(0.03) w boxxy lc 0 notitle
plot for [temp in "15 20 25 30 35 40 45 50 55"] gprintf('mgb2.imag_aniso_gap0_%06.2f',temp) u (($1-temp)*scale/2 + temp):($2-0.015):(($1-temp)*scale/2):(0.015) w boxxy lc 0 notitle
reset