# Run the calculations in the following way:

pw.x < Si.scf.in | tee Si.scf.out

pw.x < Si.bands.in | tee Si.bands.out

bands.x < bands.in | tee bands.out

gnuplot plot_bands.gnu 


## For projected band structure:

projwfc.x < Si.projwfc.in | tee Si.projwfc.out

cp si_bands_pbe.projwfc_up si_bands_pbe.proj

plotband.x < plotband.in | tee plotband.out

gnuplot plot_bands_proj.gnu 

