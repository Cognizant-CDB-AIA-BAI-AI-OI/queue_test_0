import pandas as pd

df = pd.read_csv('cadec_csv.csv')
print(df['Adverse Effects'][1])
