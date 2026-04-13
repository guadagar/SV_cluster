#!/usr/bin/env python
#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import matplotlib as mpl

'''
This script generates fig 2 panel j
GCG
'''

params = {'axes.labelsize': 9,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last.csv')

c_m = data.loc[(data['Mito'] == 'Yes') & (data['Condition'] == 'Control')]
l_m = data.loc[(data['Mito'] == 'Yes') & (data['Condition'] == "LTP")]

fig, axs = plt.subplots(figsize=(2, 1.6))
fig.subplots_adjust(right=0.98, left = 0.26, bottom =0.22, top = 0.94)

plt.scatter(c_m['b_vol'],c_m['mito_vol'],color='#224FDF',marker='.',s = 10)
plt.scatter(l_m['b_vol'],l_m['mito_vol'],color='#CB1D25',marker='.', s = 10)

slopem, interceptm, r_valuem, p_valuem, std_errm = stats.linregress(np.log(c_m['b_vol']),np.log(c_m['mito_vol']))
slopelm, interceptlm, r_valuelm, p_valuelm, std_errlm = stats.linregress(np.log(l_m['b_vol']),np.log(l_m['mito_vol']))
print('con',p_valuem,'ltp',p_valuelm)
a = np.exp(interceptm)
b = slopem
x = c_m['b_vol']
plt.plot(x, a*(x**b),color='#224FDF')

a1 = np.exp(interceptlm)
b1 = slopelm
x1 = l_m['b_vol']
plt.plot(x1, a1*(x1**b1),color='#CB1D25')

axs.set_ylabel(r'Total Mito Vol ($\mu m^3$)',fontsize=9,labelpad=0.3)
axs.set_xlabel(r'Bouton Vol ($\mu m^3$)',fontsize=9,labelpad=0.3)

yText3 = r'R$^2$ = %.2f ' %(np.round(r_valuelm**2,decimals=2))
yText4 = r'R$^2$ = %.2f ' %(np.round(r_valuem**2,decimals=2))

plt.ylim(0.005,0.2)

plt.text(0.075,0.1, yText3, fontsize=7,color='#CB1D25')
plt.text(0.075,0.14, yText4, fontsize=7,color='#224FDF')

plt.xscale('log')
plt.yscale('log')

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/bvol_mito_vol.png',dpi =600)

plt.show()
