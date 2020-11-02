import os
import re

filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    print("Указанный файл существует")
    with open(filename, "r") as myfile:
        valid = list()
        for line in myfile:
            result = re.findall(r'(?:\d|\+\d)(?:\(|-)\d{3}(?:\)|-)\d{3}-\d{2}-\d{2}', line)
            if len(result) != 0:
                valid.extend(result)
    key = input("Посмотреть предварительный список валидных номеров? ")
    if key.lower() == "да":
          for i in valid:
             print(i)
    newfilename = input("Введите имя файла, в который желаете сохранить данные? ")
    with open(newfilename, "w") as newfile:
        for i in valid:
            newfile.write(i + "\n")
    print("Работа программы завершена")
else:
    print("Файл не существует")
