import re

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def replacer(w):
    match = re.sub('комар(\w{0,3}?\W)','слон\1' , w)
    mmatch = re.sub('Комар(\w{0,3}?\W)','Слон\1' , w)
    print(mmatch)
     
def main():
   replacer(openfile('komar.html'))
if __name__ == "__main__":
    main()

    
