import random
lines = []

#retrieving a file
def getfile(filename):
    with open (filename, encoding = "utf-8") as f:
        text = f.read()
        lines = text.split('\n')
        return lines
    
#randomly choosing one option
def choice(lines):
        return random.choice(lines)
    
#choosing parts of speech    
def nounfem2():
    return choice(getfile('nounfem2.txt'))

def nounmal2():
    return choice(getfile('nounmal2.txt'))

def nounneu2():
    return choice(getfile('nounneu2.txt'))


def nounfem3():
    return choice(getfile('nounfem3.txt'))

def nounmal3():
    return choice(getfile('nounmal3.txt'))

def nounneu3():
    return choice(getfile('nounneu3.txt'))


def verbptm2():
    return choice(getfile('verbptm2.txt'))

def verbptf2():
    return choice(getfile('verbptf2.txt'))

def verbptn2():
    return choice(getfile('verbptn2.txt'))


def verbptf3():
    return choice(getfile('verbptf3.txt'))

def verbptm3():
    return choice(getfile('verbptm3.txt'))

def verbptn3():
    return choice(getfile('verbptn3.txt')) 


def verse1(n):
    if n == 1:
        line1 = str(nounfem3())+ " " + str(verbptf2())
    elif n == 2:
        line1 = str(nounmal3())+ " " + str(verbptm2())
    elif n == 3:
        line1 = str(nounneu3())+ " " + str(verbptn2())
    elif n == 4:
        line1 = str(nounfem2())+ " " + str(verbptf3())
    elif n == 5:
        line1 = str(nounmal2())+ " " + str(verbptm3())
    elif n == 6:
        line1 = str(nounneu2())+ " " + str(verbptn3())
    return line1

def main():
    print(verse1(random.randint(1,6)))
    
if __name__ == "__main__":
    main()
    
