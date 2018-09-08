import os
import re
import csv

def csv_writer(firstline):
    with open('usedabbr.csv', "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(firstline)

def openfile(file):
    with open (file, encoding = 'windows-1251') as f:
        text = f.read()
        #print(text)
    return text

def lem(start_path):
    i = 0
    for root, dirs, files in os.walk(start_path):
        for file in files:
            fname = start_path + '/' + file
            punch(openfile(fname))       
    return i


def punch(file):
    count = {}
    i = 0
    lems = re.findall('<w><ana lex="(.*?)"', file)
    for lem in lems:
        if lem.isupper():
            if lem in count:
                count[lem] += 1
            else:
                count[lem] = 1
            line = lem, count[lem]
            with open('usedabbr.csv', "a", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(line)

def main():
    line = "abbr", "used"
    csv_writer(line)
    lem('./news')
if __name__ == "__main__":
    main()
