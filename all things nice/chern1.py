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
    for c in count:
        if count[c] > a:
            a = count[c]
            b = c
    return b, a

def stats(file):
    a, b, c = sort(openfile(file))
    d, e = topper(c)
    a = 'количество различных слов в песне: ' + str(a)
    b = 'общее количество слов в песне: ' + str(b)
    d = 'самое частотное слово в песне: ' + str(d)
    e = 'оно было употреблено ' + str(e) + ' раз'
    return a, b, d, e

def main():
    r = input('введите название песни: ')
    while r != '' :
        a, b, c, d = stats(r+'.txt')
        print('вот статистика по количеству и частотности слов в данной песне:')
        print(a)
        print(b)
        print(c)
        print(d)
        r = input('введите название песни: ')
    
if __name__ == "__main__":
    main()
