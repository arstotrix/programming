
def openfile(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
        words = text.split('\n')
    return words

def main():
   checkfile = openfile("bear.txt")
   print(checkfile)
   

if '__name__' == '__main__':
    main()
