import pandas as pd

def my_func():
  df = pd.read_csv('cadec_csv.csv')
  print(df['Adverse Effects'][1])

  
