# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:17:58 2023

@author: 22080
"""
import pandas as pd
import numpy as np
#import copy
import datetime
from catboost import CatBoostClassifier, Pool
from server.model.work_functions import DataFromTxt

def RawData(Path_to_file):
    '''
    Получение данных любым способом. В примере - чтение из экселя
    
    Out: объект типа pandas.dataframe [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html]
    '''
    
    return pd.read_csv(filepath_or_buffer=Path_to_file, sep=';')#, index_col=False).drop('Unnamed: 0', axis=1) # , index_col=False)


def PredictionClassification(InsertCombinedDataFrame, selected_features, model_path, need_save=True):
    '''
    1. Получить данные, которые предсказывать
    2. Прописанная в функции предобработка
    3. Загрузить список признаков для выбора
    4. Загрузить модель
    5. Засунуть часть данных (выбранную по списку признаков) в моель
    6. Получить таблицу=датафрейм и выдать как результат работы функции
    Каждой строке исходного датаферйма поставить класс (Y) на основании загруженной модели
    
    In: 
    InsertCombinedDataFrame: pandas.DataFrame. Данные, на основании которых будем предсказывать
    selected_features: [txt]. Признаки, которые берём для предсказания из всех признаков, которые есть в данных
    model_path = [string] or  [python.Path.Path] - путь для загрузки модели.
    
    Out:
    df_pred: pandas.DataFrame с id объектов и их соответствующим предсказанным классом
        
    Example кривой:
    Model: Y = X1
    In: | X1 |
        | 1 |
        | 0 |
    Out: | X1 | Y |
        | 1 | 1 |
        | 0 | 0 |
    
    '''
    X = InsertCombinedDataFrame.copy()
    
    # предобработка
    #target_col = 'Класс_ЭЧ' # 'Survived'
    cat_features = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
    #selected_features = DataFromTxt('selected_features.txt')
    #selected_features = [i for i in X.columns.tolist() if i not in [target_col]]
    X[cat_features] = X[cat_features].replace(to_replace=[None], value=np.nan).fillna('gap').astype(str).astype('category')

    
    #test_pool = Pool(test[selected_features].values, test[target_col],cat_features=[selected_features.index(i)  for i in cat_features if i in selected_features])
    test_pool = Pool(X[selected_features].values, cat_features=[selected_features.index(i)  for i in cat_features if i in selected_features])
    
    model_work = CatBoostClassifier()
    model_work.load_model('classifier.bin')
    pred = model_work.predict(test_pool)
    
    #df_pred = pd.DataFrame({'№ЭЧ':X['№ЭЧ'], 'pred':pred}).sort_values(['pred']).reset_index(drop=True)
    df_pred = pd.DataFrame({'№ЭЧ':X['№ЭЧ'], '№ВК':X['№ВК'], '№СИОМ':X['№СИОМ'], 'pred':pred}).reset_index(drop=True)
    
    curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    if need_save:
        df_pred.to_excel('./data_output/pred {}.xlsx'.format(curr_time))
       
    return df_pred



def MainPipeline(path_data, path_selected_features, model_path, model_type):
    '''
    

    Parameters
    ----------
    path_data : [string] 
        путь к файлу с данными. которые предсказывать
    path_selected_features : [string]
        путь к файлу с признаками, которые берём из всех тек, которые есть в данных.
    model_path : [string]
        путь к сохранённой моедели.
    model_type : [stirng]
        тип модели (есть в рабочей версии).

    Returns
    -------
    df_pred : [pandas.DataFrame] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
        таблица с поставленными классами данным.

    '''
    # Загрузка данных
    X_orig = RawData(path_data) # [pandas.DataFrame]
    selected_features = DataFromTxt(path_selected_features) # [list]

    # Предсказание классов для всех строк
    if model_type == 'classification':
        df_pred = PredictionClassification(X_orig, selected_features, model_path, need_save=False)
        
        return df_pred # [pandas.DataFrame]
    elif model_type == 'regression':
        return 'регрессия тут не реализована'


if __name__ == "__main__":
    
    
    
    df_pred = MainPipeline(path_data=r"data_input_prediction/test.csv"
                          ,path_selected_features='selected_features.txt'
                          , model_path ='classifier.bin'
                          ,model_type='classification')
    
    '''
    Проверка точности. Не нужна в реальной задаче, так как там не ответов с которыми сравнивать
    df_answers = pd.read_csv(r"./data_input_prediction/test_Y.csv") # Ответы
    df_acc = pd.merge(left=df_answers,
                      right=df_pred,
                      left_on='№ЭЧ',
                      right_on='№ЭЧ',
                      how='inner')
    
    model_y = df_acc['Класс_ЭЧ'] # 'Survived'
    pred = df_acc['pred']
    
    test_pred = pd.DataFrame({'test':model_y, 'pred':pred}).sort_values(['test']).reset_index(drop=True)
    test_pred.columns=['Значение параметра из тестовой выборки', 'Прогноз модели']

    test_pred['Счёт'] = 1
    #test_pred.groupby(['Значение параметра из тестовой выборки', 'Прогноз модели']).count()
    
    # Подсчёт доли полных совпадений
    exact_pred_sum = 0
    for value in test_pred['Значение параметра из тестовой выборки'].unique():
        temp_df = test_pred[test_pred['Значение параметра из тестовой выборки'] == value]
        exact_pred_sum += temp_df[temp_df['Прогноз модели'] == value].shape[0]
    
    print('Доля полных совпадений:', round((exact_pred_sum / test_pred.shape[0]),2))
    Конец проверки точности
    '''
    
    # Если хочется вывод в json, то https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html
    #orient: str; default is ‘columns’; allowed values are: {‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’}
    #df_pred = df_pred.to_json(orient='columns')
    
    #print(df_pred)    
    