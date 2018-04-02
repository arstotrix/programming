import re

base = []

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def finder(w):
    match = re.search('title="Столица"(.*?)title="(.*?)"', w, flags=re.DOTALL)
    print(match.group(2))
     
def main():
   finder(openfile('canada.html'))
if __name__ == "__main__":
    main()

    
