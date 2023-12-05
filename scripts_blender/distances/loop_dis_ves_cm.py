#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv

'''New code that loops over the distances and generate text files with the minimum distance to the active zone
I consider all the active zones present and for each vesicle I get the minimum distance
02.01.22
GCG
'''


folder_path = './dis_ol_dis_cm/xr/'
f = open('./dis_ol_dis_cm/xr_dis_ves_cm_median.txt','w')
#g = open('fh_az_dis_nmito_n.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_ssvr')):
    x = filename.split('/')
    xname = x[3].split('_')[0]
    di = pickle.load(open(filename,'rb'))
    a_di = np.array(di[di!= 0])
    #print(di)

    f.write(xname)
    f.write('\t')
    f.write(str(np.median(a_di)))
    f.write('\t')
    f.write(str(np.std(a_di)))
    f.write('\n')
f.close()
