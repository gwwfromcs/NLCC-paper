import numpy as np
import matplotlib.pyplot as plt

def file_len(fname):
    with open(fname) as f:
       for i, l in enumerate(f):
           pass
    return i + 1

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

alat = 4.5
blat = 2*np.pi/4.5
blat2 = blat**2
frhoc = open('rhocg.dat', 'r')
nrhoc = file_len('rhocg.dat')
frhov = open('rho_r_g.dat', 'r')
nrhov = file_len('rho_r_g.dat')

rhoc = np.zeros((nrhoc,2))
rhov = np.zeros((nrhov,2))
for i in range(nrhoc):
    line = (frhoc.readline()).split()
    rhoc[i,0] = float(line[3])*blat2
    rhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )

for i in range(nrhov):
    line = (frhov.readline()).split()
    rhov[i,0] = float(line[1])*blat2
    rhov[i,1] = np.sqrt( float(line[2])**2 + float(line[3])**2 )

plt.xlabel(r'$|G|^2/2$ (Ryd)')
plt.ylabel(r'$|\rho(G)|$ (a.u.)$^{-3}$')
t = np.arange(550.0, 1200.0, 0.5) # rhov stops at around 480 Ryd, extend it with zeros
s = np.zeros(len(t))
plt.plot(rhoc[:,0],rhoc[:,1],'r.',markersize=0.5)
plt.plot(rhov[:,0],rhov[:,1],'b.',markersize=0.5)
plt.plot(-1,100.0,'r.',markersize=4,label=r'partial core charge $|\rho_c(G)|$')
plt.plot(-1,100.0,'b.',markersize=4,label=r'valence charge $|\rho(G)|$')
plt.legend(loc='upper right', fontsize='small')

#plt.plot(t, s,'b.',markersize=0.5)
plt.xlim(100, 1100)
plt.ylim(-0.4e-8,0.000001)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.show()

plt.savefig("B-rhoc-vs-rhov.png",dpi=250)
