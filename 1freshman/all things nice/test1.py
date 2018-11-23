import os
texts = []
start_path = 'texts'
for root,dirs,files in os.walk(start_path):
    #print(files)
    texts += files
print(texts)
