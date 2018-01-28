import random
def getfile(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
        lines = text.split('\n')
        #print(lines)
        return lines
def choice(lines):
    chs = ['1','2','3']
    return random.choice(chs)









def main():
    lines = getfile('filename.txt')
    print(choice(lines))
if __name__ == "__main__":
    main()
