import os
import re

def counter(start_path):
    i = 0
    k = 0
    for root, dirs, files in os.walk(start_path):
        print(root)
        k = root.split('\\')
        print(dirs)
        print(k)
    #print(i)
    return i

def main():
    print(counter('.'))
        
if __name__ == '__main__':
    main()
