# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 01:32:59 2017

@author: JUSTIN
"""

#Import libraries
import pandas as pd
import numpy as np
import matplotlib as plt

#Load training set
train = pd.read_csv("train.csv")


#Get summary statistics for dataset

print(train.head(10))
print(train.describe())
print(train['Property_Area'].value_counts())

#Examine distributions of values
print(train['ApplicantIncome'].hist(bins=50))
print(train.boxplot(column='ApplicantIncome', by = 'Education'))
print(train['LoanAmount'].hist(bins=50))

#Categorical variable analysis
temp1 = train['Credit_History'].value_counts(ascending=True)
temp2 = train.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map ({'Y':1,'N':0}).mean())
temp3 = pd.crosstab(train['Credit_History'], train['Loan_Status'])

print 'Frequency Table for Credit History:'
print temp1

print '\nProbability of getting loan from each Credit History Class:'
print temp2

temp3.plot(kind='bar', stacked=True, color=['red','blue'], grid = False)

#==============================================================================
# fig = plt.figure(figsize=(8,4))
# ax1 = fig.add_subplot(121)
# ax1.set_xlabel('Credit_History')
# ax1.set_ylabel('Count of Applicants')
# ax1.set_title("Applicants by Credit_History")
# temp1.plot(kind='bar')
# 
# ax2 = fig.add_subplot(122)
# temp2.plot(kind='bar')
# ax2.set_xlabel('Credit_History')
# ax2.set_ylabel('Probability of getting loan')
# ax2.set_title("Probability of getting loan by credit history")
#==============================================================================

# Check for missing values
print train.apply(lambda x: sum(x.isnull()),axis = 0)