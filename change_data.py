from data_create import name_data, surname_data, phone_data, address_data

def change_data():
    var_fc = int(input(f"\n\nВ каком формате вы хотите изменить данные?\n\n"
                    f"1 вариант:\n\n"
                    f"Имя\n"
                    f"Фамилия\n"
                    f"Телефон\n"
                    f"Адрес\n\n"
                    f"2 вариант: \n\n"
                    f"Имя; Фамилия; Телефон; Адрес\n\n"
                    f"Выберите вариант: "))
    
    if var_fc == 1:
        with open('data_1.csv', 'r', encoding='utf-8') as data_1:
            data_1_read = data_1.readlines()
            data_1_list = []
            j = 0
            for i in range(len(data_1_read)):
                if data_1_read[i] == '\n' or i == len(data_1_read)-1:
                    data_1_list.append(''.join(data_1_read[j:i+1]))
                    j = i
            j = 0

            titles = ["Имя", "Фамилия", "Телефон", "Адрес"]
            data_1_list = ''.join(data_1_list)
            data_1_list = data_1_list.replace('\n\n', '').split('\n')
            data_for_change = []

            for i in range(len(data_1_list)):
                for j in range(len(titles)):
                    if j == (i % len(titles)):
                        data_for_change.append({titles[j]: data_1_list[i]})
            data_for_change = [data_for_change[i:i+len(titles)] for i in range(0, len(data_for_change), len(titles))]

            for i in range(len(data_for_change)):
                print(f"{i+1}.")
                for j in range(len(titles)):
                    print(f"{data_for_change[i][j][titles[j]]}")
                print()

        block_for_change = int(input("Выберите запись для изменения: "))

        while block_for_change not in range(1, len(data_for_change)+1):
            print("Такой записи не существует")
            block_for_change = int(input("Выберите запись для изменения: "))
        print("\nКакие данные вы хотите изменить?\n")
        
        for t in range(len(titles)):
            print(f"{t+1} {titles[t]}")
        print(f"{len(titles)+1} Все данные в этой записи\n")
        string_for_change = int(input("Выберите вариант: "))

        while string_for_change not in range(1, 6):
            print("Некорректный вариант")
            string_for_change = int(input("Выберите вариант: "))

        if string_for_change == 1:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: name_data()}
        elif string_for_change == 2:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: surname_data()}
        elif string_for_change == 3:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: phone_data()}
        elif string_for_change == 4:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: address_data()}
        elif string_for_change == 5:
            data_for_change[block_for_change-1][0] = {titles[0]: name_data()}
            data_for_change[block_for_change-1][1] = {titles[1]: surname_data()}
            data_for_change[block_for_change-1][2] = {titles[2]: phone_data()}
            data_for_change[block_for_change-1][3] = {titles[3]: address_data()}

        changed_data_for_write = []   
        for l in range(len(data_for_change)):
            for l2 in range(len(data_for_change[l])):
                changed_data_for_write.append(data_for_change[l][l2][titles[l2]])
        
        with open('data_1.csv', 'w', encoding='utf-8') as data_1:
            for w in range(len(changed_data_for_write)):
                if (w+1) % len(titles) == 0:
                    data_1.write(f"{changed_data_for_write[w]}\n"
                                 f"\n")
                else:
                    data_1.write(f"{changed_data_for_write[w]}\n")

    if var_fc == 2:
        with open('data_2.csv', 'r', encoding='utf-8') as data_2:
            data_2_read = data_2.readlines()
            data_2_list = ''.join(data_2_read)
            data_2_list = data_2_list.replace('\n\n', ';').replace('; ', ';').split(';')
            titles = ["Имя", "Фамилия", "Телефон", "Адрес"]
            data_for_change = []


            for i in range(len(data_2_list)):
                for j in range(len(titles)):
                    if data_2_list[i] == '':
                        break
                    if j == (i % len(titles)):
                        data_for_change.append({titles[j]: data_2_list[i]})
            data_for_change = [data_for_change[i:i+len(titles)] for i in range(0, len(data_for_change), len(titles))]

            for i in range(len(data_for_change)):
                print(f"{i+1}.")
                print(f"{data_for_change[i][0][titles[0]]}; {data_for_change[i][1][titles[1]]}; {data_for_change[i][2][titles[2]]}; {data_for_change[i][3][titles[3]]}")
                print()


        block_for_change = int(input("Выберите запись для изменения: "))

        while block_for_change not in range(1, len(data_for_change)+1):
            print("Такой записи не существует")
            block_for_change = int(input("Выберите запись для изменения: "))
        print("\nКакие данные вы хотите изменить?\n")
        
        for t in range(len(titles)):
            print(f"{t+1} {titles[t]}")
        print(f"{len(titles)+1} Все данные в этой записи\n")
        string_for_change = int(input("Выберите вариант: "))

        while string_for_change not in range(1, 6):
            print("Некорректный вариант")
            string_for_change = int(input("Выберите вариант: "))
        

        if string_for_change == 1:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: name_data()}
        elif string_for_change == 2:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: surname_data()}
        elif string_for_change == 3:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: phone_data()}
        elif string_for_change == 4:
            data_for_change[block_for_change-1][string_for_change-1] = {titles[string_for_change-1]: address_data()}
        elif string_for_change == 5:
            data_for_change[block_for_change-1][0] = {titles[0]: name_data()}
            data_for_change[block_for_change-1][1] = {titles[1]: surname_data()}
            data_for_change[block_for_change-1][2] = {titles[2]: phone_data()}
            data_for_change[block_for_change-1][3] = {titles[3]: address_data()}

        changed_data_for_write = []   
        for l in range(len(data_for_change)):
            for l2 in range(len(data_for_change[l])):
                changed_data_for_write.append(data_for_change[l][l2][titles[l2]])
        
        with open('data_2.csv', 'w', encoding='utf-8') as data_2:
            for w in range(len(changed_data_for_write)):
                if (w+1) % len(titles) == 0:
                    data_2.write(f"{changed_data_for_write[w]}\n"
                                 f"\n")
                else:
                    data_2.write(f"{changed_data_for_write[w]}; ")               