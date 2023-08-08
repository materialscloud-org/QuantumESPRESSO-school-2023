# PURPOSE OF THE EXERCISE:
## How to calculate the phonon frequencies of the polar semiconductor AlAs at the Gamma point.
------------------------------------------------------------------------

### Steps to perform:

1. Run the SCF ground-state calculation

        `mpirun -np 2 pw.x -i  AlAs.scf.in > AlAs.scf.out`

2. Run the phonon calculation at Gamma

        `mpirun -np 2 ph.x < AlAs.phG.in > AlAs.phG.out`

3. Impose the acoustic sum rule for the Zone Center  modes and compute the dielectric tensor 
        
        `dynmat.x -i AlAs.dynmat.in > AlAs.dynmat.log` 

4. Add the non-analytic and compute the LO-TO splitting for the long wave limit

        mpirun -np 4 dynmat.x < AlAs.dynmat-LO-TO.in > AlAs.dynmatLOTO.log
