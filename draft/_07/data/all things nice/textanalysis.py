#это не код, а один огромный костыль, Маслова

base = []
count = {}

def openfile(filename):
    with open (filename, encoding = 'utf-8') as f:
        puncts = """.,?!:;—""«»„“()<>"""
        text = f.read()
        text = text.lower()
        words = text.split()
        for i, word in enumerate(words):
            words[i] = word.strip(puncts)
    return words

def sort(text):
    base = []
    count = {}
    for t in text:
        i = 1
        for b in base:
            if t == b:
                i = 0
                break
        if i == 1:
            base.append(t)
        if t in count:
            count[t] += 1    
        else:
            count[t] = 1
            
    return len(base), len(text), count

def topper(count):
    a = 0
    b = ''
    for c in count:
        if count[c] > a:
            a = count[c]
            b = c
    return b, a

def stats(file):
    c = ''
    a, b, z = sort(openfile(file))
    c, d = topper(z)
    return a, b, c, d, z

def main():
    r = input('введите название песни: ')
    while r != '' :
        a, b, c, d, z = stats(r+'.txt')
        print('вот статистика по количеству и частотности слов в данной песне:')
        print('количество различных слов в песне: ', a)
        print('общее количество слов в песне: ', b)
        #print(z)
        print('самое частотное слово в песне: ', c)
        print('оно было употреблено ', d, ' раз')
        r = input('введите название песни: ')
    
if __name__ == "__main__":
    main()
