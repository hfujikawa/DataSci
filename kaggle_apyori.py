# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:55:24 2020
https://www.kaggle.com/yugagrawal95/market-basket-analysis-apriori-in-python
@author: hfuji
"""

#import all required packages..
import pandas as pd
import numpy as np
from apyori import apriori

fpath = r'D:\Develop\DataSci\Kaggle\input\basket-optimisation.zip'

df = pd.read_csv(fpath, header=None)
print(df.head())

#replacing empty value with 0.
df.fillna(0,inplace=True)
print(df.head())

#for using aprori need to convert data in list format..
# transaction = [['apple','almonds'],['apple'],['banana','apple']]....
transactions = []
for i in range(0,len(df)):
    transactions.append([str(df.values[i,j]) for j in range(0,20) if str(df.values[i,j])!='0'])
print(transactions[0])

#Call apriori function which requires minimum support, confidance and lift, min length is combination of item default is 2".
rules = apriori(transactions,min_support=0.003,min_confidance=0.2,min_lift=3,min_length=2)
#it generates a set of rules in a generator file...
print(rules)
# all rules need to be converted in a list..
Results = list(rules)
print(Results)

#convert result in a dataframe for further operation...
df_results = pd.DataFrame(Results)
# as we see order statistics itself a list so need to be converted in proper format..
print(df_results.head())

#keep support in a separate data frame so we can use later.. 
support = df_results.support

'''
convert orderstatistic in a proper format.
order statistic has lhs => rhs as well rhs => lhs we can choose any one for convience i choose first one which is 'df_results['ordered_statistics'][i][0]'
''' 

#all four empty list which will contain lhs, rhs, confidance and lift respectively.

first_values = []
second_values = []
third_values = []
fourth_value = []

# loop number of rows time and append 1 by 1 value in a separate list.. first and second element was frozenset which need to be converted in list..
for i in range(df_results.shape[0]):
    single_list = df_results['ordered_statistics'][i][0]
    first_values.append(list(single_list[0]))
    second_values.append(list(single_list[1]))
    third_values.append(single_list[2])
    fourth_value.append(single_list[3])

#convert all four list into dataframe for further operation..
lhs = pd.DataFrame(first_values)
rhs= pd.DataFrame(second_values)
confidance=pd.DataFrame(third_values,columns=['Confidance'])
lift=pd.DataFrame(fourth_value,columns=['lift'])

#concat all list together in a single dataframe
df_final = pd.concat([lhs,rhs,support,confidance,lift], axis=1)
df_final

'''
 we have some of place only 1 item in lhs and some place 3 or more so we need to a proper represenation for User to understand. 
 removing none with ' ' extra so when we combine three column in 1 then only 1 item will be there with spaces which is proper rather than none.
 example : coffee,none,none which converted to coffee, ,
'''
df_final.fillna(value=' ', inplace=True)

#set column name
df_final.columns = ['lhs',1,2,'rhs','support','confidance','lift']

#add all three column because those where the lhs itemset only
df_final['lhs'] = df_final['lhs']+str(", ")+df_final[1]+str(", ")+df_final[2]

#drop those 1,2 column because now we already appended to lhs column..
df_final.drop(columns=[1,2],inplace=True)

#this is final output.. you can sort based on the support lift and confidance..
print(df_final.head())






