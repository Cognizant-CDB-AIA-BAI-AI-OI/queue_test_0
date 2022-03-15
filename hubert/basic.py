import librosa
from transformers import HubertForCTC, Wav2Vec2Processor
import torch
import os

def s2t():
  processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
  model = HubertForCTC.from_pretrained("facebook/hubert-large-ls960-ft") 
  
  print("curr path is: ",os.getcwd())
  
  data = './harvard1.wav'
  
  speech, rate = librosa.load('harvard1.wav', sr=16000)
  
  input_values = processor(speech, return_tensors="pt", padding="longest", sampling_rate=rate).input_values
  logits = model(input_values).logits
  
  predicted_ids = torch.argmax(logits, dim=-1)
  transcription = processor.batch_decode(predicted_ids)
  print(transcription)
  
  f = open('outputs/converted.txt','w+')
  f.write(transcription)
  f.close()
