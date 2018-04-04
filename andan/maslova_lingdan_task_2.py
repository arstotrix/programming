def count(n):
    res = 1
    text = "Извините, вы ввели ноль"
    if n > 0:
        for i in range (1, n+1):
            res = i **(1/res)
            #print(res)
        text = "Член данной последовательности под номером " + str(n) + " равен " + str(res)
    return text

#я не знаю, необходима ли эта часть, но пусть будет
    
def main():
    print(count(int(input('Введите целое число: '))))
    
if __name__ == '__main__':
    main()
