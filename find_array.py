# coding=utf-8
from scipy import io
import numpy as np

# i=130000
alphabet_power = 65536


# Наивный алгоритм. Работает медленно

# def naive_find(data,fragm):
#
#     for i in range(0, data.shape[0] - fragm.shape[0]):
#
#         if np.array_equal(data[i:i+fragm.shape[0]],fragm):
#
#             print i
#             return i

# вычисление таблицы смещений
def calculate_offset(data):
    # алфавит в данном случае все натуральные числа до 2^8, т.к. числа не превышают этого значения.
    # мощность алфавита меняется в зависимости от порядка чисел во входных данных

    offset = []
    pattern_length = fragm.shape[0]

    for i in range(0, 2 * alphabet_power):
        offset.append(pattern_length)

    for j in range(0, pattern_length - 2):
        offset[alphabet_power + fragm[j]] = pattern_length - j - 1

    offset = np.array(offset)

    return offset

# для поиска используются алгоритм Бойера-Мура-Хорпсула
def boyer_mur_horpsul(data, fragm):

    i = fragm.shape[0] - 1
    while i < data.shape[0] - fragm.shape[0]:

        if data[i] == fragm[-1]:
            part_data = data[i - (fragm.shape[0] - 1):i + 1]


            if np.array_equal(part_data, fragm):

                return i-(fragm.shape[0]- 1)                            # возвращает индекс первого элемента

            else:
                for j in range(2, fragm.shape[0] - 1):

                    if part_data.tolist()[-j] != fragm.tolist()[-j]:    # в случае если элементы не совпадают, то индекс меняется в соответствии с таблицей смещения
                        i += offset[alphabet_power + data[i]]
                        break

        else:
            i += offset[alphabet_power + data[i]]                       # в случае если последний элемент не совпадают, то индекс меняется в соответствии с таблицей смещения

    return None


def max_matcher(all_data,fragm):

    return_data = all_data

    for data in all_data:

        if np.amax(data) < np.amax(fragm):
            return_data.remove(data)

    return return_data

matlab_data = io.loadmat('/home/alexandr/Dropbox/task2.mat')

data_1 = matlab_data['data_1'][0]
data_2 = matlab_data['data_2'][0]
data_3 = matlab_data['data_3'][0]

all_data = []
all_data.append(data_1)
all_data.append(data_2)
all_data.append(data_3)


fragm = matlab_data['fragm'][0]

# all_data = max_matcher(all_data,fragm)

offset = calculate_offset(fragm)



for index,data in enumerate(all_data):                      #поиск фрагмента

    if boyer_mur_horpsul(data,fragm)!=None:
        print(index)

