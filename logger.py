from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"\n\nВ каком формате записать данные?\n\n"
                    f"1 вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 вариант: \n\n"
                    f"{name}; {surname}; {phone}; {address}\n\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Некорректная команда")
        var = int(input("Введите число: "))

    if var == 1:
        with open('data_1.csv', 'a', encoding='utf-8') as data_1:
            data_1.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    if var == 2:
        with open('data_2.csv', 'a', encoding='utf-8') as data_2:
            data_2.write(f"{name}; {surname}; {phone}; {address}\n\n")

def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_1.csv', 'r', encoding='utf-8') as data_1:
        data_1_read = data_1.readlines()
        data_1_list = []
        j = 0
        for i in range(len(data_1_read)):
            if data_1_read[i] == '\n' or i == len(data_1_read)-1:
                data_1_list.append(''.join(data_1_read[j:i+1]))
                j = i
        print(''.join(data_1_list))
    print("Вывожу данные из 2 файла: \n")
    with open('data_2.csv', 'r', encoding='utf-8') as data_2:
        data_2_read = data_2.readlines()
        print(*data_2_read)
