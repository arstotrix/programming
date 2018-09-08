#вариант 1
i = 0 
with open ("Extinct_languages.tsv", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        pieces = line.split("\t")
        #print(pieces)
        if pieces[2] == "Critically endangered\n":
            i+=1
            #print(i)
    print(i)
        
            
