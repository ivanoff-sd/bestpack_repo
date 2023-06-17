#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import pickle
import json
# импорт кастомных классов
from class_predictor import predictor
from class_packer import packer

#
#
# ВНИМАНИЕ! ВНИМАНИЕ!!!
# Прошу исправить адреса файлов на актуальные!
carton = pd.read_csv('carton_full_features.csv')
sku = pd.read_csv('full_sku_data.csv')
#
#
#
#
#

# откроем модели
with open('model_big.pcl', 'rb') as f:

    model_large = pickle.load(f)
    
with open('model_small.pcl', 'rb') as f:

    model_small = pickle.load(f)
    
    
# создаем экземпляр класса predictor

pred = predictor(model_large=model_large, model_small=model_small, sku=sku, carton=carton)


#объявляем функцию предсказания

# переводим ввод из подаваемого формата в список

def predict(in_put):
    
    try:    
        in_put = json.loads(in_put)
    except:
        pass
    
    sample = []
    for n in range(0, len(in_put)):
        list_item = [in_put[n]['sku']]* in_put[n]['count']
        sample.extend(list_item)

    
#def predict(sample): 
    
    
    
    predictions = pred.predict(sample)

    pc = packer(predictions, carton)

    
    result = pc.pack()
    
    dict_list = []

    
    
    
    # переводим вывод в потребный список словарей
    for row in result.index:
        dictionary = {}

        dictionary['carton'] = result.loc[row, 'box']
        series = pd.Series(result.loc[row, 'goods']).value_counts()
        list_items = []
        for n in series.index: 

            list_items.append({'sku':{'sku': n}, 'amount': series[n]})
        dictionary['skus'] = list_items
        dict_list.append(dictionary)
    
    return dict_list

