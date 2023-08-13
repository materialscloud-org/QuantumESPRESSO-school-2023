import ase
from ase import Atoms
from ase.calculators.emt import EMT
import ase.io
import cellconstructor as CC, cellconstructor.Phonons
import spglib

# Initialize the cellconstructor atomic structure
struct = CC.Structure.Structure()
struct.read_generic_file("Ag.cif")

ag_harmonic = CC.Phonons.compute_phonons_finite_displacements(struct,
        EMT(), supercell=(4,4,4))
ag_harmonic.Symmetrize()
ag_harmonic.save_qe("AgDyn")
