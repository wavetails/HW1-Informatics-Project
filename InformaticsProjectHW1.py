import csv
import pandas as pd
df = pd.read_csv(open('input1.csv'))
df1 = pd.melt(df, id_vars=["State"], var_name='Divorce and Marriage Rates' )
df1.sort_values('State', inplace=True)
df1.to_csv('output.csv')
print('output.csv')
