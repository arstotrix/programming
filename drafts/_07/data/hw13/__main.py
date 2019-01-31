import os
import re

def counter(start_path):
    i = 0
    k = 0
    for root, dirs, files in os.walk(start_path):
        #print(root)
        k = len(root.split('\\'))-1
        #print(dirs)
        #print(k)
        if len(dirs) == 0:
            if k > i:
                i = k
    #print(i)
    return i

def main():
    print(counter('.'))
        
if __name__ == '__main__':
    main()
