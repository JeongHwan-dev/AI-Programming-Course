# Day_17_01_LinearRegression.py
import tensorflow as tf

x = [1, 2, 3]
y = [1, 2, 3]

w = tf.Variable(5.0)
b = tf.Variable(-3.0)

# hx = wx + b

hx = tf.add(tf.multiply(w, x), b)

loss_i = tf.square(hx - y)
loss = tf.reduce_mean(loss_i)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(loss=loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer)

for i in range(10):
    sess.run(train)


sess.close()