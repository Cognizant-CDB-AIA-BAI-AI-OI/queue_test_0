import pysnooper
import time
#import gradio as gr
import os
import sys
#import openai
import subprocess
import pysnooper
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

@pysnooper.snoop('outputs/file.log')

def adder(text):
    tokenizer = T5Tokenizer.from_pretrained('t5-large')
    model = T5ForConditionalGeneration.from_pretrained('t5-large')
    model = model.to('cuda')
    inputs = tokenizer(text, return_tensors='pt')
    inputs = inputs.to('cuda')
    outputs = model.generate(**inputs,max_length=128)
    out_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    f = open('outputs/a_test_dile.txt','w+')
    f.write(str(out_text))
    f.close()

text='gender : Sachin Ramesh Tendulkar  pronounced [sət͡ʃin t̪eːɳɖulkəɾ]; born 24 April 1973) is a former international cricketer of India who served as captain of the Indian national team. He is regarded as one of the greatest batsmen in the history of cricket. He is the highest run scorer of all time in international cricket, and the only player to have scored one hundred international centuries, the first batsman to score a double century in a One Day International (ODI), the holder of the record for the most runs in both Test and ODI cricket, and the only player to complete more than 30,000 runs in international cricket. In 2013, he was the only Indian cricketer included in an all-time Test World XI named to mark the 150th anniversary of Wisden Cricketers Almanack. He is affectionately known as Little Master or Master Blaster. Tendulkar took up cricket at the age of eleven, made his Test debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years. In 2002, halfway through his career, Wisden Cricketers Almanack ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards. Later in his career, Tendulkar was a part of the Indian team that won the 2011 World Cup, his first win in six World Cup appearances for India. He had previously been named Player of the Tournament at the 2003 edition of the tournament, held in South Africa.'
adder(text)
