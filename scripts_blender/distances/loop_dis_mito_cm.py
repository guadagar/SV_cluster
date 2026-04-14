#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv

'''This script loops over the distances and generate text files with the minimum distance to the nearest mito and the
distance from the distance from the center to the closest mito.
02.01.22
GCG
'''

folder_path = './dis_cm/xr/'
f = open('./dis_cm/xr_dis_mito_cm.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_ssvr')):
    x = filename.split('/')
    xname = x[3].split('_')[0]
    di = pickle.load(open(filename,'rb'))
    #a_di = np.array(di[di!= 0])
    #print(di)

    f.write(xname)
    f.write('\t')
    f.write(str(di[0]))
    f.write('\t')
    f.write(str(di[1]))
    f.write('\n')
f.close()
