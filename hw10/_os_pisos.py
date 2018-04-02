# для тестирования нужно положить файл в папку countries
# как в образце

import re
import os

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def finder(w):
    match = re.search('title="Столица"(.*?)title="(.*?)"', w, flags=re.DOTALL).group(2)
    print('Столица: ' + match + '\n')

def openos():
    clist = os.listdir('countries')
    for c in clist:
        a = openfile(c)
        match = re.search('<title>(.*?) ', a, flags=re.DOTALL).group(1)
        print('Страна: ' + match)
        finder(a)

def main():
   finder(openos())
if __name__ == "__main__":
    main()
