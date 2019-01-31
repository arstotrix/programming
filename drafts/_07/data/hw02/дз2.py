word=input("Введите слово (только кириллица!): ")
a=0
for i in word:
    if (i!="а")and(i!="к")and (a%2!=0):
        print(i)
    a+=1
print("="*10)
