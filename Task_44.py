
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
import numpy as np


# Создаем список с элементами 'robot' повторенными 10 раз и 'human' повторенными 10 раз
lst = ['robot'] * 10
lst += ['human'] * 10

# Перемешиваем список случайным образом
random.shuffle(lst)

# Создаем DataFrame с одной колонкой 'whoAmI' и заполняем данными из списка lst
data = pd.DataFrame({'whoAmI': lst})


# Создаем функцию для преобразования категориальной переменной в one hot представление

def one_hot_encode(data, column_name, categories):
    encoded_data = pd.DataFrame()

# Для каждой категории создаем новую колонку и заполняем ее значениями 0 или 1

    for category in categories:
        encoded_data[column_name + '_' + category] = np.where(data[column_name] == category, 1, 0)

    return encoded_data


# Выполняем преобразование переменной 'whoAmI' в one hot представление

one_hot_data = one_hot_encode(data, 'whoAmI', ['robot', 'human'])

# Выводим первые несколько строк преобразованного DataFrame

print(one_hot_data.head())