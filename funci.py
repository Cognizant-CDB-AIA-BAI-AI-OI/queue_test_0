import time
import gradio as gr
import os
import openai
import subprocess

def adder() :
  print('creating  a file')
  #time.sleep(10)
  print(subprocess.check_output(['conda','env', 'list']).decode())
  print(subprocess.check_output("conda env list | grep '*'", shell=True, encoding='utf-8'))
  f = open('outputs/a_test_dile.txt','w+')
  #f.write(subprocess.check_output("conda env list | grep '*'", shell=True, encoding='utf-8'))
  #f.write('hi hello world')
  #f.close()
  
  def output(text):
    openai.api_key = "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"
    response = openai.Completion.create( engine="text-davinci-002", prompt = text, temperature=0.7, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0 )
    return response["choices"][0]["text"]
  
  iface = gr.Interface(fn=output, inputs = gr.inputs.Textbox(label="Input",lines=15),outputs=gr.outputs.Textbox(label="Output"), theme="dark-seafoam",title ="NLP MegaModel")
  f.write(iface.launch(share=True)) 
  
  f.close()
adder()
  
  
