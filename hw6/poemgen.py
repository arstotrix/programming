# coding=utf-8
import random
# Эта программа генерирует стихотворение с соблюдением метрической схемы - трехстопный анапест

def imperative():
    # эта функция возвращает случайный глагол в повелительном наклонении; у неё нет аргументов
    # чтобы получился хороший анапест, нужно подобрать глаголы с ударением на третий слог
    imperative = ["прокати", "уходи", "не спеши", "погоди", "подожди", "позвони", "убегай", "не плошай", "подержи"]
    return random.choice(imperative)

def verb():
    # эта функция возвращает случайный глагол мн.ч.; у неё нет аргументов
    # чтобы получился хороший анапест, нужно подобрать глаголы с ударением на третий слог
    plural_verbs = ["привезут", "принесли", "принесут", "пожуют", "погрызут", "приплетут", "приведут", "привели"]
    return random.choice(plural_verbs)

def noun_phrase():
    # эта функция возвращает случайное сочетание из двух слов:
    # первое - клитика (короткое односложное безударное слово)
    clitics = ["по", "ни", "на", "хоть", "лишь", "вот", "не", "от", "за", "пусть"]
    clitic = random.choice(clitics)
    # второе - какое-то двусложное слово с ударением на второй слог
    words2 = ["себе", "тебе", "земля", "игра", "звезда", "мороз", "ответ", "превед", "футбол", "печаль", "бокал"]
    noun = random.choice(words2)
    return clitic + ' ' + noun

def noun(number):
    # эта функция возвращает случайное существительное; у неё есть один аргумент - число существительного
    # чтобы получился хороший анапест, нужно подобрать слова с ударением на третий слог
    singular_nouns = ["монолог", "коридор", "почему", "потому", "отчего", "каратэ", "кабарэ", "курага", "кандидат"]
    plural_nouns = ["малыши", "рукава", "камыши", "табуны", "рюкзаки", "пиджаки", "пацаны", "чуваки"]
    # мы ожидаем, что функция будет получать в качестве аргумента либо строку 's' - для сущ. ед.ч.
    if number == 's':
        return random.choice(singular_nouns)
    # либо любую другую строку - для сущ. мн.ч.
    return random.choice(plural_nouns)

def punctuation():
    # эта функция возвращает случайный знак препинания из небольшого списка; у неё нет аргументов
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def verse1():
    # эта функция собирает строчку из сущ.мн.ч., глагола, еще одного сущ.мн.ч. и знака препинания
    # например "малыши пожуют камыши!"
    return noun('pl') + ' ' + verb() + ' ' + noun('pl') + punctuation()

def verse2():
    # эта функция собирает строчку из глаг.повел.накл., сущ.ед.ч, сочетания клитики с каким-то словом и знака препинания
    # например "не плошай курага хоть печаль."
    return imperative() + ' ' + noun('s') + ' ' + noun_phrase() + punctuation()

def verse3():
    # эта функция собирает строчку из сочетания клитики с каким-то словом, глагола, сущ.мн.ч. и знака препинания
    # например "на тебе принесут пиджаки."
    return noun_phrase() + ' ' + verb() + ' ' + noun('pl') + punctuation()


def make_verse():
    # эта функция выбирает случайный номер из 1,2,3 и возвращает соответствующую строчку
    verse = random.choice([1,2,3])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()

# тут начинается основной код. 
# Он распечатывает 4 случайные строчки, чтобы получилась строфа. 
for n in range(4):
    print(make_verse())
