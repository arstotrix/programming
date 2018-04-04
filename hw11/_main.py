import re

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def replacer(w):
    match = re.search('комар\d{0,3}', w).group()
    print(match)
     
def main():
   replacer(openfile('komar.html'))
if __name__ == "__main__":
    main()

    
