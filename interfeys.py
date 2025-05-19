from laba import EncryptData, DecryptData
while True:
    print("Привіт! Ця програма зашифрує або розшифрує твій текс шифром Rabbit")
    data=input("Якщо тобі треба зашифрувати текс то натисни 1, якщо розшифрувати 2, або введи \"close\" щоби вийти: ")
    if data=="1":
        print("Добре, зараз зашифруємо ваші дані")
        name_file_key=input("Введіть ім'я файлу з ключем: ")
        name_file_vec=input("Введіть ім'я файлу з вектором: ")
        name_file_data=input("Введіть ім'я файлу з даними для шифрування: ")
        name_file_output=input("Введіть ім'я файлу для зашифрованих даних: ")
        with open(name_file_key, 'r') as file:
            key=''.join(file.read().split())
        with open(name_file_vec, 'r') as file:
            vec=''.join(file.read().split())
        with open(name_file_data, 'r') as file:
            text=''.join(file.read().split())
        with open(name_file_output, 'w') as file:
            file.write(EncryptData(key, vec, text))
    elif data=="2":
        print("Добре, зараз розшифруємо ваші дані")
        name_file_key=input("Введіть ім'я файлу з ключем: ")
        name_file_vec=input("Введіть ім'я файлу з вектором: ")
        name_file_data=input("Введіть ім'я файлу з даними для розшифрування: ")
        name_file_output=input("Введіть ім'я файлу для розшифрованих даних: ")
        with open(name_file_key, 'r') as file:
            key=''.join(file.read().split())
        with open(name_file_vec, 'r') as file:
            vec=''.join(file.read().split())
        with open(name_file_data, 'r') as file:
            text=''.join(file.read().split())
        with open(name_file_output, 'w') as file:
            file.write(DecryptData(key, vec, text))
    elif data.lower()=="close":
        break
