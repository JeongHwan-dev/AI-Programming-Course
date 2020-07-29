# Day_16_01_DL_basic.py
# import tensorflow as tf         # 1.14.0
import matplotlib.pyplot as plt


def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) ** 2
        c += loss

    return c / len(x)


def gradient_descent(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) * x[i]
        c += loss

    return c / len(x)


def show_cost():
    # hx = wx + b
    #      1    0
    #  y = ax + b
    #  y = x
    x = [1, 2, 3]
    y = [1, 2, 3]

    print(cost(x, y, w=0))
    print(cost(x, y, w=1))
    print(cost(x, y, w=2))
    print('-' * 30)

    for i in range(-30, 50):
        w = i / 10
        c = cost(x, y, w)
        print(w, c)

        plt.plot(w, c, 'ro')
    plt.show()


def show_gradient():
    x = [1, 2, 3]
    y = [1, 2, 3]

    w = 5
    for i in range(100):
        g = gradient_descent(x, y, w)
        w -= 0.1 * g
        print(i, w)

    # 문제
    # x가 5와 7인 경우에 대해 예측하세요.
    print('5: ', w * 5)
    print('7: ', w * 7)


# 문제
# w가 1이 되는 코드로 수정하세요.
def show_gradient2():
    x = [1, 2, 3]
    y = [1, 2, 3]

    w = 1
    for i in range(100):
        g = gradient_descent(x, y, w)
        w -= 0.1 * g
        print(i, w)


# show_cost()
show_gradient()
# show_gradient2()


# 미분 : 기울기, 순간 변화량, x가 y에 영향을 주는 정도.
#       x가 1만큼 변할 때 y가 변하는 만큼.

# y = 3             3=1, 3=2, 3=3                           => 0
# y = x             1=1, 2=2, 3=3                           => 1
# y = 2x            2=1, 4=2, 6=3                           => 2
# y = (x+1)         2=1, 3=2, 4=3                           => 1
# y = xz                                                    => z, x

# y = x^2           1=1, 4=2, 9=3
#                   2 * x^(2-1) = 2x
#                   2 * x^(2-1) * x미분 = 2x
# y = (x+1)^2       2 * (x+1)^(2-1) = 2(x+1) = 2x+2
#                   2 * (x+1)^(2-1) * (x+1)미분 = 2x+2






