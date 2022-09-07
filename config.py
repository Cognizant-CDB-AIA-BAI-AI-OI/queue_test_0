#from .hubert import basic
from .funci import adder
import subprocess
def config():
  #subprocess.run('conda init bash', shell = True)
  #subprocess.run('conda ~/root/.bashrc',shell = True)
  #subprocess.run('conda install --stats', shell=True)
  #subprocess.run('conda env create -f environment.yml', shell=True)
  #subprocess.run('conda activate stats', shell=True)
  adder() 
  
  
