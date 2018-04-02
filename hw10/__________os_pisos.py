import re
import os

base = []

def openfile(a):
    with open (a, encoding = "utf-8") as f:
        text = f.read()
    return text
def openos():
    list = os.listdir('countries')
    for c in countries:
           a = openfile(c)
    return a
def finder(words):
    
    return a
     
def main():
   finder(openos())
if __name__ == "__main__":
    main()
