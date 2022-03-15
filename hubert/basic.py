import librosa
from transformers import HubertForCTC, Wav2Vec2Processor
import torch
import os
import tensorflow as tf


def s2t():
  processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
  model = HubertForCTC.from_pretrained("facebook/hubert-large-ls960-ft") 
  
  print("number of gpus are: ",tf.test.is_gpu_available(cuda_only=True))
  
  speech, rate = librosa.load('./queue_test_0/hubert/Harvard list 01.wav', sr=16000)
  
  input_values = processor(speech, return_tensors="pt", padding="longest", sampling_rate=rate).input_values
  logits = model(input_values).logits
  
  predicted_ids = torch.argmax(logits, dim=-1)
  transcription = processor.batch_decode(predicted_ids)
  print(transcription)
  
  f = open('outputs/converted.txt','w+')
  f.write(transcription[0])
  f.close()
