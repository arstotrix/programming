import random
lines = []
line = []
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


def adjefem2():
    return choice(getfile('adjefem2.txt'))

def adjemal2():
    return choice(getfile('adjemal2.txt'))

def adjeneu2():
    return choice(getfile('adjeneu2.txt'))


def adjefem3():
    return choice(getfile('adjefem3.txt'))

def adjemal3():
    return choice(getfile('adjemal3.txt'))

def adjeneu3():
    return choice(getfile('adjeneu3.txt'))


def verbimp2():
    return choice(getfile('verbimp2.txt'))

def verbimp3():
    return choice(getfile('verbimp3.txt'))


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


def nouns2():
    return choice(getfile('nouns2.txt'))
    
def nouns3():
    return choice(getfile('nouns3.txt'))



#composing verse 1
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


#composing verse 2
def verse2(n):
    if n == 1:
        line2 = str(adjefem2()) + ' ' + str(nounfem3()) + ' ' + str(verbptf2())
    elif n == 2:
        line2 = str(adjemal2()) + ' ' + str(nounmal3()) + ' ' + str(verbptm2())
    elif n == 3:
        line2 = str(adjeneu2()) + ' ' + str(nounneu3()) + ' ' + str(verbptn2()) 
    elif n == 4:
        line2 = str(adjefem2()) + ' ' + str(nounfem2()) + ' ' + str(verbptf3()) 
    elif n == 5:
        line2 = str(adjemal2()) + ' ' + str(nounmal2()) + ' ' + str(verbptm3()) 
    elif n == 6:
        line2 = str(adjeneu2()) + ' ' + str(nounneu2()) + ' ' + str(verbptn3()) 
    elif n == 7:
        line2 = str(adjefem3()) + ' ' + str(nounfem2()) + ' ' + str(verbptf2()) 
    elif n == 8:
        line2 = str(adjemal3()) + ' ' + str(nounmal2()) + ' ' + str(verbptm2())
    elif n == 9:
        line2 = str(adjeneu3()) + ' ' + str(nounneu2()) + ' ' + str(verbptn2())    
    return line2
 

#composing verse 3
def verse3(n):
    if n == 1:
        line3 = verbimp2() + ', ' + nouns3() + '!' 
    elif n == 2:
        line3 = verbimp3() + ', ' + nouns2() + '!'
    return line3


#main program
def main():
    print(verse1(random.randint(1,6)))
    print(verse2(random.randint(1,9)))
    print(verse3(random.randint(1,2)))
    
if __name__ == "__main__":
    main()
