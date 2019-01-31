import os
import re
import csv

def csv_writer(firstline):
    with open('taglines.csv', "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(firstline)

def openfile(file):
    with open (file, encoding = 'windows-1251') as f:
        text = f.read()
        #print(text)
    return text

def create(start_path):
    i = 0
    for root, dirs, files in os.walk(start_path):
        for file in files:
            fname = start_path + '/' + file
            punch(openfile(fname))       
    return i


def punch(file):
    a = re.search('meta content="(.*?)" name="docid"', file).group(1)
    b = re.search('title>(.*?)</title', file).group(1)
    c = re.search('meta content="(.*?)" name="author"', file).group(1)
    d = re.search('meta content="(.*?)" name="created"', file).group(1)
    e = re.search('meta content="(.*?)" name="topic"', file).group(1)
    f = re.search('meta content="(.*?)" name="tagging"', file).group(1)
    line = a, b, c, d, e, f
    with open('taglines.csv', "a", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(line)
    return a,b,c,d,e,f

def main():
    line = "doc_id", "title", "author", "created", "topic", "tagging"
    csv_writer(line)
    create('./news')
if __name__ == "__main__":
    main()
