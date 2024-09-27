import os
import sys
import ollama
import time

t0=time.time()

fn=sys.argv[1]
#parse something like de2en
src=fn[-12:-10]
dest=fn[-9:-7]

languages={
    'de':'German',
    'en':'English',
    'es':'Spanish',
    'fr':'French',
    'pt':'Portuguese',
    'ru':'Russian',
    'it':'Italian'
}

fo=f"results/baseline_run1_{src}2{dest}_{dest}.txt"

src=languages[src]
dest=languages[dest]

print(f"translating from {src} to {dest}",file=sys.stderr)

existent=[]
try:
     with open(fo,mode="r",encoding="utf-8") as file:
        existent = [line.rstrip() for line in file]
        print(f"using {len(existent)} lines already translated in {fo}")
except:
     print(f"{fo} does not exist, it will be created")

with open(fn,mode="r",encoding="utf-8") as file:
    k=-1
    with open(fo,mode="w",encoding="utf-8") as g:
        for line in file:
            k+=1
            if k>=len(existent):
                text=line
                print(f"{k}",file=sys.stderr)
                response = ollama.chat(model='llama3.1:70b', messages=[
                 {"role": "system", "content": f"You are a helpful assistant specialised in biomedical translation. You will be provided with a text in {src}, and your task is to translate it into {dest}. You will add nothing and comment nothing, just produce the accurate translation of the text in specialist language. Keep the formatting as close as possible to the source and especially do not insert any newline."},
                 {'role': 'user','content': text},
                ],options={'num_ctx':8192})                
                translated=response['message']['content'].replace('\n', ' ').replace('\r', ' ')
                print(translated,file=g)                
                assert(response['done_reason']=="stop") 
                # if totaltokens >300:
                #     assert(0)
            else:
                print(existent[k],file=g)
            g.flush()

took=time.time()-t0
print(f"took: {took} s",file=sys.stderr)
            # if totaltokens>200:
            #     assert(0)
