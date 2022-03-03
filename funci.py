import time

def adder():
  print('creating  a file')
  time.sleep(10)
  
  f = open('outputs/a_Test_dile.txt','w+')
  f.write('hi hello world')
  f.close()
