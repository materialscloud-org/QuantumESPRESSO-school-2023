from ase.calculators.emt import EMT

import cellconstructor as CC, cellconstructor.Phonons
import sscha
import sscha.Ensemble, sscha.SchaMinimizer, sscha.Utilities

TEMPERATURE=300
N_CONFIGS=100

dyn = CC.Phonons.Phonons("AgDyn", nqirr=13)

# Impose all phonons to be real
dyn.ForcePositiveDefinite()

# Generate the ensemble
ensemble = sscha.Ensemble.Ensemble(dyn, T0=TEMPERATURE)
ensemble.generate(N_CONFIGS)

# Compute energies forces and stress for the ensemble
ensemble.compute_ensemble(calculator = EMT(),
        compute_stress=True)


# Run SSCHA
minim = sscha.SchaMinimizer.SSCHA_Minimizer(ensemble)
minim.meaningful_factor = 0.001

# Setup utilities
ioinfo = sscha.Utilities.IOInfo()
ioinfo.SetupSaving("minimization_300")

minim.init()
minim.run(custom_function_post=ioinfo.CFP_SaveAll)
minim.finalize()

minim.dyn.save_qe("final_sscha_300_")
