#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import pickle
from scipy.stats import skew
from scipy.stats import norm
from scipy import stats
import os,glob

folder_path = './xr/xr_vor_con/'

f2s = open('xr_pval_distri_vor_ax.txt','w')


for filename in glob.glob(os.path.join(folder_path,'*_ssvr.txt')):
    x = filename.split('/')
    #print(filename.split('/')[3])
    xname = x[3].split('_')[0]
    #print(xname)
    vor_vol = []
    file2open = os.path.join(folder_path,xname+'_ssvr.txt')
    p = open(file2open,'r')
    lines = p.readlines()[1:]
    p.close()
    n = 0
    for line in lines:
        vor_vol.append(float(line.split()[1]))
        n = n + 1
    #print('LTP',xname, 'ske:',skew(vor_vol),'med:',np.median(vor_vol),n)
#    di_ol_name = './latest_blend_11_22/dis_ves_ol/fh/'+xname+'_ssvr'
#    try:
#        di = pickle.load(open(di_ol_name,'rb'))
#        a_di = np.array(di[di!= 0])
#    except:
#        print('no di')
    #print('LTP','dis-OL',np.median(a_di))
    vor_vol_ra = []
    file_path_name1 = './random/xr/xr_vor_con/'+xname+'_ssvr.txt'
    #print(filename)
    try:
        p = open(file_path_name1,'r')
        lines = p.readlines()[1:]
        p.close()
        print('esta',xname)
        n_ra = 0
        for line in lines:
            vor_vol_ra.append(float(line.split()[1]))
            n_ra = n_ra + 1
        #print(vor_vol_ra)
        # #print('Ra-LTP',xname,'stats',stats.mannwhitneyu(vor_vol_ra, vor_vol)[1])
        print(xname,stats.mannwhitneyu(vor_vol_ra, vor_vol)[1])
        f2s.write(str(xname))
        f2s.write('\t')
        f2s.write(str(stats.mannwhitneyu(vor_vol_ra, vor_vol)[1]))
        f2s.write('\t')
        f2s.write(str(np.std(vor_vol)/np.mean(vor_vol)))
        f2s.write('\t')
        f2s.write(str(np.std(vor_vol_ra)/np.mean(vor_vol_ra)))
        f2s.write('\n')
    #print('LTP-Ra', 'med vor:',np.median(vor_vol),np.median(vor_vol_ra), 'stats:',stats.mannwhitneyu(vovor_vol_ra, vor_vol)[1])
    except:
        #continue
        print('No,random',xname)
    #distance OL
#    file_path_name2 = './latest_blend_11_22/mcell_sim/mcell_sim_all/random/dis_ves_ol/fh/'+xname+'_ssvr_ra'
#    try:
#        di = pickle.load(open(file_path_name2,'rb'))
#        a_di1 = np.array(di[di!= 0])
#        print('dis',xname,stats.mannwhitneyu(a_di, a_di1)[1])
#        f2s.write(str(xname))
#        f2s.write('\t')
#        f2s.write(str(stats.mannwhitneyu(a_di, a_di1)[1]))
#        f2s.write('\n')
#    except:
#        print('No,random',xname)
f2s.close()
# w = 5e-5
# bins = np.arange(0, 4e-3,w)
# v =  5.84e-5
# #ov_l = #[(i - v)/v  for i in vor_vol]
# #ov1_l = #[(i - v)/v  for i in vor_vol1]
# #ov_c = #[(i - v)/v  for i in vor_vol2]
#
# aov_l = np.array(vor_vol)
# #aov_l1 = np.array(vor_vol1)
# aov_l3 = np.array(vor_vol3)
#
#
#
# #print(np.median(ov_l),np.median(ov_c))
# plt.figure(1)
#
# hist, bin_edges = np.histogram((aov_l),bins)
# plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'r', label ='con',alpha =0.5)
#
# #hist, bin_edges = np.histogram((aov_l1),bins)
# #plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'b', label ='blen',alpha =0.5)
#
# hist, bin_edges = np.histogram((aov_l3),bins)
# plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'g', label ='random',alpha =0.5)
#
# #hist, bin_edges = np.histogram((aov_c1),bins)
# #plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'lightblue', label ='CTRL',alpha =0.8)
#S
# plt.ylabel('Frequency (#/N)')
# plt.xlabel(r'Vor Vol')
# plt.legend()
# #plt.savefig('two_distri_vol_ssb_nm')
# plt.show()
