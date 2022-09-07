import time
import subprocess
def adder():
  print('creating  a file')
  subprocess.run('conda init bash', shell = True)
  print(subprocess.run('conda activate stats', shell=True))
  print('comma')
  time.sleep(10)
  print(subprocess.check_output(['conda','env', 'list']).decode())
  print(subprocess.check_output("conda env list | grep '*'", shell=True, encoding='utf-8'))
  f = open('outputs/a_Test_dile.txt','w+')
  f.write('hi hello world')
  f.close()
