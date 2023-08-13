import ase
from ase import Atoms
from ase.calculators.emt import EMT
import ase.io
import cellconstructor as CC, cellconstructor.Phonons
import spglib

# Generate the structure using ASE
a = 4.0  
b = a / 2
ag = Atoms('Ag',
           cell=[(0, b, b), (b, 0, b), (b, b, 0)],
           pbc=1,
           calculator=EMT())


ase.io.write('Ag.cif', ag)

print("Spacegroup: ", spglib.get_spacegroup(ag))
