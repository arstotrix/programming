#вариант 1
user_lng="1"
while (user_lng != ""):
    i = 0
    user_lng = input("Your language here: ")
    with open ("Extinct_languages.tsv", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            pieces = line.split("\t")
            if(pieces[0] == user_lng):
                #похоже, там были повторяющиеся языки
                #поэтому я поставила проверку
                if i == 0:
                    print(pieces[0]+" "+pieces[1]+" "+pieces[2])
                    i += 1
    if i == 0:
        #если вводилось пустое слово, он сначала выводил non existent data
        #и только потом прекращал программу
        #и мне это не понравилось
        if user_lng != "":
            print("Non-existent data\n")
    
        
        
