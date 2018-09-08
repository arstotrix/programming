import re

def openfile(t):
    with open (t, encoding = 'utf-8') as f:
        text = f.read()
    return text

def finder(a):
    t = re.search ("\n.*?</teiHeader>.*?\n" ,a).group()
    #print(t)
    return t

def counter(a, b):
    bb = b.strip('\n')
    i = 0
    aa = a.split('\n')
    for j in aa:
        i+=1
        if j == bb:
            break
        #print (i, j)
    return i

def writefile(a,b):
    with open (b, 'w', encoding = 'utf-8') as f:
        f.write(a)
        
def main():
    writefile(str(counter(openfile("icelandic.xml"),finder(openfile("icelandic.xml")))), 'maslova_1.txt')

if __name__ == '__main__':
    main()
