#from .hubert import basic
#from .funci import adder
import subprocess
import time

def config():
  
  print('config running in test')
  time.sleep(30)
  print('done with queue test repo!!')
  '''
  try :
    import sys 
    subprocess.run('conda env create -f queue_test_0/env3.yml',shell =True)
  
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
      
      subprocess.run('conda run -n env3 python queue_test_0/funci.py',shell =True)
    
    except :
      f = open('outputs/a_test_dile.txt','a+')
      f.write(str(sys.exc_info()[0]))
      f.close()
    
    try :
      
      subprocess.run('conda env remove -n env3',shell =True)
    
    except :
      f = open('outputs/a_test_dile.txt','a+')
      f.write(str(sys.exc_info()[0]))
      f.close()
      
    else :
      f = open('outputs/a_test_dile.txt','a+')
      f.write('Environment Deleted')
      f.close()
 
  '''
 

