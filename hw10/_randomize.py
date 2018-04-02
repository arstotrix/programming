import re
import random

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def openrand():
    t = openfile('t.txt').split('\n')
    a = openfile(random.choice(t) + '.html')
    return a

def finder(w):
    match = re.search('title="Столица"(.*?)title="(.*?)"', w, flags=re.DOTALL)
    print(match.group(2))
    
def main():
   finder(openrand())
if __name__ == "__main__":
    main()
