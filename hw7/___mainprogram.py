import random
dict={}

def getfile(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
        words = text.split()
        return words
    
def search(words):
    i = 0
    a = 0
    for word in words:
        if word[-3:] == "ing":
            i = int(dict[word])
            i = i+1
            dict[word]=i
    return dict

#def searching(ing,words):
#    for word in words:
#        if word == ing:
            
#    return 

def main():
    words = getfile('textfile.txt')
    print(words)
    print(search(words))
    ing = input("input an - ing form please: ")
#    print(searching(ing,words))

if __name__ == "__main__":
    main()
