import numpy as np
import matplotlib.pyplot as plt

def file_len(fname):
    with open(fname) as f:
       for i, l in enumerate(f):
           pass
    return i + 1

alat = 4.5
blat = 2*np.pi/4.5
blat2 = blat**2

F_brhoc=open('b/extract-b-nlcc/rhocg.dat','r')
n_brhoc = file_len('b/extract-b-nlcc/rhocg.dat')
F_crhoc=open('c/extract-c-nlcc/rhocg.dat','r')
n_crhoc = file_len('c/extract-c-nlcc/rhocg.dat')
F_nrhoc=open('n/extract-n-nlcc/rhocg.dat','r')
n_nrhoc = file_len('n/extract-n-nlcc/rhocg.dat')

F_cr_rhoc=open('cr/extract-cr-nlcc/rhocg.dat','r')
n_cr_rhoc = file_len('cr/extract-cr-nlcc/rhocg.dat')
F_fe_rhoc=open('fe/extract-fe-nlcc/rhocg.dat','r')
n_fe_rhoc = file_len('fe/extract-fe-nlcc/rhocg.dat')
F_mn_rhoc=open('mn/extract-mn-nlcc/rhocg.dat','r')
n_mn_rhoc = file_len('mn/extract-mn-nlcc/rhocg.dat')

F_cr_rhoc=open('cr/extract-cr-nlcc/rhocg.dat','r')
n_cr_rhoc = file_len('cr/extract-cr-nlcc/rhocg.dat')
F_fe_rhoc=open('fe/extract-fe-nlcc/rhocg.dat','r')
n_fe_rhoc = file_len('fe/extract-fe-nlcc/rhocg.dat')
F_mn_rhoc=open('mn/extract-mn-nlcc/rhocg.dat','r')
n_mn_rhoc = file_len('mn/extract-mn-nlcc/rhocg.dat')

F_na_rhoc=open('Na/extract-na-nlcc/rhocg.dat','r')
n_na_rhoc = file_len('Na/extract-na-nlcc/rhocg.dat')
F_li_rhoc=open('Li/extract-li-nlcc/rhocg.dat','r')
n_li_rhoc = file_len('Li/extract-li-nlcc/rhocg.dat')
F_k_rhoc=open('K/extract-k-nlcc/rhocg.dat','r')
n_k_rhoc = file_len('K/extract-k-nlcc/rhocg.dat')

brhoc = np.zeros((n_brhoc,2))
nrhoc = np.zeros((n_nrhoc,2))
crhoc = np.zeros((n_crhoc,2))

fe_rhoc = np.zeros((n_fe_rhoc,2))
cr_rhoc = np.zeros((n_cr_rhoc,2))
mn_rhoc = np.zeros((n_mn_rhoc,2))

na_rhoc = np.zeros((n_na_rhoc,2))
li_rhoc = np.zeros((n_li_rhoc,2))
k_rhoc = np.zeros((n_k_rhoc,2))

for i in range(n_brhoc):
    line = (F_brhoc.readline()).split()
    brhoc[i,0] = float(line[3])*blat2
    brhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_brhoc.close()

for i in range(n_crhoc):
    line = (F_crhoc.readline()).split()
    crhoc[i,0] = float(line[3])*blat2
    crhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_crhoc.close()

for i in range(n_nrhoc):
    line = (F_nrhoc.readline()).split()
    nrhoc[i,0] = float(line[3])*blat2
    nrhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_nrhoc.close()

for i in range(n_fe_rhoc):
    line = (F_fe_rhoc.readline()).split()
    fe_rhoc[i,0] = float(line[3])*blat2
    fe_rhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_fe_rhoc.close()

for i in range(n_cr_rhoc):
    line = (F_cr_rhoc.readline()).split()
    cr_rhoc[i,0] = float(line[3])*blat2
    cr_rhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_cr_rhoc.close()

for i in range(n_mn_rhoc):
    line = (F_mn_rhoc.readline()).split()
    mn_rhoc[i,0] = float(line[3])*blat2
    mn_rhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_mn_rhoc.close()

for i in range(n_na_rhoc):
    line = (F_na_rhoc.readline()).split()
    na_rhoc[i,0] = float(line[3])*blat2
    na_rhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_na_rhoc.close()

for i in range(n_li_rhoc):
    line = (F_li_rhoc.readline()).split()
    li_rhoc[i,0] = float(line[3])*blat2
    li_rhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_li_rhoc.close()

for i in range(n_k_rhoc):
    line = (F_k_rhoc.readline()).split()
    k_rhoc[i,0] = float(line[3])*blat2
    k_rhoc[i,1] = np.sqrt( float(line[4])**2 + float(line[5])**2 )
F_k_rhoc.close()

plt.subplot(311)

plt.ylabel(r'$|\rho^{partial}_{core}(G)|$ (a.u.)$^{-3}$')
plt.plot(brhoc[:,0],brhoc[:,1],'r.',markersize=0.5)
plt.plot(crhoc[:,0],crhoc[:,1],'b.',markersize=0.5)
plt.plot(nrhoc[:,0],nrhoc[:,1],'k.',markersize=0.5)
plt.plot(-1,100.0,'r.',markersize=4,label=r'B')
plt.plot(-1,100.0,'b.',markersize=4,label=r'C')
plt.plot(-1,100.0,'k.',markersize=4,label=r'N')
plt.legend(loc='upper right', fontsize='small')

plt.xlim(200, 1100)
plt.xticks(np.arange(200,1200,100),10*[''])
plt.ylim(-0.4e-8,0.000002)
plt.yticks([0,1e-6,1e-6])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0),useMathText=True)

plt.subplot(312)

plt.ylabel(r'$|\rho^{partial}_{core}(G)|$ (a.u.)$^{-3}$')
plt.plot(fe_rhoc[:,0],fe_rhoc[:,1],'r.',markersize=0.5)
plt.plot(cr_rhoc[:,0],cr_rhoc[:,1],'b.',markersize=0.5)
plt.plot(mn_rhoc[:,0],mn_rhoc[:,1],'k.',markersize=0.5)
plt.plot(-1,100.0,'r.',markersize=4,label=r'Fe')
plt.plot(-1,100.0,'b.',markersize=4,label=r'Cr')
plt.plot(-1,100.0,'k.',markersize=4,label=r'Mn')
plt.legend(loc='upper right', fontsize='small')

plt.xlim(200, 1100)
plt.xticks(np.arange(200,1200,100),10*[''])
plt.ylim(-0.4e-8,0.0000005)
plt.yticks([0,1e-7,2e-7,3e-7,4e-7,5e-7])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0),useMathText=True)

plt.subplot(313)

plt.xlabel(r'$|G|^2/2$ (Rydberg)')
plt.ylabel(r'$|\rho^{partial}_{core}(G)|$ (a.u.)$^{-3}$')
plt.plot(na_rhoc[:,0],na_rhoc[:,1],'r.',markersize=0.5)
plt.plot(li_rhoc[:,0],li_rhoc[:,1],'b.',markersize=0.5)
plt.plot(k_rhoc[:,0], k_rhoc[:,1], 'k.',markersize=0.5)
plt.plot(-1,100.0,'r.',markersize=4,label=r'Na')
plt.plot(-1,100.0,'b.',markersize=4,label=r'Li')
plt.plot(-1,100.0,'k.',markersize=4,label=r'K ')
plt.legend(loc='upper right', fontsize='small')

plt.xlim(200, 1100)
plt.xticks(np.arange(200,1200,100), np.arange(200,1200,100))
plt.ylim(-0.4e-10,0.000000015)
plt.yticks([0,1e-8])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0),useMathText=True)

#plt.show()
plt.tight_layout()
fig = plt.gcf()
fig.set_size_inches(6, 6)
fig.savefig('compare_elements.png', dpi=250)
