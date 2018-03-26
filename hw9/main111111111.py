import re
def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text 
def findword(a):
    results = re.findall('откро[йюя].*? ', a)
    return results
    
    
def main():
    text = openfile('file.txt')
    print(text)
    print(findword(text))
if __name__ == "__main__":
    main()
