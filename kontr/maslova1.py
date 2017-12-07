#sklgbjnx
i=0
#j=0
with open ("quotes.txt", encoding="utf-8") as f:
    text = f.read()
    lines = text.split('\n')
    #print(lines)
    for line in lines[:10]:
        #print(line)
        words=line.split()
        #print(words[0])
        if len(words[0]) < 5:
            for word in words:
                if word != '—':
                    i+=1
                    #print(word)
        #print(i)
        if i < 10:
            print(line)
        i = 0
            
