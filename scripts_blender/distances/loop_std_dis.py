#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv

'''This script loops over all the standard distances and generates a text file with the name of each bouton and the standard distance
 02.01.22
GCG
'''

folder_path = './std_cm/xr/'
f = open('./std_cm/xr_std_dis.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_ssvr')):
    x = filename.split('/')
    xname = x[3].split('_')[0]
    di = pickle.load(open(filename,'rb'))

    #print(di)
    #print(filename, np.mean(di_min))
    f.write(xname)
    f.write('\t')
    f.write(str(di))
    #f.write('\t')
    #f.write(str(np.std(di)))
    f.write('\n')
f.close()
