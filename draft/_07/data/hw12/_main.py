# выводит все файлы или папки, которые она нашла
import os
import re
i = 0
fnames = os.listdir()
for fname in fnames:
    if os.path.isfile(fname):
        j = 0
        print(fname.split('.')[0])
    else:
        print(fname)
        if re.search('\d', fname) != None:
            i += 1
print('в данной директории', i, 'папок с цифрами')
