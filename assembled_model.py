

import pandas as pd
import numpy as np
import pickle

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


# объявляем функцию предсказания

def predict(sample):
    predictions = pred.predict(sample)
    
    pc = packer(predictions, carton)
    
    result = pc.pack()
    
    return result

