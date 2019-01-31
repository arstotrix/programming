def openfile(file):
    with open (file, encoding = 'utf-8') as f:
        words = []
        puncts = """.,?!:;—""«»„“()<>"""
        text = f.read().split('\n')
        for t in text:
            words += t.split()
        for i, word in enumerate(words):
            words[i] = word.strip(puncts)
    return words
def listedd(text):
    thicc = [a for a in text if len(a) >= 7]
    return thicc
def outputt(listt):
    for a in listt:
        print('{:-<20}{:->20}'.format(a, len(a)))
    return 0
def main():
    outputt(listedd(openfile('text.txt')))
if __name__ == '__main__':
    main()
