day = int(input("Введите день вашего рождения (число): "))
month = int(input("Введите месяц вашего рождения (число): "))

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Твой знак зодиака: Овен")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Твой знак зодиака: Телец")
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Твой знак зодиака: Близнецы")
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("Твой знак зодиака: Рак")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Твой знак зодиака: Лев")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Твой знак зодиака: Дева")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Твой знак зодиака: Весы")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Твой знак зодиака: Скорпион")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Твой знак зодиака: Стрелец")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Твой знак зодиака: Козерог")
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Твой знак зодиака: Водолей")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Твой знак зодиака: Рыбы")
else:
    print("Проверьте правильность введенных данных")