import matplotlib.pyplot as plt 
import numpy as np 
# read data for dispersion plot from the freq.gp file

DISP_FILENAME  = "AlAs_dispersion.freq.gp"    
with open(DISP_FILENAME, 'r') as fr:
    data = np.array([[float(d) for d in l.split()] for l in iter(fr)])

x = np.array([_[0] for _ in data])
y = np.array([_[1:] for _ in data])

# set the High Symmetry Points as indicated in the output of plotband.x
hsp = [
        np.array([0.0, 0.0, 0.0]), # gamma
        np.array([0.75, 0.75, 0.0]), #K 
        np.array([0.5, 1.0, 0.0]), #W 
        np.array([0.0, 1.0, 0.0]), #X 
        np.array([0.0, 0.0, 0.0]), #gamma
        np.array([0.5,0.5,0.5])
        ]
# compute the abscissas corresponding to each high-symmetry point

s = [0.0, ] + [np.sqrt((hsp[i]-hsp[j]).dot(hsp[i]-hsp[j])) 
        for i,j in zip(range(1,len(hsp)),range(len(hsp))) ]

temp = [sum(s[0:i+1]) for i in range(len(s))] 
s = temp

# read data for VDOS 

VDOS_FILE = 'AlAs.vdos' 
with open(VDOS_FILE, 'r') as fr:
    fr.readline() 
    dosdata = np.array([[float(_) for _ in __.split()] for __ in iter(fr)])
e = [_[0] for _ in dosdata]
dd = [_[1] for _ in dosdata]

#Create the figure with matplotlib

fignew = plt.figure(constrained_layout=True, figsize=[10,8])
widths = [7,3]
heights=[12,]
spec = fignew.add_gridspec(ncols=2, nrows=1, width_ratios=widths, 
    height_ratios=heights, wspace=0.03, hspace=1.0)

#plot the dispersion 

ax = fignew.add_subplot(spec[0,0])
plt.sca(ax)
plt.plot(x,y, color='black')
plt.axis([0,x[-1],0, 450])
plt.xticks(s,['$\mathrm{\Gamma}$','$\mathrm{K}$', 'W', 'X', '$\mathrm{\Gamma}$','L'], size=28)
plt.yticks(size=24)
plt.ylabel('energies ($\mathrm{cm}^{-1}$)', size=24)
plt.grid(visible=True, axis='x')
plt.tick_params(axis='x',which='major',length=4,width=4, direction='out',grid_alpha=0.5, grid_linewidth=4)    

#plot the VDOS

ax = fignew.add_subplot(spec[0,1])
plt.sca(ax)

plt.plot(dd,e,color='black', linewidth=2 )
_ = plt.axis()
plt.axis([0.0, _[1], 0.0,450])

plt.xlabel('DOS', size=24)
plt.yticks([],[])
plt.xticks([],[])

#plt.subplots_adjust(wspace=0.05)
plt.savefig(fname='disp_and_dos.png',facecolor='white',bbox_inches='tight')

