#coding:utf-8
import tensorflow as tf

x=tf.constant([[1.0,2.0]])
w=tf.vari

y=tf.matmul(x,w)
print(y)

with tf.Session() as sess:
    print(sess.run(y))