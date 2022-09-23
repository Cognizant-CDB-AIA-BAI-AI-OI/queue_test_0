#from .hubert import basic
#from .funci import adder
import subprocess
def config():
  #subprocess.run('conda init bash', shell = True)
  subprocess.run('conda run -n stats1 python funci.py',shell =True)
  #subprocess.run('conda env create -f environment.yml', shell=True)
  #subprocess.run('conda activate stats', shell=True)
  #subprocess.run('cd home/jupyter/Mukesh4/Queue',shell= True)
  #subprocess.run('rq worker --with-scheduler',shell =True)
  #adder() 

  
  
  
  
  
  
  
  
