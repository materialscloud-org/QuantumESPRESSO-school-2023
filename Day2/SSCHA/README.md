# SSCHA Tutorial

In this tutorial we will:

- Generate a Fcc structure file (cif) for silver (Ag).
- Harmonic phonons using a EMT force-field with ASE.
- Anharmonic self-consistent phonons for silver.
- Relax the unit-cell at fixed temperature.
- Thermal expansion.


## Generation of the structure of Silver.


We use the Atomic Simulation Environment (ASE) to build the cell of silver (FCC).

Run the file `create_structure.py` to generate the cif file of the Ag.
This should be the same as `Ag.cif` provided. 

## Exercize 1. Compute harmonic phonons.


Harmonic phonons can be evaluated within DFPT as illustrated in the previous tutorial.
Here we employ a different approach:

$$
\Phi_{ab}  = -\frac{d f_a}{d R_b}
-F\
$$

where $f_a$ is the force along the $a$ direction (encoding both the atom index and the Cartesian coordinate),
while $R_b$ is the position of the $b$ coordinate (encoding both the atom index and component). 

Exploiting symmetries, we can reduce the number of independent displacements to be evaluated.
In the case of Fcc lattice (Fm$\bar 3$m symmetry group), we have only 1 independent displacement.

We use cellconstructor to perform this calculation:

```
import cellconstructor as CC, cellconstructor.Phonons

# Initialize the cellconstructor atomic structure
struct = CC.Structure.Structure()
struct.read_generic_file("Ag.cif")

ag_harmonic = CC.Phonons.compute_phonons_finite_displacements(
    struct,
    EMT(), 
    supercell=(4,4,4))
```

The function ``compute_phonons_finite_displacements`` takes as input the structure,
the ASE calculator (to compute the force on the structure), and the supercell on which 
to evaluate the dynamical matrix. The supercell is equivalent to the phonon q-mesh
employed in a DFPT calculation.

To impose the symmetries and the acoustic sum rule:

```
ag_harmonic.Symmetrize()
```

To save the dynamical matrix in quantum espresso format:

```
ag_harmonic.save_qe("AgDyn")
```

You find the complete script in `scripts/compute_harmonic_phonons.py`.

As in the quantum espresso format, the dynamical matrix generates many files (13 in this case), each one encoding the dynamical 
matrix of a separate star of q-points. The total number of q-points matches with the q-mesh (4x4x4 = 64), but only 13 of these are independent by symmetry.
