import pysnooper
import time
#import gradio as gr
import os
import sys
#import openai
import subprocess

import re
import io
import gzip
import pandas as pd

@pysnooper.snoop('outputs/file.log')

def adder() :
  #print('creating  a file')
  #time.sleep(10)
  #print(subprocess.check_output(['conda','env', 'list']).decode())
  #print(subprocess.check_output("conda env list | grep '*'", shell=True, encoding='utf-8'))
  
  
  def read_gzip_txt_file(file_path: str, encoding: str = 'utf-8') -> str:
  
    with open(file_path, 'rb') as f:
      content = f.read()

    with gzip.GzipFile(fileobj=io.BytesIO(content), mode='rb') as f:
      content = f.read()
    return content.decode(encoding)
  
  try :
    content1=read_gzip_txt_file('queue_test_0/file.txt')
    f = open('outputs/a_test_dile.txt','a+')
    f.write(str(len(content1)))
    f.close()
    
  except :
    f = open('outputs/a_test_dile.txt','a+')
    f.write(str(sys.exc_info()[0]))
    f.close()
    
  
  
  #f = open('outputs/a_test_dile.txt','w+')
  #f.write(subprocess.check_output("conda env list | grep '*'", shell=True, encoding='utf-8'))
  #f.write('hi hello world')
  #f.close()
  
 
  #f.close()
adder()
  
  

  
