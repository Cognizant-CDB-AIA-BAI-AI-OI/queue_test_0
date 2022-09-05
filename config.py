#from .hubert import basic
from .funci import adder
import subprocess
def config():
  subprocess.run('conda init bash', shell = True)
  subprocess.run('source /opt/conda/etc/profile.d/conda.sh',shell = True)
  subprocess.run('conda activate stats', shell=True)
  adder() 
  
  
  
