# Day_25_03_CarEvaluation.py
import numpy as np
from sklearn import model_selection, preprocessing
import tensorflow as tf
import pandas as pd


# 문제 1
# car.data 파일을 읽어서
# x_train, x_test, y_train, y_test 데이터를 반환하는 함수를 만드세요

# 문제 2
# 높은 정확도를 갖는 모델을 만드세요


def get_data():
    names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'classes']
    car = pd.read_csv('data/car.data', header=None, names=names)
    car.info()

    enc = preprocessing.LabelEncoder()
    for col in car.columns:
        car[col] = enc.fit_transform(car[col])

    # buying   = enc.fit_transform(car.buying)
    # maint    = enc.fit_transform(car.maint)
    # doors    = enc.fit_transform(car.doors)
    # persons  = enc.fit_transform(car.persons)
    # lug_boot = enc.fit_transform(car.lug_boot)
    # safety   = enc.fit_transform(car.safety)
    # classes  = enc.fit_transform(car.classes)
    #
    # x = [buying, maint, doors, persons, lug_boot, safety]
    # x = np.transpose(x)
    #
    # y = classes
    # print(x.shape, y.shape)     # (1728, 6) (1728,)
    # print(y[:10])
    #
    # return model_selection.train_test_split(x, y, train_size=0.7)



get_data()
