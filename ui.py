from logger import input_data, print_data
from change_data import change_data
from delete_data import delete_data

def interface():
    print("Добрый день! Выберите действие: \n 1 - Запись данных \n 2 - Вывод данных \n 3 - Изменение данных \n 4 - Удаление данных")
    command = int(input())
    while command not in range(1, 5):
        print("Некорректная команда")
        command = int(input("Введите число: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()
