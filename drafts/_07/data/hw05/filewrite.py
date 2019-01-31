word=input("Введите слово: ")
while word!="":
    word=word[:2]+word[3:]
    word=word[::-1]
    filename="text.txt"
    with open (filename, 'a') as f:
        f.write(word+"\n")
    word=input("Введите слово: ")
