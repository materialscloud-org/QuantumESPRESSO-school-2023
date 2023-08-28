# Run the calculations in the following way:

* KI calculation on a regular 6x6x6 grid 

`./link_wann.sh`

`kcw.x -in kc.khi | tee kc.kho`

`gnuplot plot_bands.gnu`

* Interpolation using better localized WFs

 1) mv to the wannier_post folder
 
    cd wannier_post

 2) Wannier90 pre-processing

    wannier90.x -pp wann

 3) interface between PW and Wannier90
 
    pw2wannier90.x -in pw2wan.p2wi | tee pw2wan.p2wo

 4) Wannierization of the occupied manifold

    wannier90.x wann

 5) Plot the interpolated bands

    gnuplot plot_bands.gnu
