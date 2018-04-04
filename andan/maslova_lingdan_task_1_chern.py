def joined(line):
    l = ''
    puncts = """.,?!:;—""«»„“()<>"""
    words = line.split(' ')
    for i, word in enumerate(words):
        words[i] = word.strip(puncts)
    for word in words:
        l += word.lower()
    return l
def is_palindrome(word):
    res = True
    for i in range (0,len(word)):
        if word[i] != word[len(word)-1-i]:
            res = False
            break
    print(res)

def main():
    is_palindrome(joined(input('Введите фразу: ')))

if __name__ == '__main__':
    main()
        
