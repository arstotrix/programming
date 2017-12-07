i=0
with open ("quotes.txt", encoding="utf-8") as f:
    text = f.read()
    lines = text.split('\n')
    #print(lines)
    for line in lines:
        parts=line.split(". —" )
        words=parts[0].split()
        #print(len(words[0]))
        for word in words:
            if word != "—":
                i+=1
        #print(i)
        if i <= 10:
            if len(words[0]) < 5:
                print(line)
        i = 0
