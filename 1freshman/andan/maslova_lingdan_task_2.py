def count(n):
    res = 1
    text = "Извините, вы ввели не натуральное число." 
    if n > 0:
        if int(n) == n:     
            for i in range (1, int(n)+1):
                res = i **(1/res)
        text = "Член данной последовательности под номером " + str(int(n)) + " равен " + str(res)
    return text

#я не знаю, необходима ли эта часть, но пусть будет
    
def main():
    print(count(float(input('Введите натуральное число: '))))
    
if __name__ == '__main__':
    main()
