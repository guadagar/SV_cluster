#!/usr/bin/env python
#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import matplotlib as mpl
import seaborn as sns
from matplotlib.lines import Line2D

'''
This script generates fig 5 panel f
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.7,1.3)}
mpl.rcParams.update(params)

fig, axs = plt.subplots(figsize=(1.7, 1.3))
fig.subplots_adjust(right=0.97, left = 0.25, bottom =0.3, top = 0.98)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')


data['den'] = data['nr_ves_b']/data['final_chull_mvv_ax']
data['den_loc'] = 1.0 /data['med_ass_ves_vol_final_ax']
data['den_loc_ra'] = 1.0 /data['ra_ass_ves_vol_final_ax']

ltp = data.loc[ (data['Condition'] == 'LTP') & (data['ra_ass_ves_vol_final_ax'] > 0) & (data['med_ass_ves_vol_final_ax'] > 0)]
c = data.loc[ (data['Condition'] == 'Control')  & (data['ra_ass_ves_vol_final_ax'] > 0) & (data['med_ass_ves_vol_final_ax'] > 0) ]

ltp_ra = data.loc[ (data['Condition'] == 'LTP') & (data['ra_ass_ves_vol_final_ax'] > 0) & (data['med_ass_ves_vol_final_ax'] > 0)]
c_ra = data.loc[ (data['Condition'] == 'Control')  & (data['ra_ass_ves_vol_final_ax'] > 0) & (data['med_ass_ves_vol_final_ax'] > 0) ]

sns.scatterplot(data=c, x= 'den',y= 'den_loc',s = 3,color='#224FDF',legend=False,ax=axs,zorder=10, label = 'Control')# marker='s',s = 2,c=l_ltp_m['per_mito'],cmap=plt.cm.viridis,vmin=0, vmax=20)
sns.scatterplot(data=ltp, x= 'den',y= 'den_loc',s = 3,color='#CB1D25',legend=False,ax=axs,zorder=10, label = 'LTP')# marker='s',s = 2,c=l_ltp_m['per_mito'],cmap=plt.cm.viridis,vmin=0, vmax=20)

sns.scatterplot(data=c_ra, x= 'den',y= 'den_loc_ra',s = 3,color='skyblue',legend=False,ax=axs,zorder=10, label = 'RD Control')# marker='s',s = 2,c=l_ltp_m['per_mito'],cmap=plt.cm.viridis,vmin=0, vmax=20)
sns.scatterplot(data=ltp_ra, x= 'den',y= 'den_loc_ra',s = 3,color='#F08080',legend=False,ax=axs,zorder=10, label = 'RD LTP')# marker='s',s = 2,c=l_ltp_m['per_mito'],cmap=plt.cm.viridis,vmin=0, vmax=20)

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(ltp['den']),np.log(ltp['den_loc']))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(c['den']),np.log(c['den_loc']))

a = np.exp(intercept)
b = slope
x = ltp['den']
plt.plot(x, a*(x**b),color='#CB1D25',lw=1,zorder=5)

a1 = np.exp(interceptc)
b1 = slopec
x1 = c['den']
plt.plot(x1, a1*(x1**b1),color='#224FDF',lw=1,zorder=5)

yText1 = r'R$^2$ = %.2f' %(np.round(r_valuec**2,decimals=2))
yText2 = r'R$^2$ = %.2f ' %(np.round(r_value**2,decimals=2))

slopera, interceptra, r_valuera, p_valuera, std_err = stats.linregress(np.log(ltp_ra['den']),np.log(ltp_ra['den_loc_ra']))
slopera_l, interceptra_l, r_valuera_l, p_valuera, std_err = stats.linregress(np.log(c_ra['den']),np.log(c_ra['den_loc_ra']))

ara = np.exp(interceptra)
b = slopera
x = ltp_ra['den']
plt.plot(x, ara*(x**b),color='#F08080',lw=1,zorder=5)

ara_l = np.exp(interceptra_l)
b = slopera_l
x = c_ra['den']
plt.plot(x, ara_l*(x**b),color='skyblue', lw=1,zorder=5)

plt.text(2900,120000, yText2, fontsize=6,color='#224FDF')
plt.text(2900,70000, yText1, fontsize=6,color='#CB1D25')

yText3 = r'R$^2$ = %.2f' %(np.round(r_valuera**2,decimals=2))
yText4 = r'R$^2$ = %.2f' %(np.round(r_valuera_l**2,decimals=2))

plt.text(2900,40000, yText3, fontsize=6,color='skyblue')
plt.text(2900,22000, yText4, fontsize=6,color='#F08080') #LTP

axs.set_ylim(7e2,22e4)
axs.set_xlim(7e2,1.1e4)

plt.ylabel('')
plt.xlabel('')

axs.set_ylabel(r'SV Den$\rm_{i}$  ($\mu m^{-3}$)',fontsize=6,labelpad=0.01)
axs.set_xlabel(r' SV Den$\rm_{C}$ ($\mu m^{-3}$)',fontsize=6,labelpad=0.01)

x = np.arange(1e3,12000,2000)
plt.plot(x, 1*(x),color='k',lw=1)

plt.xscale('log')
plt.yscale('log')

circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#224FDF",mec='#224FDF')
circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#CB1D25",mec='#CB1D25')
circ3 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="skyblue",mec='skyblue')
circ4 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#F08080",mec='#F08080')
plt.legend((circ1, circ2,circ3,circ4), ("Control","LTP","RD Control","RD LTP"), numpoints=1,loc='upper right',frameon = False, bbox_to_anchor=(0.50, 1.02,0.05,0.05),handletextpad=0.01,labelspacing=0.1)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/glob_vs_loc_den_log_f.png',dpi =600)

plt.show()