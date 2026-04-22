#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import csv
from scipy import stats

'''
This script uses boostraping to estimate the SV radius for each series.
The output is the mean SV radius per series.
GCG
'''

mi = []
rad = []
with open('../latest_results/data/vesicles/fh_ves.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        #print(float(row[3]),row[5])
        rad.append(float(row[3]))
        mi.append(row[5])

idx_m = []
idx_nm = []

for i,j in enumerate(mi):
    if j=='y':
        idx_m.append(i)
    else:
        idx_nm.append(i)

a_rad = np.array(rad)

rad_nm = a_rad[idx_nm]
rad_m = a_rad[idx_m]

sampled_ves_vol_nm = rad_nm
sampled_ves_vol_m = rad_m

nrep = 10000 #number of times I repeat the process
f_ves_vol_nm = np.zeros((1, nrep))

for k in range(0,nrep):
        #rad_nm = stats.norm.rvs(loc=mu_nm, scale=sigma_nm, size=int(j), random_state=rng)
    ves_rad_sam = np.random.choice(sampled_ves_vol_nm,size = len(sampled_ves_vol_nm), replace = True)
    #print(ves_rad_sam)
        #plt.errorbar(k,np.mean(ves_tot[np.nonzero(ves_tot)])/j,marker = 'o',color='r')
    f_ves_vol_nm[0,k] = np.mean(ves_rad_sam)
    #print(k,np.mean(ves_rad_sam))
ra_me = np.median(f_ves_vol_nm[0,:]) #Mean
std_me = np.std(f_ves_vol_nm[0,:]) #SEM

print('nm',np.round(ra_me,decimals=4),np.round(std_me,decimals=4))

f_ves_vol_m = np.zeros((1,nrep))

for k in range(0,nrep):
    ves_rad_sam = np.random.choice(sampled_ves_vol_m,size = len(sampled_ves_vol_m), replace = True)
        #plt.errorbar(k,np.mean(ves_tot[np.nonzero(ves_tot)])/j,marker = 'o',color='r')
    f_ves_vol_m[0,k] = np.mean(ves_rad_sam)

ra_me = np.median(f_ves_vol_m[0,:]) #Mean
std_me = np.std(f_ves_vol_m[0,:]) #SEM

    #plt.errorbar(np.arange(100),(4/3.0)*np.pi*(mu_nm)**3*1e-9*np.ones(100),marker = 'o',color='k')
print('m',np.round(ra_me,decimals=4),np.round(std_me,decimals=4))


#plt.show()
