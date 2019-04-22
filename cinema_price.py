film = input ("Выберите фильм: \n 1 - 'Пятница'\n 2 - 'Чемпионы'\n 3 - 'Пернатая банда'\n")
date = input ("Выберите дату: \n 1 - Сегодня\n 2 - Завтра \n")
if date == '1':
    date_disc = 0.95
elif date == '2':
    date_disc = 1
if film == '1':
    time = input ("Выберите время: \n 1 - 12 часов \n 2 - 16 часов \n 3 - 20 часов \n")
elif film == '2':
    time = input ("Выберите время: \n 1 - 10 часов \n 2 - 13 часов \n 3 - 16 часов \n")
elif film == '3':
    time = input ("Выберите время: \n 1 - 10 часов \n 2 - 14 часов \n 3 - 18 часов \n")
num = int(input("Укажите число билетов \n"))
if num >= 20:
    num_disc = 0.8
else:
    num_disc = 1
if (film == '1' and time == '1'):
    print ("Стоимость билетов: ", 250 * num * date_disc * num_disc, "рублей.")
elif (film == '1' and time == '2'):
    print ("Стоимость билетов: ", 350 * num * date_disc * num_disc, "рублей.")
elif (film == '1' and time == '3'):
    print ("Стоимость билетов: ", 450 * num * date_disc * num_disc, "рублей.")
elif (film == '2' and time == '1'):
    print ("Стоимость билетов: ", 250 * num * date_disc * num_disc, "рублей.")
elif (film == '2' and time == '2'):
    print ("Стоимость билетов: ", 350 * num * date_disc * num_disc, "рублей.")
elif (film == '2' and time == '3'):
    print ("Стоимость билетов: ", 350 * num * date_disc * num_disc, "рублей.")
elif (film == '3' and time == '1'):
    print ("Стоимость билетов: ", 350 * num * date_disc * num_disc, "рублей.")
elif (film == '3' and time == '2'):
    print ("Стоимость билетов: ", 450 * num * date_disc * num_disc, "рублей.")
elif (film == '3' and time == '3'):
    print ("Стоимость билетов: ", 450 * num * date_disc * num_disc, "рублей.")
