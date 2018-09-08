import random
def getfile(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
        lines = text.split('\n')
        #print(lines)
        return lines
def choice(lines):
    return random.choice(lines)
def main():
    lines = getfile('filename.txt')
    print(choice(lines))
if __name__ == "__main__":
    main()
