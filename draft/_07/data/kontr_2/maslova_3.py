def openfile(t):
    with open (t, encoding = 'utf-8') as f:
        tt = f.read()
    text = tt.split('\n')
    return text

def writefile(a,b):
    with open (b, 'w', encoding = 'utf-8') as f:
        f.write(a)

def main():
    print(openfile("icelandic.xml"))

if __name__ == '__main__':
    main()

