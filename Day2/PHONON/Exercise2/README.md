# PURPOSE OF THE EXERCISE:
## How to calculate the phonon dispersion and VDOS of  the polar semiconductor AlAs
------------------------------------------------------------------------

### Steps to perform:

1. Run the SCF ground-state calculation

        `mpirun -np 2 pw.x < AlAs.scf.in > AlAs.scf.out`

2. Run the phonon calculation on a uniform grid of q-points

        `mpirun -np 2  ph.x < AlAs.ph.in > AlAs.ph.out`

3. Compute the Interatomic Force Constants using q2r.x  

        `q2r.x < AlAs.q2r.in > AlAs.q2r.out`

4. Use the IFC to compute the dynamical matrices at generic `q` points:

    4.1 Compute the phonon dispersion along high symmetry directions of the BZ:

        `matdyn.x < AlAs.matdyn.in > AlAs.matdyn.out`

    4.2 Compute the phonon energies on a denser k point mesh and compute the vibrational density of states. 

5. Plot the phonon dispersion and VDOS of AlAs

    5.1 Use plotband to extract information needed for the plot: 

        `plotband.x < plotband.AlAs.in > plotband.AlAs.out`

    5.2  Example1 gnuplot script for plotting phonon dispersion:

        gnuplot plot_dispersion.gp
        evince  phonon_dispersion.eps 

    5.3 Example2 python script for plotting the dispersion and the VDOS with matplotlib
   
