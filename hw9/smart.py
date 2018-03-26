import re

base = []

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def database(words):
    base = []
    tt = openfile('paradigm.txt')
    noun = tt.split()
    for word in words:
        i = 1
        j = 1
        for b in base:
            if word == b:
                 i = 0
                 break
            for n in noun:
                if word == n:
                    i = 0
                    break
        if i == 1:
            base.append(word)
    return base

def findword(a):
    base1 = re.findall('откро[йюе]\w*', a)
    base2 = re.findall('откры[лт]\w*', a)
    base3 = re.findall('открывш\w*', a)
    base4 = re.findall('открыв ', a)
    for i, b in enumerate(base4):
        base4[i] = b.strip(' ')
    base = base1 + base2 + base3 + base4
    res = database(base)
    return res
     
def main():
    print(findword(openfile('file1.txt')))
if __name__ == "__main__":
    main()

