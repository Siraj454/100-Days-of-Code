# -*- coding: utf-8 -*-
"""


## Task Description
**The attached transactions.csv file has a years worth of transactions
that occur between 8am and 5pm every day, even weekends.  The "Time"
column includes the date and time.  The "Amount" column is the amount of
transaction which can be positive or negative.  Three additional columns
need to be added to this file.  "Balance", "Opening Balance", "Change
 From Opening Balance".  The "Balance" column should be the running
balance of all transactions up until that point in time.  "Opening
Balance" should be the last balance from the day prior.  The opening
balance will be 0 at the beginning.  "Change From Opening Balance"
should be the difference between the "Balance" column, and the "Opening
Balance" column, which can be positive or negative.  Send me back the
script that processes the file, and adds the three additional columns.**
"""

# import library pandas to handle csv
import pandas as pd

# read csv file into dataframe
df=pd.read_csv('transactions.csv')
df

# get information about the dataset
df.dtypes

## function to convert string values into numeric
def numeric(amount_string):
  return float(amount_string.replace(',',''))

# changing date column into right format , converting amount from string to float
df.Time=pd.to_datetime(df['Time'])
df['Amount']=df['Amount'].apply(lambda x:numeric(x))
df.dtypes

df.head()

"""**Task1: The "Balance" column should be the running balance of all transactions up until that point in time**"""

# take cumulative sum to get current balance
df['Balance']=df['Amount'].cumsum()
df

"""**--Task 2: "Opening Balance" should be the last balance from the day prior. The opening balance will be 0 at the beginning.**"""

# create day and month column
df['Day']=df['Time'].dt.day
df['Month']=df['Time'].dt.month

# group together month and date , and get last balance of each date
g=df.groupby(['Month', 'Day']).tail(1)['Balance']

# convert series of last balance of each day into list to use later
opn_bal=list(g)
# set initial value to zero as initial balance is zero and remove the last value
opn_bal.insert(0,0)
opn_bal.pop()
opn_bal

# for each date we have 108 values so duplicate each last balance to 108 to meet the dimensions
duplicate_opn=[i for i in opn_bal for j in range(108)]

# assign values to the column
df['Opening Balance'] = duplicate_opn

df

# drop unnecessary columns
df=df.drop(columns=['Day','Month'])
# add change from opening balance column
df["Change From Opening Balance"]=df['Balance']-df['Opening Balance']
"""## verify results by printing values of different dates,"""
print("*************Day 1***********")
print(df.loc[(df['Time'].dt.day==1) & (df['Time'].dt.month==1)])
print("*************Day 2***********")
print(df.loc[(df['Time'].dt.day==2) & (df['Time'].dt.month==1)])
print("*************Day 3***********")
print(df.loc[(df['Time'].dt.day==3) & (df['Time'].dt.month==1)])

# save results in a new csv
df.to_csv('transactions_done.csv')

