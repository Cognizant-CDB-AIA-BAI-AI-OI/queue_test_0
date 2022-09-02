#from .hubert import basic
from .funci import adder
import subprocess
def config():
  subprocess.run('conda activate stats', shell=True)
  adder() 
  
  
  
