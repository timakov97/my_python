value = input("Введите порядковый номер элемента: ")
if value:
    num = int(value)
    if num == 3:
        print("Li")
    elif num == 25:
        print("Mn")
    elif num == 80:
        print("Hg")
    elif num == 17:
        print("Cl")
    else:
        print("Не знаю такого элемента...")
else:
    print ("Введите значение элемента!")
