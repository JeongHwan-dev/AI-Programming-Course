# Day_18_01_MultipleRegression.py
import tensorflow as tf


# 문제
# 피처를 두 개로 늘리세요(공부한 시간, 출석한 일수)
def multiple_regression_1():
    #       1         1        0
    # hx = w1 * x1 + w2 * x2 + b
    #  y = x1 + x2
    x1 = [1, 0, 3, 0, 5]        # 공부한 시간
    x2 = [0, 2, 0, 4, 0]        # 출석한 일수
    y = [1, 2, 3, 4, 5]         # 성적

    w1 = tf.Variable(tf.random_uniform([1]))
    w2 = tf.Variable(tf.random_uniform([1]))
    b = tf.Variable(tf.random_uniform([1]))

    hx = w1 * x1 + w2 * x2 + b

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    sess.close()


# 문제
# x1과 x2를 변수 1개로 만드세요
def multiple_regression_2():
    x = [[1, 0, 3, 0, 5],       # 공부한 시간
         [0, 2, 0, 4, 0]]       # 출석한 일수
    y = [1, 2, 3, 4, 5]         # 성적

    w = tf.Variable(tf.random_uniform([2]))
    b = tf.Variable(tf.random_uniform([1]))

    hx = w[0] * x[0] + w[1] * x[1] + b

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    sess.close()


# 문제
# bias를 없애보세요
def multiple_regression_3():
    # x = [[1, 0, 3, 0, 5],       # 공부한 시간
    #      [0, 2, 0, 4, 0],
    #      [1, 1, 1, 1, 1]]       # 출석한 일수
    x = [[1, 0, 3, 0, 5],       # 공부한 시간
         [1, 1, 1, 1, 1],
         [0, 2, 0, 4, 0]]       # 출석한 일수
    x = [[1, 1, 1, 1, 1],
         [1, 0, 3, 0, 5],       # 공부한 시간
         [0, 2, 0, 4, 0]]       # 출석한 일수
    y = [1, 2, 3, 4, 5]         # 성적

    w = tf.Variable(tf.random_uniform([3]))
    # b = tf.Variable(tf.random_uniform([1]))

    # hx = w[0] * x[0] + w[1] * x[1] + b
    # hx = w[0] * x[0] + w[1] * x[1] + w[2]
    # hx = w[0] * x[0] + w[1] * x[1] + w[2] * 1
    hx = w[0] * x[0] + w[1] * x[1] + w[2] * x[2]

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    # print(sess.run(w))
    sess.close()


# 문제
# hx 연산을 행렬 곱셈으로 바꾸세요. (ft.matmul)

def multiple_regression_4():
    x = [[1., 1., 1., 1., 1.],
         [1., 0., 3., 0., 5.],       # 공부한 시간
         [0., 2., 0., 4., 0.]]       # 출석한 일수
    y = [1, 2, 3, 4, 5]         # 성적

    w = tf.Variable(tf.random_uniform([3]))

    # hx = w[0] * x[0] + w[1] * x[1] + w[2] * x[2]
    # hx = w @ x
    # () = (1, 3) @ (3, 5)
    hx = tf.matmul(w, x)

    loss_i = (hx - y) ** 2
    loss = tf.reduce_mean(loss_i)

    optimizer = tf.train.GradientDescentOptimizer(0.1)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(10):
        sess.run(train)
        print(i, sess.run(loss))

    sess.close()




# multiple_regression_1()
# multiple_regression_2()
# multiple_regression_3()
multiple_regression_4()



