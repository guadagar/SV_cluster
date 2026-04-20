#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:16:55 2025

@author: ggarcia
"""

#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pickle
import matplotlib as mpl
import pandas as pd
from matplotlib.lines import Line2D

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.613,1.319)}
mpl.rcParams.update(params)
#

vol_cloud = 0.128

vol_axon = 0.583 - vol_cloud

#--------------------
ves_in_l = np.genfromtxt('./diff_ves_ltp_files/mcell/output_data/react_data/seed_00001/ves_in_cloud.dat',
                      dtype=float,
                     delimiter=' ')
ves_out_l = np.genfromtxt('./diff_ves_ltp_files/mcell/output_data/react_data/seed_00001/ves_out_axon.dat',
                      dtype=float,delimiter=' ')
ves_out_cloud_l = np.genfromtxt('./diff_ves_ltp_files/mcell/output_data/react_data/seed_00001/ves_out_cloud.dat',
                     dtype=float,delimiter=' ')
#----------------

ves_in_c = np.genfromtxt('./diff_ves_con_files/mcell/output_data/react_data/seed_00001/ves_in_cloud.dat',
                     dtype=float,
                      delimiter=' ')
ves_out_c = np.genfromtxt('./diff_ves_con_files/mcell/output_data/react_data/seed_00001/ves_out_axon.dat',
                     dtype=float,delimiter=' ')
ves_out_cloud_c = np.genfromtxt('./diff_ves_con_files/mcell/output_data/react_data/seed_00001/ves_out_cloud.dat',
                      dtype=float,delimiter=' ')
#-----------------

ves_in_lnm = np.genfromtxt('./diff_ves_nomito_ltp_files/mcell/output_data/react_data/seed_00001/ves_in_cloud.dat',
                      dtype=float,
                      delimiter=' ')
ves_out_lnm = np.genfromtxt('./diff_ves_nomito_ltp_files/mcell/output_data/react_data/seed_00001/ves_out_axon.dat',
                      dtype=float,delimiter=' ')
ves_out_cloud_lnm = np.genfromtxt('./diff_ves_nomito_ltp_files/mcell/output_data/react_data/seed_00001/ves_out_cloud.dat',
                    dtype=float,delimiter=' ')

#------------

ves_in_cnm = np.genfromtxt('./diff_ves_nomito_con_files/mcell/output_data/react_data/seed_00001/ves_in_cloud.dat',
                      dtype=float,
                      delimiter=' ')
ves_out_cnm = np.genfromtxt('./diff_ves_nomito_con_files/mcell/output_data/react_data/seed_00001/ves_out_axon.dat',
                      dtype=float,delimiter=' ')
ves_out_cloud_cnm = np.genfromtxt('./diff_ves_nomito_con_files/mcell/output_data/react_data/seed_00001/ves_out_cloud.dat',
                      dtype=float,delimiter=' ')

fig, ax = plt.subplots(figsize=(1.7,1.4))
fig.subplots_adjust(right=0.95, left = 0.21, bottom =0.22, top = 0.96)

ax.plot(ves_in_c[:2500000,0],ves_in_c[:2500000,1],color='navy',linestyle = '--')#,label = 'Control +M')
ax.plot(ves_in_l[:2500000,0]+2.5,ves_in_l[:2500000,1],color='#CB1D25',linestyle = '--')#,label = 'LTP +M')

ax.plot(ves_in_cnm[:2500000,0],ves_in_cnm[:2500000,1],color='#224FDF',linestyle = '--')#,label = 'Control -M')
ax.plot(ves_in_lnm[:2500000,0]+2.5,ves_in_lnm[:2500000,1],color='salmon',linestyle = '--')#,label = 'LTP -M')

circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#224FDF",mec='#224FDF')
circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="salmon",mec='salmon')
circ3 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="navy",mec='navy')
circ4 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#CB1D25",mec='#CB1D25')
plt.legend((circ1, circ2,circ3,circ4), ("Control -M ","LTP -M","Control +M","LTP +M"), numpoints=1,loc = 'lower left',mode ='expand', ncol=2, frameon = False,prop={'size': 5}, labelspacing=0.1,borderaxespad=0.1,handletextpad=0.1, handlelength=1)#,loc='upper right',frameon = False,handletextpad=0.01,labelspacing=0.1, bbox_to_anchor=(0.999, 0.9,0.05,0.05))
#plt.legend(loc = 'lower left',mode ='expand', ncol=2, frameon = False,prop={'size': 5}, labelspacing=0.1,borderaxespad=0.1,handletextpad=0.1, handlelength=1)

#plt.legend(prop={'size': 5},handlelength=1)
plt.ylim(0,700)
plt.xlim(0,5)
#plt.xlim(0,3.5e-4)

ax.set_ylabel(r'# SVs cluster',fontsize=6,labelpad=0.01)
ax.set_xlabel(r'Time (sec)',fontsize=6,labelpad=0.01)

plt.savefig('timec2ltp_m_nm.png', dpi=600)
plt.show()
