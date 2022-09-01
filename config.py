#from .hubert import basic
from .funci import adder
def config():
  subprocess.run('source activate stats', shell=True)
  adder() 

  
  
