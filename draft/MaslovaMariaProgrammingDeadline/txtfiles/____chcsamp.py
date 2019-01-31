import random
lines = []
def getfile(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
        lines = text.split('\n')
        return lines
    
def choice(lines):
    return random.choice(lines)

def nounfem2():
    return choice(getfile('nounfem2.txt'))

def main():
    print(nounfem2())
if __name__ == "__main__":
    main()
