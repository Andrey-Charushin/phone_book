def delete_data():
    var_fd = int(input(f"\n\nИз списка какого формата вы хотите удалить данные?\n\n"
                    f"1 вариант:\n\n"
                    f"Имя\n"
                    f"Фамилия\n"
                    f"Телефон\n"
                    f"Адрес\n\n"
                    f"2 вариант: \n\n"
                    f"Имя; Фамилия; Телефон; Адрес\n\n"
                    f"Выберите вариант: "))
    
    if var_fd == 1:
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

        block_for_delete = int(input("Выберите запись для удаления: "))

        while block_for_delete not in range(1, len(data_for_change)+1):
            print("Такой записи не существует")
            block_for_delete = int(input("Выберите запись для удаления: "))

        changed_data_for_write = []   
        for l in range(0, block_for_delete-1):
            for l2 in range(len(data_for_change[l])):
                changed_data_for_write.append(data_for_change[l][l2][titles[l2]])
              
        for l in range(block_for_delete, len(data_for_change)):
            for l2 in range(len(data_for_change[l])):
                changed_data_for_write.append(data_for_change[l][l2][titles[l2]])
               
        with open('data_1.csv', 'w', encoding='utf-8') as data_1:
            for w in range(len(changed_data_for_write)):
                if (w+1) % len(titles) == 0:
                    data_1.write(f"{changed_data_for_write[w]}\n"
                                 f"\n")
                else:
                    data_1.write(f"{changed_data_for_write[w]}\n")
    
    if var_fd == 2:
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


        block_for_delete = int(input("Выберите запись для удаления: "))

        while block_for_delete not in range(1, len(data_for_change)+1):
            print("Такой записи не существует")
            block_for_delete = int(input("Выберите запись для удаления: "))

        changed_data_for_write = []   
        for l in range(0, block_for_delete-1):
            for l2 in range(len(data_for_change[l])):
                changed_data_for_write.append(data_for_change[l][l2][titles[l2]])
              
        for l in range(block_for_delete, len(data_for_change)):
            for l2 in range(len(data_for_change[l])):
                changed_data_for_write.append(data_for_change[l][l2][titles[l2]])
                
        with open('data_2.csv', 'w', encoding='utf-8') as data_2:
            for w in range(len(changed_data_for_write)):
                if (w+1) % len(titles) == 0:
                    data_2.write(f"{changed_data_for_write[w]}\n"
                                 f"\n")
                else:
                    data_2.write(f"{changed_data_for_write[w]}; ")