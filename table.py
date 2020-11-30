import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def table_info(table):
    print("--------------------------------")
    print("Кол-во строк и столбцов в таблице: ")
    print(table.shape)
    print("Тип данных: ")
    print(table.dtypes)
    print("Наименования столбцов: ")
    print(table.columns.ravel())
    print("--------------------------------")


filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    print("Указанный файл существует")
else:
    print("Указанный файл не существует, попробуйте снова")
    exit()
# C:\Users\aaa\PycharmProjects\lab1\covid_17.11.20.xlsx
xl = pd.ExcelFile(filename)
table = xl.parse('Лист 1')
pd.set_option('display.max_rows', None, 'display.max_columns', None)
desired_width = 320
pd.set_option('display.width', desired_width)
# Информация о таблице
table_info(table)
# Информация по региону
print("--------------------------------")
region = input("Введите город/регион в котором хотите узнать статистику: ")
print(table.loc[table['ГОРОД/РЕГИОН '] == region])
print("--------------------------------")
var = int(input("Введите число, чтобы узнать, в каких регионах число заболевших превышает введенное: "))
print(table[table['ЧИСЛО ЗАБОЛЕВШИХ'] > var][['ГОРОД/РЕГИОН ', 'ЧИСЛО ЗАБОЛЕВШИХ']])
print("--------------------------------")

# Сортировка по параметрам
table.sort_values(by=['ЧИСЛО ВЫЗДОРОВЕВШИХ'], ascending=[False], inplace=True)
table_sort_by_recovered = table.copy()
table.sort_values(by=['ЧИСЛО УМЕРШИХ'], ascending=[False], inplace=True)
table_sort_by_dead = table.copy()

# Определение топ 5 наибольших и наименьших значений по различным параметрам
h1 = table.nlargest(5, ['ЧИСЛО ЗАБОЛЕВШИХ'])[['ГОРОД/РЕГИОН ', 'ЧИСЛО ЗАБОЛЕВШИХ']]
h2 = table_sort_by_recovered.nlargest(5, ['ЧИСЛО ВЫЗДОРОВЕВШИХ'])[['ГОРОД/РЕГИОН ', 'ЧИСЛО ВЫЗДОРОВЕВШИХ']]
h3 = table_sort_by_dead.nlargest(5, ['ЧИСЛО УМЕРШИХ'])[['ГОРОД/РЕГИОН ', 'ЧИСЛО УМЕРШИХ']]
h4 = table.nsmallest(5, ['ЧИСЛО ЗАБОЛЕВШИХ'])[['ГОРОД/РЕГИОН ', 'ЧИСЛО ЗАБОЛЕВШИХ']]
h5 = table_sort_by_recovered.nsmallest(5, ['ЧИСЛО ВЫЗДОРОВЕВШИХ'])[['ГОРОД/РЕГИОН ', 'ЧИСЛО ВЫЗДОРОВЕВШИХ']]
h6 = table_sort_by_dead.nsmallest(5, ['ЧИСЛО УМЕРШИХ'])[['ГОРОД/РЕГИОН ', 'ЧИСЛО УМЕРШИХ']]

# Построение гистограммы ранее полученных данных
plt.figure(figsize=(35, 20))
plt.subplot(2, 3, 1)
plt.title("Топ 5 наибольших по заболеваниям")
plt.bar(h1['ГОРОД/РЕГИОН '], h1['ЧИСЛО ЗАБОЛЕВШИХ'])
plt.subplot(2, 3, 2)
plt.title("Топ 5 наибольших по выздоровлениям")
plt.bar(h2['ГОРОД/РЕГИОН '], h2['ЧИСЛО ВЫЗДОРОВЕВШИХ'])
plt.subplot(2, 3, 3)
plt.title("Топ 5 наибольших по числу умерших")
plt.bar(h3['ГОРОД/РЕГИОН '], h3['ЧИСЛО УМЕРШИХ'])
plt.subplot(2, 3, 4)
plt.title("Топ 5 наименьших по заболеваниям")
plt.bar(h4['ГОРОД/РЕГИОН '], h4['ЧИСЛО ЗАБОЛЕВШИХ'])
plt.subplot(2, 3, 5)
plt.title("Топ 5 наименьших по выздоровлениям")
plt.bar(h5['ГОРОД/РЕГИОН '], h5['ЧИСЛО ВЫЗДОРОВЕВШИХ'])
plt.subplot(2, 3, 6)
plt.title("Топ 5 наименьших по числу умерших")
plt.bar(h6['ГОРОД/РЕГИОН '], h6['ЧИСЛО УМЕРШИХ'])
plt.show()
