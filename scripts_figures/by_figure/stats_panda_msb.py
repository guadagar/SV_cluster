
#!/usr/bin/env python
import matplotlib.ticker as mticker
import numpy as np
from scipy import stats
import pandas as pd
'''
This script is used to calculate statistics between multi-synaptic boutons (MSB) and single synaptic boutons (SSB) 
GCG
'''


data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')

data['den'] = data['nr_ves_in']/data['final_chull_ax']

ltp_nm = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'No')  & (data['msb']=='y') ]#& (data['final_chull_mvv']>0 )]#- data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05)]
c_nm = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'No') & (data['msb']=='y') ]#& (data['final_chull_mvv']>0 )]#final_med_mean_dis - data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05) ]

ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') & (data['msb']=='y') ]#& (data['final_chull_mvv']>0 )]# - data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05)]
c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes') &  (data['msb']=='y')]# & (data['final_chull_mvv']>0 )]# - data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05)]

ltp_nm_ss = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'No') &  (data['msb']=='n') ]#& (data['final_chull_mvv']>0 )]#]#- data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05)]
c_nm_ss = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'No') & (data['msb']=='n') ]#& (data['final_chull_mvv']>0 ) ]#& (data['msb']=='n')]#final_med_mean_dis - data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05) ]

ltp_m_ss = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') & (data['msb']=='n') ]#& (data['final_chull_mvv']>0 ) ]#& (data['msb']=='n')]# - data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05)]
c_m_ss = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes') & (data['msb']=='n')]# & (data['final_chull_mvv']>0 )]#& (data['msb']=='n')]# - data['dis_ves_ol_ra_f'] < 0 ) & (data['pval_d_ves_ol'] <0.05)]

a = 'final_med_mean_dis'

x = 5
print('MSB, LTP-c-NM',np.round(ltp_nm[a].median(),decimals=x),np.round(c_nm[a].median(),decimals=x),stats.mannwhitneyu(ltp_nm[a], c_nm[a])[1])
print('LTP-c-NM',np.round(ltp_nm[a].std(),decimals=x),np.round(c_nm[a].std(),decimals=x),stats.mannwhitneyu(ltp_nm[a], c_nm[a])[1])

print('MSB, LTP-C-M',np.round(ltp_m[a].median(),decimals=x),np.round(c_m[a].median(),decimals=x),stats.mannwhitneyu(ltp_m[a],c_m[a])[1])
print('LTP-C-M',np.round(ltp_m[a].std(),decimals=x),np.round(c_m[a].std(),decimals=x),stats.mannwhitneyu(ltp_m[a],c_m[a])[1])

print('MSB, LTP-NM-M',np.round(ltp_nm[a].median(),decimals=x),np.round(ltp_m[a].median(),decimals=x),stats.mannwhitneyu(ltp_nm[a],ltp_m[a])[1])
print('C-NM-M',np.round(c_m[a].median(),decimals=x),np.round(c_nm[a].median(),decimals=x),stats.mannwhitneyu(c_m[a],c_nm[a])[1])

print('LTP-C-NM-SSB',np.round(ltp_nm_ss[a].median(),decimals=x),np.round(c_nm_ss[a].median(),decimals=x),stats.mannwhitneyu(ltp_nm_ss[a], c_nm_ss[a])[1])
print('LTP-C-M-SSB',np.round(ltp_m_ss[a].median(),decimals=x),np.round(c_m_ss[a].median(),decimals=x),stats.mannwhitneyu(ltp_m_ss[a],c_m_ss[a])[1])

print('LTP-NM-SS',np.round(ltp_nm[a].median(),decimals=x),np.round(ltp_nm_ss[a].median(),decimals=x),stats.mannwhitneyu(ltp_nm[a], ltp_nm_ss[a])[1])
print('LTP-M-SS',np.round(ltp_m[a].median(),decimals=x),np.round(ltp_m_ss[a].median(),decimals=x),stats.mannwhitneyu(ltp_m[a],ltp_m_ss[a])[1])
print('C-NM-SS',np.round(c_nm[a].median(),decimals=x),np.round(c_nm_ss[a].median(),decimals=x),stats.mannwhitneyu(c_nm[a], c_nm_ss[a])[1])
print('C-M-SS',np.round(c_m[a].median(),decimals=x),np.round(c_m_ss[a].median(),decimals=x),stats.mannwhitneyu(c_m[a],c_m_ss[a])[1])
