import re

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text

def finder(w):
    match = re.findall('комар\w{0,3}?\W', w)
    mmatch = re.findall('Комар\w{0,3}?\W', w)
    print(match)
    print(mmatch)
     
def main():
   finder((openfile('komar.html')))
if __name__ == "__main__":
    main()

    
