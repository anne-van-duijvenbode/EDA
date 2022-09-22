#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Import relevant libraries & load data 'participants.tsv'


# In[356]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


## Reading tsv-file and setting indexstart to 1


# In[357]:


data = pd.read_csv('participants.tsv', sep = '\t')

index = pd.RangeIndex(start=1, stop = 1347, step=1)
df = pd.DataFrame(data, index = index)
df.index


# In[8]:


###Checking the shape, datatypes and info of 'participants.tsv'


# In[358]:


print(df.shape, df.size)
print(data.dtypes)
print(data.info())
df[-10:]
# df[-10:]


# In[4]:


##Getting Numbers of 'formal ADHD', 'indication ADHD', both 'formal and incidication ADHD' and 'total ADHD'


# In[359]:


##Formal diagnosis ADHD
adhd_formal = df[(df['formal Dx'] == 'ADHD')]
n_adhd_formal = adhd_formal['formal Dx'].count()

##Two 'ADHD'-values contain an unexpected space  
adhd_indication = df[(df['indication'] == 'ADHD')]
adhd_indication_space =  df[(df['indication'] == 'ADHD ')]
n_adhd_indication = adhd_indication['indication'].count() + adhd_indication_space['indication'].count()

##Formal and Indication diagnosis
adhd_formal_and_indication_space = df[(df['indication'] == 'ADHD ') & (df['formal Dx'] == 'ADHD')]
adhd_formal_and_indication = df[(df['indication'] == 'ADHD') & (df['formal Dx'] == 'ADHD')]
n_adhd_formal_and_indication = adhd_formal_and_indication['formal Dx'].count() + adhd_formal_and_indication_space['formal Dx'].count()


n_missing_because_of_space = (n_adhd_formal - n_adhd_formal_and_indication)

n_adhd_total = (n_adhd_formal - n_adhd_formal_and_indication) + n_adhd_indication

print('ADHD formal: N = {}\n'       'ADHD indication: N = {}\n'      'ADHD formal and indication: N = {}\n'       'ADHD only formal: N = {}\n'      'ADHD total: N = {}'.format(n_adhd_formal, n_adhd_indication,                                   n_adhd_formal_and_indication,  n_only_formal, n_adhd_total,))


# In[360]:


## Further exploration indication ADHD
df_adhd_indication = df[(df['indication'] == 'ADHD') | (df['indication'] == 'ADHD ')]

df_adhd_indication[180:190]


# In[303]:


## Checking formal diagnoses after indication ADHD

# print(df_adhd_indication)
unique_adhd_indication = df_adhd_indication['formal Dx'].unique()
print(unique_adhd_indication)

## formal Dx == 'UNKNOWN'
formal_unknown_adhd_indication = df_adhd_indication[(df_adhd_indication['formal Dx'] == 'UNKNOWN')]
n_formal_unknown_adhd_indication = formal_unknown_adhd_indication['formal Dx'].count()


## formal Dx == 'ADHD'
formal_adhd_adhd_indication = df_adhd_indication[(df_adhd_indication['formal Dx'] == 'ADHD')]
n_formal_adhd_adhd_indication = formal_adhd_adhd_indication['formal Dx'].count()


## formal Dx == 'geen diagnose gevonden'
formal_no_diagnosis_adhd_indication = df_adhd_indication[(df_adhd_indication['formal Dx'] == 'geen diagnose gevonden')]
n_formal_no_diagnosis_adhd_indication = formal_no_diagnosis_adhd_indication['formal Dx'].count()


## formal Dx == nan
n_formal_nan_adhd_indication = df_adhd_indication['formal Dx'].isna().sum()

print('Participants with ADHD indication:\n\n'       'Unknown formal diagnosis: N = {}\n'       'Formal ADHD diagnosis: N = {}\n'       'No formal diagnosis: N = {}\n'       'Missing formal diagnosis: N = {} '.format(n_formal_unknown_adhd_indication,                                          n_formal_adhd_adhd_indication,                                          n_formal_no_diagnosis_adhd_indication,                                                  n_formal_nan_adhd_indication))


# In[ ]:


## Make table with numbers of ADHD diagnosis


# In[311]:


pip install tabulate


# In[312]:


from tabulate import tabulate


# In[353]:


table = [['ADHD diagnosis indication', 'N ='],           ['Unknown formal diagnosis', n_formal_unknown_adhd_indication],           ['Formal ADHD diagnosis', n_formal_adhd_adhd_indication],           ['No formal diagnosis', n_formal_no_diagnosis_adhd_indication],           ['Missing formal diagnosis',  n_formal_nan_adhd_indication]] 
     
         

table_formal_adhd = tabulate(table, headers = 'firstrow', tablefmt='github')

print(table_formal_adhd)


# In[375]:


#checking cases of multiple diagnoses including ADHD

m_dx = df.fillna('NaN') 

m_dx_formal = m_dx['formal Dx'].unique() 
m_dx_indication = m_dx['indication'].unique()

# print(m_dx_formal)
# print(m_dx_indication)

m_dx_formal_values = [d for d in m_dx_formal if 'ADHD' in d]
m_dx_indication_values = [d for d in m_dx_indication if 'ADHD' in d]


print(m_dx_formal_values)
print(m_dx_indication_values)


# In[384]:


## Formal 'ADHD/OCD'
m_dx_formal_ADHD_OCD = df[(df['formal Dx'] == 'ADHD/OCD')]
n_m_dx_formal_ADHD_OCD = m_dx_formal_ADHD_OCD['formal Dx'].count()

## Indication 'ADHD/ASPERGER'
m_dx_indication_ADHD_ASP = df[(df['indication'] == 'ADHD/ASPERGER')]
n_m_dx_indication_ADHD_ASP = m_dx_indication_ADHD_ASP ['indication'].count()

## Indication 'ADHD/DYSLEXIA'
m_dx_indication_ADHD_DYS = df[(df['indication'] == 'ADHD/DYSLEXIA')]
n_m_dx_indication_ADHD_DYS = m_dx_indication_ADHD_DYS ['indication'].count()

## Indication 'ADHD/ASD/ANXIETY'
m_dx_indication_ADHD_ASD_ANX = df[(df['indication'] == 'ADHD/ASD/ANXIETY')]
n_m_dx_indication_ADHD_ASD_ANX = m_dx_indication_ADHD_ASD_ANX ['indication'].count()

## Indication 'MDD/ADHD'
m_dx_indication_MDD_ADHD = df[(df['indication'] == 'MDD/ADHD')]
n_m_dx_indication_MDD_ADHD = m_dx_indication_MDD_ADHD ['indication'].count()

## Indication 'ADHD/PDD NOS'
m_dx_indication_ADHD_PDD = df[(df['indication'] == 'ADHD/PDD NOS')]
n_m_dx_indication_ADHD_PDD = m_dx_indication_ADHD_PDD ['indication'].count()

## Indication 'ADHD/EPILEPSY'
m_dx_indication_ADHD_EPI = df[(df['indication'] == 'ADHD/EPILEPSY')]
n_m_dx_indication_ADHD_EPI = m_dx_indication_ADHD_EPI ['indication'].count()

## Indication 'PDD NOS/ADHD'
m_dx_indication_PDD_ADHD = df[(df['indication'] == 'PDD NOS/ADHD')]
n_m_dx_indication_PDD_ADHD = m_dx_indication_PDD_ADHD ['indication'].count()

## Indication 'ADHD/ANXIETY'
m_dx_indication_ADHD_ANX = df[(df['indication'] == 'ADHD/ANXIETY')]
n_m_dx_indication_ADHD_ANX = m_dx_indication_ADHD_ANX ['indication'].count()

## Indication 'ADHD/DYSLEXIA/DYSCALCULIA'
m_dx_indication_ADHD_DYS_DYS = df[(df['indication'] == 'ADHD/DYSLEXIA/DYSCALCULIA')]
n_m_dx_indication_ADHD_DYS_DYS = m_dx_indication_ADHD_DYS_DYS ['indication'].count()

## Indication 'ADHD/MDD'
m_dx_indication_ADHD_MDD = df[(df['indication'] == 'ADHD/MDD')]
n_m_dx_indication_ADHD_MDD = m_dx_indication_ADHD_MDD ['indication'].count()

## Indication 'PTSD/ADHD' 
m_dx_indication_PTSD_ADHD = df[(df['indication'] == 'PTSD/ADHD' )]
n_m_dx_indication_PTSD_ADHD = m_dx_indication_PTSD_ADHD ['indication'].count()

## Indication 'ADHD/GTS'
m_dx_indication_ADHD_GTS = df[(df['indication'] == 'ADHD/GTS')]
n_m_dx_indication_ADHD_GTS = m_dx_indication_ADHD_GTS ['indication'].count()

## Indication 'MDD/ADHD/LYME'
m_dx_indication_MDD_ADHD_LYME = df[(df['indication'] == 'MDD/ADHD/LYME')]
n_m_dx_indication_MDD_ADHD_LYME = m_dx_indication_MDD_ADHD_LYME ['indication'].count()

## Indication 'ADHD/OCD'
m_dx_indication_ADHD_OCD = df[(df['indication'] == 'ADHD/OCD')]
n_m_dx_indication_ADHD_OCD = m_dx_indication_ADHD_OCD ['indication'].count()

## Indication 'MDD/OCD/ADHD'
m_dx_indication_MDD_OCD_ADHD = df[(df['indication'] == 'MDD/OCD/ADHD')]
n_m_dx_indication_MDD_OCD_ADHD = m_dx_indication_MDD_OCD_ADHD ['indication'].count()

## Indication 'MDD/ADHD/ANOREXIA'
m_dx_indication_MDD_ADHD_ANO = df[(df['indication'] == 'MDD/ADHD/ANOREXIA')]
n_m_dx_indication_MDD_ADHD_ANO = m_dx_indication_MDD_ADHD_ANO ['indication'].count()

## Total = 
print([n_m_dx_formal_ADHD_OCD,     n_m_dx_indication_ADHD_ASP,    n_m_dx_indication_ADHD_DYS,     n_m_dx_indication_ADHD_ASD_ANX,    n_m_dx_indication_MDD_ADHD,    n_m_dx_indication_ADHD_PDD,     n_m_dx_indication_ADHD_EPI,     n_m_dx_indication_PDD_ADHD,    n_m_dx_indication_ADHD_ANX,    n_m_dx_indication_ADHD_DYS_DYS,    n_m_dx_indication_ADHD_MDD,    n_m_dx_indication_PTSD_ADHD,    n_m_dx_indication_ADHD_GTS,    n_m_dx_indication_MDD_ADHD_LYME,     n_m_dx_indication_ADHD_OCD,     n_m_dx_indication_MDD_OCD_ADHD,     n_m_dx_indication_MDD_ADHD_ANO])

total_m_dx = sum([n_m_dx_formal_ADHD_OCD,     n_m_dx_indication_ADHD_ASP,    n_m_dx_indication_ADHD_DYS,      n_m_dx_indication_ADHD_ASD_ANX,    n_m_dx_indication_MDD_ADHD,    n_m_dx_indication_ADHD_PDD,     n_m_dx_indication_ADHD_EPI,     n_m_dx_indication_PDD_ADHD,    n_m_dx_indication_ADHD_ANX,    n_m_dx_indication_ADHD_DYS_DYS,    n_m_dx_indication_ADHD_MDD,    n_m_dx_indication_PTSD_ADHD,    n_m_dx_indication_ADHD_GTS,    n_m_dx_indication_MDD_ADHD_LYME,     n_m_dx_indication_ADHD_OCD,     n_m_dx_indication_MDD_OCD_ADHD,     n_m_dx_indication_MDD_ADHD_ANO])

print(total_m_dx)


['ADHD', 'ADHD/ASPERGER', 'ADHD/DYSLEXIA', 'ADHD/ASD/ANXIETY', 'MDD/ADHD',  'ADHD/PDD NOS', 'ADHD/EPILEPSY', 'PDD NOS/ADHD', 'ADHD/ANXIETY',  'ADHD/DYSLEXIA/DYSCALCULIA', 'ADHD/MDD', 'PTSD/ADHD', 'ADHD/GTS',  'MDD/ADHD/LYME', 'ADHD/OCD', 'MDD/OCD/ADHD', 'ADHD ', 'MDD/ADHD/ANOREXIA']

n_multiple_diagnoses_formal


# In[390]:


table = [['\033[1m' + 'Formal or indication' + '\033[0m', '\033[1m' + 'Diagnoses' + '\033[0m', '\033[1m' + 'N = ' + '\033[0m'],           ['formal', 'ADHD/OCD', n_multiple_diagnoses_formal],           ['indication', 'ADHD/ASPERGER', n_m_dx_indication_ADHD_ASP],            ['indication',  'ADHD/DYSLEXIA', n_m_dx_indication_ADHD_DYS],            ['indication',  'ADHD/ASD/ANXIETY',  n_m_dx_indication_ADHD_ASD_ANX],          ['indication',  'MDD/ADHD', n_m_dx_indication_MDD_ADHD],           ['indication',  'ADHD/PDD NOS', n_m_dx_indication_ADHD_PDD],           ['indication',  'ADHD/EPILEPSY', n_m_dx_indication_ADHD_EPI],           ['indication',  'PDD NOS/ADHD', n_m_dx_indication_PDD_ADHD],           ['indication',  'ADHD/ANXIETY', n_m_dx_indication_ADHD_ANX],           ['indication',  'ADHD/DYSLEXIA/DYSCALCULIA', n_m_dx_indication_ADHD_DYS_DYS],           ['indication',  'ADHD/MDD', n_m_dx_indication_ADHD_MDD],           ['indication',  'PTSD/ADHD', n_m_dx_indication_PTSD_ADHD],           ['indication',  'ADHD/GTS', n_m_dx_indication_ADHD_GTS],           ['indication',  'MDD/ADHD/LYME', n_m_dx_indication_MDD_ADHD_LYME],           ['indication',  'ADHD/OCD', n_m_dx_indication_ADHD_OCD],           ['indication',  'MDD/OCD/ADHD', n_m_dx_indication_MDD_OCD_ADHD],           ['indication',  'MDD/ADHD/ANOREXIA', n_m_dx_indication_MDD_ADHD_ANO],          ['\033[1m' + 'total' + '\033[0m', '', '\033[1m' + str(total_m_dx) + '\033[0m']]
     
         

table_formal_adhd = tabulate(table, headers = 'firstrow', tablefmt='github')

print(table_formal_adhd)


# In[392]:


## Getting numbers of healthy participants


# In[404]:


#checking cases of multiple diagnoses including ADHD
m_dx = df.fillna('NaN') 

m_dx_formal = m_dx['formal Dx'].unique() 
m_dx_indication = m_dx['indication'].unique()

# print(m_dx_formal)
# print(m_dx_indication)

m_dx_formal_values = [d for d in m_dx_formal if 'ADHD' not in d]
m_dx_indication_values = [d for d in m_dx_indication if 'ADHD' not in d]


print(m_dx_formal_values)
print(m_dx_indication_values)


# In[ ]:


## Checking numbers of 'HEALTHY', 'geen diagnose gevonden'


# In[442]:


people_no_adhd_formal = [d for d in m_dx['formal Dx'] if 'ADHD' not in d]
people_no_adhd_indication = [d for d in m_dx['indication'] if 'ADHD' not in d]

n_people_no_adhd_formal = len(people_no_adhd_formal)
n_people_no_adhd_indication = len(people_no_adhd_indication)

## formal 'HEALTHY'
dx_healthy_formal = df[(df['formal Dx'] == 'HEALTHY')]
n_dx_healthy_formal = dx_healthy_formal['formal Dx'].count()

## indication 'HEALTHY'
dx_healthy_indication = df[(df['indication'] == 'HEALTHY')]
n_dx_healthy_indication = dx_healthy_indication['indication'].count()

## formal and indication 'HEALTHY': 
dx_healthy_indication_formal = df[(df['indication'] == 'HEALTHY') | (df['formal Dx'] == 'HEALTHY')] 
n_dx_healthy_indication_formal = dx_healthy_indication['indication'].count()

## Formal no diagnosis:
dx_formal_no_dx = df[(df['formal Dx'] == 'geen diagnose gevonden')]
n_dx_formal_no_dx = dx_formal_no_dx['formal Dx'].count()

## indication ADHD and formal no diagnoses:
dx_adhd_indication_no_dx_formal = df[(df['indication'] == 'ADHD') | (df['formal Dx'] == 'geen diagnose gevonden')] 
n_dx_adhd_indication_no_dx_formal = dx_adhd_indication_no_dx_formal['indication'].count()

table = [['\033[1m' + 'indication or formal' + '\033[0m', '\033[1m' +  'Diagnosis'  + '\033[0m', '\033[1m' +  'N = '  + '\033[0m'],          ['indication', 'No ADHD', n_people_no_adhd_indication],       ['formal', 'No ADHD', n_people_no_adhd_formal],       ['formal', 'healthy', n_dx_healthy_formal],          ['indication', 'healthy', n_dx_healthy_indication],         ['indication and formal', 'healthy', n_dx_healthy_indication_formal],         ['indication and formal', 'indication: ADHD, formal: no diagnosis', n_dx_adhd_indication_no_dx_formal]         ]
        

table_formal_adhd = tabulate(table, headers = 'firstrow', tablefmt='github')

print(table_formal_adhd)

