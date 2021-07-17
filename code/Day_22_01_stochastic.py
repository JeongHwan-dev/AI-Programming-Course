# Day_22_01_stochastic.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 문제
# action.txt 파일을 읽어서 x, y 데이터를 반환하는 함수를 만드세요
def get_action_1():
    action = pd.read_csv('data/action.txt',
                         header=None,
                         names=['bias', 'feature1', 'feature2', 'label'])
    print(action)

    y = action.label.values
    print(y)

    action.drop(['label'], axis=1, inplace=True)
    x = action.values

    return x, y.reshape(-1, 1)


def get_action_2():
    action = np.loadtxt('data/action.txt', delimiter=',')
    # action = np.loadtxt('data/action.txt', delimiter=',', unpack=True)
    # print(action.shape)       # (100, 4)

    return action[:, :-1], action[:, -1:]


# x, y = get_action_1()
x, y = get_action_2()
print(x.shape, y.shape)         # (100, 3) (100, 1)

# 문제
# action.txt 파일을 그래프로 표시하세요
# for i in range(len(x)):
#     if y[i][0]:
#         plt.plot(x[i][1], x[i][2], 'ro')
#     else:
#         plt.plot(x[i][1], x[i][2], 'go')

for i in range(len(x)):
    _, x1, x2 = x[i]
    plt.plot(x1, x2, 'ro' if y[i][0] else 'gx')
    # if y[i][0]:
    #     plt.plot(x1, x2, 'ro')
    # else:
    #     plt.plot(x1, x2, 'go')

plt.show()








