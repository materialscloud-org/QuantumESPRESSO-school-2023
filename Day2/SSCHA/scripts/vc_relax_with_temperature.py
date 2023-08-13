from ase.calculators.emt import EMT

import cellconstructor as CC, cellconstructor.Phonons
import sscha
import sscha.Ensemble, sscha.SchaMinimizer, sscha.Utilities
import sscha.Relax

TEMPERATURE=400
N_CONFIGS=100

dyn = CC.Phonons.Phonons("relaxed_300_", nqirr=13)

# Impose all phonons to be real
dyn.ForcePositiveDefinite()

# Generate the ensemble
ensemble = sscha.Ensemble.Ensemble(dyn, T0=TEMPERATURE)

minim = sscha.SchaMinimizer.SSCHA_Minimizer(ensemble)
minim.meaningful_factor = 0.001

# Setup utilities
ioinfo = sscha.Utilities.IOInfo()
ioinfo.SetupSaving("minimization_400")

# setup the automatic relax
relax = sscha.Relax.SSCHA(
        minim,
        ase_calculator = EMT(),
        N_configs=N_CONFIGS,
        max_pop=3)

relax.setup_custom_functions(custom_function_post=ioinfo.CFP_SaveAll)

relax.vc_relax(target_press=0,  # GPa
        static_bulk_modulus=100)

relax.minim.dyn.save_qe("relaxed_400_")


