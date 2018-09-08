words=[]
i=0
word=input("Введите слово: ")
while word!="":
    i+=1
    word=word[:2]+word[3:]
    word=word[::-1]
    words.append(word+' ')
    word=input("Введите слово: ")   
lines=str(words)
words=lines.split(' ')
filename="text2.txt"
with open (filename, 'a') as f:
    for n in range(i):
        f.write(words[n]+'\n')
    
