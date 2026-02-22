# What is Pandas?
'''
Pandas = Python Data Analysis Library

It provides:
Easy-to-use DataFrame (like Excel sheet)
Series (1D labeled array)
Fast data manipulation and cleaning
Integration with NumPy, Matplotlib, CSV, SQL, Excel 
'''
#Importing Pandas
import pandas as pd
import string

#Check the version of Pandas
print(f'Pandas version: {pd.__version__}')

#Pandas Data Structure
'''
There are two main data structures in Pandas:
Series → 1D labeled array
DataFrame → 2D labeled table
'''
data = [10,20,30,40,50]
s = pd.Series(data)
print(s)

#Custom index
value = range(1,21)  #1,2,3,...,20
index = list(string.ascii_lowercase[6:])
s1 = pd.Series(value, index=index)
print(s1)

#DataFrame: Like a table with rows and columns.
customerData = {
    'customer_id': [1,2,3,4,5],
    'name': ['John', 'Jane', 'Bob', 'Alice', 'Dave'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo']
}
indexValue = range(1,6)
df = pd.DataFrame(customerData, index=indexValue)
print(df)

#Viewing the data
print(df.head())  #First 5 rows
print('\n')
print(df.tail(2)) #Last 2 rows
print('\n')
print(df.shape)   #Number of rows and columns
print('\n')
print(df.columns) #Column names
print('\n')
print(df.info())  #Summary statistics
print('\n')
print(df.describe()) #Summary statistics
print('\n')

#Selecting rows and columns
df1 = df[['name', 'age']]
print(df1)
print('\n')
df2 = df.loc[1:4, ['name', 'age']]
print(df2)
print('\n')
print(df.loc[1])   #Selecting a row with a specific index i.e. 1
print('\n')

#Filtering & Sorting
df3 = df[df['age'] > 30]
print(df3)
print('\n')
df4 = df[df['age'] > 30].sort_values(by='age', ascending=False)
print(df4)

#Adding and modifying columns
df5 = df.assign(income=df['age']*1000)  #new data frame with new column
df5['tax'] = df5['age']*0.1             #new column with existing data
print(df5)

#Dropping columns
df6 = df5.drop(columns=['income'])         #new data frame without income column
print(df6)
df5.drop('income', axis=1, inplace=True)   #new data frame without tax column
print(df5)
df7 = df5.drop(['name', 'age'], axis=1, inplace=False)    #new data frame without name and age columns
print(df7)

#Merging
df8 = pd.DataFrame({'ID':[1,2], 'Name':['Alice','Bob']})
df9 = pd.DataFrame({'ID':[1,2], 'Salary':[50000,60000]})

df10=pd.merge(df8, df9, on='ID')
print(df10)