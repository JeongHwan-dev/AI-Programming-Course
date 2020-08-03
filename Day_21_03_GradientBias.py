# Day_21_03_GradientBias.py


def cost(x, y, w, b):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) ** 2
        c += loss

    return c / len(x)


def gradient_descent(x, y, w, b):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        loss = (hx - y[i]) * x[i]
        c += loss

    return c / len(x)


def show_gradient():
    x = [1, 2, 3]
    y = [1, 2, 3]

    w, b = 5, -3
    for i in range(10):
        c = cost(x, y, w=w, b=b)
        g = gradient_descent(x, y, w=w, b=b)
        w -= 0.1 * g
        print(i, c)

    # 문제
    # w가 1이 되는 코드로 수정하세요 (3가지)

    # 문제
    # x가 5와 7인 경우에 대해 예측하세요
    print('5 :', w * 5 + b)
    print('7 :', w * 7 + b)


show_gradient()
