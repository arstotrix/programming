def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
        words = text.split()
    return words 
def findword(a):
    
def main():
    words = openfile('file.txt')
    #print(words)
if __name__ == "__main__":
    main()
