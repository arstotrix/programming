words=[]
word=input("Введите слово: ")
while word!="":
    word=word[:2]+word[3:]
    word=word[::-1]
    words.append(word+' ')
    word=input("Введите слово: ")   
filename="text2.txt"
with open (filename, 'w') as f:
    for w in words:
      f.write(w+'\n')
