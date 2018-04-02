a=0
i=0
z=0
fname='123456.txt'
print(fname)
with open(fname, encoding="utf-8") as f:
    text = f.read()
    lines=text.split('\n')
#print(lines)
for line in lines:
    words=line.split(' ')
    i+=len(words)
    a+=1
    #print(a)
    #print(words)
    #print(i)
#z=i/a
print(i/a)
    

