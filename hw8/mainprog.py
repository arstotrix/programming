import random
dict = {}

def openfile(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
        words = text.split('\n')
    return words

def dictionarize(text, dict):
    keyword = text[0]
    hintlist = []    
    for i in range (1,len(text)):
        boom = text[i] + ' ...'
        hintlist.append(boom)
    dict[keyword] = hintlist    
    return dict
def playgame(dict, n):
    a = ''
    for i in range (0, len(n)):
        print(dict[n][i])
        t = input('введите версию: ')
        if (t == n):
             a = 'победа!'
             break
    if a!= 'победа!':
        a = 'вы проиграли'
    return a

    
def main():
    dct = dictionarize(openfile('bear.txt'), dict)
    dct = dictionarize(openfile('wolf.txt'), dict)
    dct = dictionarize(openfile('fox.txt'), dict)
    dct = dictionarize(openfile('hare.txt'), dict)
    dct = dictionarize(openfile('squirrel.txt'), dict)
    #print(dct)
    if random.randint(1,5) == 1:
        p = playgame (dict, 'медведь')
        print(p)
    elif random.randint(1,5) == 2:
        p = playgame (dict, 'волк')
        print(p)
    elif random.randint(1,5) == 3:
        p = playgame (dict, 'лиса')
        print(p)
    elif random.randint(1,5) == 4:
        p = playgame (dict, 'заяц')
        print(p)
    elif random.randint(1,5) == 5:
        p = playgame (dict, 'белка')
        print(p)
    
if __name__ == '__main__':
    main()
