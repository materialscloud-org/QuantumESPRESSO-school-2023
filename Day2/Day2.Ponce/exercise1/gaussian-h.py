###################################################################################
# Script to produce the spectral decomposition and integrated scattering rate.
# The spectral decomposition is computed at an energy 3/2 k_B T away from the band edge. 
# Samuel Poncé 
# Version1 - Fall 2018
# Version2 - Fall 2020
# Version3 - November 2022
# If you are using this script, please consider citing S. Ponc\'e et al, Phys. Rev. Research 3, 043022 (2021)
###################################################################################
import numpy as np

#####################################
# This needs to be manually updated and corresponds to the EPW calculation
mob_maxfreq = 160 # meV
mob_nfreq = 640
T = 300 # K
c = 1.0 # Gaussian broadening in meV. Should be smaller in practice. 
file1 = 'inv_tau_freq.fmt' # File name
nkpt = 272 # Number of k-points - same as in file1
nbnd = 3    # Number of bands - same as in file1
tol = 10.0 # meV. This means we are taking states around 3/2kbT +- tol in meV. In practice it should be quite small.
#####################################

#Constants
kb = 8.617333262145E-5 # eV/K
Ry2meV = 13605.6980659
hbar = 6.582119514E-16 # eVs
fact = 1.0 / (1000 * hbar * 1E12 ) # to get in THz

inv_tau_freq_tmp = np.zeros((nkpt, nbnd, mob_nfreq, 2))
inv_tau_freq_tmp[:,:,:,0] = -1000.0

step = mob_maxfreq / mob_nfreq # in meV

with open(file1,'r') as W:
  for lines in W:
    tmp = lines.split()
    if (tmp[0] == '#'):
        continue
    ikpt = int(tmp[0]) - 1
    ibnd = int(tmp[1]) - 1
    freq = float(tmp[3])
    ifreq = int(freq / step) - 1
    inv_tau_freq_tmp[ikpt, ibnd, ifreq, 0] = float(tmp[2])
    inv_tau_freq_tmp[ikpt, ibnd, ifreq, 1] = float(tmp[4])
# Put the energies in eV
inv_tau_freq_tmp[:, :, :, 0] = inv_tau_freq_tmp[:, :, :, 0] * Ry2meV
inv_tau_freq_tmp[:, :, :, 1] = inv_tau_freq_tmp[:, :, :, 1] * Ry2meV
# Find VBM
vbm = np.max(inv_tau_freq_tmp[:, :, :, 0])
print('VBM is located at ',vbm, ' meV')
# Rescale the energies to the VBM
inv_tau_freq_tmp[:, :, :, 0] = inv_tau_freq_tmp[:, :, :, 0] - vbm

# Find the energy that is at 3/2 kbT away
energy = 1000 * kb * T * 3.0 / 2 # in meV
print('Energy at 3/2 k_BT = ',energy,' meV')

# Create the final inv_tau_freq
inv_tau_freq =  np.zeros((mob_nfreq))
ndegen = np.zeros((mob_nfreq))

for ikpt in np.arange(nkpt):
  for ibnd in np.arange(nbnd):
    for ifreq in np.arange(mob_nfreq):
      if (np.abs(inv_tau_freq_tmp[ikpt, ibnd, ifreq, 0] + energy) < tol):
        inv_tau_freq[ifreq] += inv_tau_freq_tmp[ikpt, ibnd, ifreq, 1]
        ndegen[ifreq] += 1

# Average the values
for ifreq in np.arange(mob_nfreq):
  if (ndegen[ifreq] > 0):
    inv_tau_freq[ifreq] = inv_tau_freq[ifreq]/ndegen[ifreq]

# Sanity check
integral = 0.0
for ifreq in np.arange(mob_nfreq):
  integral += inv_tau_freq[ifreq] #* (step * 1E-3) # To get step in eV

print('Integrated scattering rate: tau^-1 = ',integral * fact, ' Thz')


# Now compute the cumulative integrals:
cum = np.zeros((mob_nfreq))
for ii in np.arange(mob_nfreq):
#  print ' Processing ',ii
  for jj in np.arange(ii):
    cum[ii] += inv_tau_freq[jj] #* step

# Gaussian broadening
# a = hight
# b = position
# c = width
def gauss(x,a,b,c):
  prefactor = a * step / (c*np.sqrt(2*np.pi))
  return prefactor * np.exp(- 0.5 * ((x-b)/c)**2 )

tau_gauss = np.zeros((mob_nfreq))
for ii in np.arange(mob_nfreq):
  for jj in np.arange(mob_nfreq):
    tau_gauss[ii] += gauss(ii * step, inv_tau_freq[jj] * fact,  jj * step, c)

with open(file1+'-gaussian'+str(c),'w') as W:
  W.write('# Freq [meV]   d tau^(-1) / d omega   \int_0^max domega tau^(-1)(omega) [THz] \n ')
  for ii in np.arange(mob_nfreq):
    W.write(str(ii * step)+'    '+str(tau_gauss[ii])+'     '+str(cum[ii] * fact)+' \n')

