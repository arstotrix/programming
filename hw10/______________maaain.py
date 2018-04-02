import re
import random

base = []

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text
def openrand():
    t = openfile('t.txt').split('\n')
    a = openfile(random.choice(t) + '.html')
    #print(t)
    return a
def finder(w):
    res = re.findall(r'<a href="/wiki/.*" title="Столица">Столица</a></b>'+'\n'+r'</td>'+'\n'+r'<td><span class="no-wikidata" data-wikidata-property-id=".*"><a href="/wiki/.*" title="[а-яА-ЯёЁ]">', w)
    return res
     
def main():
   print(finder(openrand()))
if __name__ == "__main__":
    main()
