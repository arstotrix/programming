def getfile(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
        words = text.split()
        puncts = """.,?!:;—""«»„“()<>"""
        #print(puncts)
        for i, word in enumerate(words):
            words[i] = word.strip(puncts)
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
    f = input('input a filename: ')
    if f == "":
        print("Sorry, try again")
    else:
        words = getfile(f)
        #print(words)
        print(search(words, dict))
        ing = input("input an - ing form please: ")
        if ing == '':
            print('Sorry, try again')
        else:
            print(searching(ing,dict))

if __name__ == "__main__":
    main()
