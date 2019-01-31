i = 0
with open ("quotes.txt", encoding="utf-8") as f:
    text = f.read()
    lines = text.split('\n')
    #print(lines)
    for line in lines:
        parts = line.split(". —")
        #print(parts[0])
        words = parts[0].split()
        for word in words:
            if word.lower() == "разум":
                i += 1
                #print(word)
        #print(i)
        if i != 0:
            print(parts[1]+"."+"\n")
        i = 0
        

