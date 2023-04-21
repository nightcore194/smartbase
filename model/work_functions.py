# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:31:51 2023

@author: 22080
"""
# Функции для работы тестового сервера (для примера импорта функций)

def DataFromTxt(path_to_txt):
    '''
    Загрузка данных из блокнота

    Parameters
    ----------
    path_to_txt : [string] путь к файлу.

    Returns
    -------
    list_out : [list] список того, что в файле.

    '''

    with open(f'{path_to_txt}', 'r', encoding='utf-8') as f:
        list_out = []
        for line in f:
            list_out.append(line.replace('\n', ''))
        return list_out