
import re
dict = {}

def openfile(t):
    with open (t, encoding = 'utf-8') as f:
        text = f.read()
    return text

def finder(a):
    t = re.findall ("<w lemma=.*?\n" ,a)
    return t

def makedict(text, count):
    for t in text:
        tt = re.search('type="(.*?)"', t).group(1)
        
        if tt in count:
            count[tt] += 1   
        else:
            count[tt] = 1         
    return count

def writefile(a,b):
    with open (b, 'w', encoding = 'utf-8') as f:
        for i in a:
            aaaaa = i + ' встречается ' + str(a[i]) +' раз(a)\n'
            f.write(aaaaa)

def main():
    writefile(makedict(finder(openfile("icelandic.xml")), dict),'maslova_2.txt')
if __name__ == '__main__':
    main()
