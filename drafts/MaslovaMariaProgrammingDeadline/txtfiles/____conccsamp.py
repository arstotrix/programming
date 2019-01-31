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


def nounmal2():
    return choice(getfile('nounmal2.txt'))


def main():
    line = str(nounfem2())+ " " + str(nounmal2())
    print(line)
if __name__ == "__main__":
    main()
