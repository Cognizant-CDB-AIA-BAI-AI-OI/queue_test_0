#from .hubert import basic
#from .funci import adder
import subprocess
import time

def config():
  
  print('config running')
  
  try :
    import sys 
    subprocess.run('conda env create -f queue_test_0/env_g.yml',shell =True)
  
  except :
    
    
    f = open('outputs/a_test_dile.txt','w+')
    f.write(str(sys.exc_info()[0]))
    f.close()
  
  else :
  
    f = open('outputs/a_test_dile.txt','w+')
    f.write('Environment Created')
    f.close()
  
    #time.sleep(150)
    
    try :
      
      subprocess.run('conda run -n env_g python queue_test_0/fun.py',shell =True)
    
    except :
      f = open('outputs/a_test_dile.txt','a+')
      f.write(str(sys.exc_info()[0]))
      f.close()
    
    try :
      
      subprocess.run('conda env remove -n env_g',shell =True)
    
    except :
      f = open('outputs/a_test_dile.txt','a+')
      f.write(str(sys.exc_info()[0]))
      f.close()
      
    else :
      f = open('outputs/a_test_dile.txt','a+')
      f.write('Environment Deleted')
      f.close()
 
  

  

 
