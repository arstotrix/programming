def is_palindrome(line):
    res = True
    pal = ''
    puncts = """.,?!:;—""«»„“()<>"""
    words = (line.replace('-', ' ')).split(' ')
    for i, word in enumerate(words):
        words[i] = word.strip(puncts)           
    for word in words:
        pal += word.lower()    
    for i in range (0,len(pal)):
        if pal[i] != pal[len(pal)-1-i]:
            res = False
            break
    return res

#я не знаю, необходима ли эта часть, но пусть будет
    
def main():
    print(is_palindrome(input('Введите фразу: ')))
    
if __name__ == '__main__':
    main()
        
