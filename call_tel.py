code = int((input("Введите код города: ")))
dur = float((input("Введите длительность переговоров в минутах: ")))
if code == 343:
    print ("Стоимость переговоров: ", dur * 15, "рублей")
elif code == 381:
    print ("Стоимость переговоров: ", dur * 18, "рублей")
elif code == 473:
    print ("Стоимость переговоров: ", dur * 13, "рублей")
elif code == 485:
    print ("Стоимость переговоров: ", dur * 11, "рублей")
else:
    print ("Неизвестный код города :(")
