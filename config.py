#from .hubert import basic
#from .funci import adder
import subprocess
import time
def config():
  
  print('config running')
  subprocess.run('conda env create -f queue_test_0/env3.yml',shell =True)
  
  f = open('outputs/a_test_dile.txt','w+')
  f.write('Environment Created')
  f.close()
  
  time.sleep(150)
  subprocess.run('conda run -n env3 python queue_test_0/funci.py',shell =True)
  
  
  
  
 


  #subprocess.run('conda env create -f environment.yml', shell=True)
  #subprocess.run('conda activate stats', shell=True)
  #subprocess.run('cd home/jupyter/Mukesh4/Queue',shell= True)
  #subprocess.run('rq worker --with-scheduler',shell =True)
  #adder() 
  
  

  
  

  
  
  
  
  
