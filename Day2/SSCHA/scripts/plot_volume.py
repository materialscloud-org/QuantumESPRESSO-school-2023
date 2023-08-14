import matplotlib.pyplot as plt
import numpy as np

import cellconstructor as CC, cellconstructor.Phonons



dyn300 = CC.Phonons.Phonons("relaxed_300_", nqirr=13)
dyn400 = CC.Phonons.Phonons("relaxed_400_", nqirr=13)


temperatures = [300, 400]
volumes = [
        dyn300.structure.get_volume(),
        dyn400.structure.get_volume()
        ]


plt.plot(temperatures, volumes, marker="o")
plt.xlabel("Temepareuter [K]")
plt.ylabel(r"Primitive cell volume [$\AA^3$]")
plt.tight_layout()
plt.savefig("volume.png")
plt.show()
