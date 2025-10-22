#если леy строки нечетное число то вывести каждый 2 элемент в противном случае если там только числа найти частно еот деления на 10если там только буквы найти на каком месте а иначе напечатать я сддала лабу
string=input('enter a text: ')
if  len(string)%2==1:
    print(string[1:len(string):2])
else:
    if string.isdigit():
        print(int(string)/10)
    elif string.isalpha():
        print(string.find("a")+1)
        #print([i for i,c in enumerate(string) if c=="a"])
    else:
        print(" я сдала лабу!")

