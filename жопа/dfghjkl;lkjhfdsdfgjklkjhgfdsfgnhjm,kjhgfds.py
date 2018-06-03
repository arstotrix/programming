import os

def counter(start_path):
    i = 0
    k = 0
    l = {}
    for root, dirs, files in os.walk(start_path):
        #print(root)
        k = root.split('\\')[-1].lower()
        #print(dirs)
        #print(k)
        #print(k[0])
        if k[0] in l:
            l[k[0]] += 1
        else:
            l[k[0]] = 1
    print(l)
    for m in l:
        if l[m] >= i:
            i = l[m]
            n = m
    return i, n

def main():
    print(counter('.'))
        
if __name__ == '__main__':
    main()
