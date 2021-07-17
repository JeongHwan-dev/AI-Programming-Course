# Day_24_02_California.py
import pandas as pd
from sklearn import preprocessing, model_selection, datasets
import numpy as np
import tensorflow as tf


# 문제
# 캘리포니아 주택가격 데이터로부터
# x_train, x_test, y_train, y_test를 반환하는 함수를 만드세요 (7:3 분할)

# 문제 2
# 학습하고 정확도를 구하세요 (미니배치/앙상블 금지)


def get_data():
    x, y = datasets.fetch_california_housing(return_X_y=True)
    print(x.shape, y.shape)         # (20640, 8) (20640,)
    print(y[:5])                    # [4.526 3.585 3.521 3.413 3.422]
    print(x.dtype, y.dtype)         # float64 float64

    # y = y.reshape(-1, 1)            # (20640, 1)
    # print(y.shape)

    return model_selection.train_test_split(x, y, train_size=0.7)


def model_california():
    x_train, x_test, y_train, y_test = get_data()
    print(x_train.shape, x_test.shape)  # (14447, 8) (6193, 8)
    print(y_train.shape, y_test.shape)  # (14447,) (6193,)

    w = tf.Variable(tf.random_uniform([x_train.shape[1], 1]))
    ph_x = tf.placeholder(tf.float32)

    # (506, 1) = (506, 13) @ (13, 1)
    hx = tf.matmul(ph_x, w)

    loss_i = (hx - y_train) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.001)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train, {ph_x: x_train})
        print(i, sess.run(loss, {ph_x: x_train}))

    preds = sess.run(hx, {ph_x: x_test})
    print(preds.shape)

    preds_1 = preds.reshape(-1)
    ytest_1 = y_test.reshape(-1)

    print(preds_1[:3])
    print(ytest_1[:3])

    diff = preds_1 - ytest_1
    print(diff[:3])

    diff_abs = np.abs(diff)
    print(diff_abs[:3])

    avg = np.mean(diff_abs)
    print('오차 평균 :', avg)
    print('오차 평균 : {}달러'.format(int(avg * 1000)))
    sess.close()


model_california()



