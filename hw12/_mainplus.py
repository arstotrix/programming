# выводит только те, которые удовлетворяют условию
import os
import re
i = 0
fnames = os.listdir()
for fname in fnames:
    if os.path.isdir(fname):
       if re.search('\d', fname) != None:
            i += 1
            print(fname)
print('в данной директории', i, 'папок с цифрами')
