import re

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def replacer(w):
    match = re.search('комар\w{0,3}?\W', w).group()
    print(match)
     
def main():
   replacer((openfile('komar.html')[:1000]))
if __name__ == "__main__":
    main()

    
