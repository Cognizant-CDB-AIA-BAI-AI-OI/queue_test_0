import pandas as pd

def my_func():
  df = pd.read_csv('cadec_csv.csv')
  print(df['Adverse Effects'][1])
  
  f = open('outputs/csv_out.txt','w+')
  f.write(df1['Adverse Effects'][0])
  f.close()
