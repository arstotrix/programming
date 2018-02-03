def getfile(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
        words = text.split()
        puncts = """.,?!:;—""«»„“()"""
        for word in words:
            for p in puncts:
                if word[-1] == p:
                    word.replace(p, '')
                elif word[0] == p:
                    word.replace(p, '')
        return words  
def search(words,dict):
    i = 0
    for word in words:
        if word[-3:] == "ing":
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return dict

def searching(ing,dict):
    if ing in dict:
        a = dict[ing]
        
    else:
        a = "This is not the word you're looking for"
    return a 

def main():
    dict={}
    words = getfile('textfile.txt')
    print(words)
    print(search(words, dict))
    ing = input("input an - ing form please: ")
    print(searching(ing,dict))

if __name__ == "__main__":
    main()
