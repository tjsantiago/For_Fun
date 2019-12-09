import pandas as pd
import matplotlib.pyplot as plt

#gather filepaths
filepaths = []

numbers = list(range(2, 9))

for date in numbers:
    filepath = f'path/to/regional-global-daily-2019-12-0{date}.csv'
    filepaths.append(filepath)
    
#create data frames for filepaths and join them
dfs = []

for file in filepaths:
    df = pd.read_csv(file)
    dfs.append(df)
    
#dfs[2].head() # checking that the above worked

my_df = pd.concat(dfs)
my_df.info()

#keep only rows about Juice WRLD
df = my_df[my_df['Artist'].str.contains("WRLD")].copy()

#drop URL and Artist cause these aren't needed
df.drop(['URL', 'Artist'], axis = 1, inplace = True)

df.to_csv('path/to/Juice_WRLD.csv')
