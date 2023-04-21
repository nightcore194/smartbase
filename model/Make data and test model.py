# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:10:55 2023

@author: 22080
"""

import pandas as pd
import numpy as np
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
from work_functions import DataFromTxt

def GenerateTrainTestData(InsertDataFrame, need_save=True):
    '''
    Разделим файл с данными Kaggle_titanic_all.xlsx на:
        * Данные. на которых будет обучаться модель (train, valid)
        * Данные, на которых будет предсказываться класс (test)
        * также для проверки предсказаний отдельно выгрузим ответы (test_Y)
    
    Parameters
    ----------
    InsertDataFrame : pandas.DataFrame.
    need_save : bool, optional
        нужно ли сохранять данные в файлы или просто передадим их для обучения модели. The default is True.

    Returns
    -------
    train : pandas.DataFrame для тренировки модели.
    test : pandas.DataFrame для предсказания класса.
    test_Y : pandas.DataFrame с ответами на предсказания класса.
    '''
    
    # Поменяем 'PassengerId' на '№ЭЧ', добавим номера ВК и СИОМ для соответствия реальной задаче
    #print('GenerateTrainTestData: InsertDataFrame shape', InsertDataFrame.shape)
    func_df = InsertDataFrame.copy()
    func_df.rename(columns={'PassengerId':'№ЭЧ'}, inplace=True)
    func_df['№ЭЧ'] = func_df['№ЭЧ'] * 10
    func_df['№ЭЧ'] = func_df['№ЭЧ'].astype(str)
    func_df['№ВК'] = func_df['№ЭЧ'].str[0]
    func_df['№СИОМ'] = func_df['№ЭЧ'].str[1:]
    #print('GenerateTrainTestData: func_df shape', func_df.shape)
    
    # Поменяем целевую переменную 'Survived' на 'Класс_ЭЧ'
    func_df.rename(columns={'Survived':'Класс_ЭЧ'}, inplace=True)
    
    train, test = train_test_split(func_df, test_size=0.2, random_state=42, stratify=func_df['Класс_ЭЧ'])
    
    test_Y = test[['№ЭЧ','Класс_ЭЧ']]
    
    test.drop(columns=['Класс_ЭЧ'], inplace=True)
    
    if need_save:
        train.to_csv('./data_input_make_model/train.csv')
        test.to_csv('./data_input_prediction/test.csv')
        test_Y.to_csv('./data_input_prediction/test_Y.csv')
    
    return train, test, test_Y


def MakeModel(InsertDataFrame):
    '''
    На основании входящих тренировочных данных и жёстко забитых параметров 
    создадим и сохраним модель машинного обучения

    Parameters
    ----------
    InsertDataFrame : pandas.DataFrame с тренировочными данными

    Returns
    -------
    model : catboost.model.

    '''
    
    X = InsertDataFrame.copy()
      
    target_col = 'Класс_ЭЧ'
    cat_features = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
    selected_features = DataFromTxt('selected_features.txt')
    #selected_features = [i for i in X.columns.tolist() if i not in [target_col]]
    
    # предобработка
    X[cat_features] = X[cat_features].replace(to_replace=[None], value=np.nan).fillna('gap').astype(str).astype('category')


    # Выборки для моедли
    train, valid = train_test_split(X, test_size=0.2, random_state=42, stratify=X['Класс_ЭЧ'])
    #valid, test = train_test_split(valid, test_size=0.5, random_state=42, stratify=valid['Класс ЭЧ'])
    
    train_pool = Pool(train[selected_features].values, train[target_col], cat_features=[selected_features.index(i) for i in cat_features if i in selected_features])
    valid_pool = Pool(valid[selected_features].values, valid[target_col], cat_features=[selected_features.index(i) for i in cat_features if i in selected_features])
    #test_pool = Pool(test[selected_features].values, test[target_col], cat_features=[selected_features.index(i) for i in cat_features if i in selected_features])
    
    model = CatBoostClassifier(iterations=5000, random_seed=0, learning_rate=0.01)
    
    model.fit(train_pool,
    eval_set=valid_pool,early_stopping_rounds=50,plot =True, logging_level='Silent')
    
    model.save_model('classifier.bin')
    print('model.best_score_:/n', model.best_score_)
    
    return model
    
if __name__ == "__main__":
    # Читаем исходный Kaggle Titanic файл https://www.kaggle.com/c/titanic/data
    X = pd.read_csv("./data_input_make_model/Kaggle_titanic_all.csv")
    
    # Делим на выборки: 
    # * Для обучения модели (train) 
    # * Для предсказания на сервере (test). 
    # * Правильные ответы предсказания (test_Y)
    train, test, test_Y = GenerateTrainTestData(X, need_save=True)
    # Создаём и сохраняем модель
    MakeModel(train)
