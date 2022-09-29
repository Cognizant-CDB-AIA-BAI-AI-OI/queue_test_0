#from .hubert import basic
#from .funci import adder
import subprocess
import time
def config():
  #subprocess.run('conda init bash', shell = True)
  print('config running')
  subprocess.run('conda env create -f queue_test_0/env1.yml',shell =True)
  time.sleep(100)
  subprocess.run('conda run -n env1 python queue_test_0/funci.py',shell =True)
  #subprocess.run('conda run -n gradio python queue_test_0/funci.py',shell =True)
  #print('done')
  
 
  #subprocess.run('conda env create -f environment.yml', shell=True)
  #subprocess.run('conda activate stats', shell=True)
  #subprocess.run('cd home/jupyter/Mukesh4/Queue',shell= True)
  #subprocess.run('rq worker --with-scheduler',shell =True)
  #adder() 

 
  

  
  
