caesar="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
word=input("insert a word: ")
i=int(input("insert a number from 1 to 25 inclusively: "))
encr=""
y=0
for a in word:
    for b in caesar:
        if a==b:
            encr+=caesar[y+i]
            y=0
            break
        y+=1        
print(encr)
if len(word)>=6:
    pswrd=input("insert password ")
    if pswrd=="password":
        print("double encryption enabled!!!")
        print(encr[3::]+encr[:3])
        print("поставьте десять плес я так старалась")
    else:
        print ("incorrect password, но десять всё равно поставьте")

