import time
import subprocess
def adder():
  print('creating  a file')
  time.sleep(10)
  print(subprocess.check_output(['conda','env', 'list']).decode())
  print(subprocess.check_output("conda env list | grep '*'", shell=True, encoding='utf-8'))
  f = open('outputs/a_Test_dile.txt','w+')
  f.write(subprocess.check_output("conda env list | grep '*'", shell=True, encoding='utf-8'))
  #f.write('hi hello world')
  f.close()
