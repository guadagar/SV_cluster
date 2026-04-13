#!/usr/bin/env python
import pandas as pd
import numpy as np
#from pingouin import ancova

#Esto corre en scarlett con, env myenv

data = pd.read_csv('all_data.csv')
#data = pd.read_csv('../../../../../latest_results/data/all_data_together/all_data.csv')

df_m = data.loc[ (data['Mito'] == 'Yes')]
#data['log_mean_ves_vol'] = np.log(data['mean_ves_vol'])
#data['log_b_vol'] =  np.log(data['b_vol'])
df_m['log_m_vol'] = np.log(df_m['mito_vol'])
df_m['log_b_vol'] =  np.log(df_m['b_vol'])

#ves_vol vs b_vol, condition, control - ltp
#a = ancova(data=data, dv='log_mean_ves_vol', covar='log_b_vol', between='Condition')
#print(a)
a = ancova(data=df_m, dv='log_m_vol', covar='log_b_vol', between='Condition')
print(a)