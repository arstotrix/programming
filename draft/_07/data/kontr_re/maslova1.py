#вариант 1
with open ("Extinct_languages.tsv", encoding = "utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if(len(line) > 35):
            print(line)
