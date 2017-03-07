#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:39:11 2017

@author: chosenone
"""

import tensorflow as tf
node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0,tf.float32)
print(node1,node2)


sess = tf.Session()
print(sess.run([node1,node2]))

node3 = tf.add(node1,node2)
print(node3)
print(sess.run(node3))


# placeholder

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a+b # short cut for tf.add(a,b)

add_and_triple = adder_node * 3

print(sess.run(adder_node,{a:3,b:4.5}))

print(sess.run(adder_node,{a:[1,2],b:[3,4]}))

print(sess.run(add_and_triple,{a:3,b:4.5}))




# linear model

W = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)

x = tf.placeholder(tf.float32)

linear_model = W * x + b

y = tf.placeholder(tf.float32)

squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)


# init all variables
init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model,{x:[1,2,3,4]}))
print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

fixW = tf.assign(W,[-1.])
fixb = tf.assign(b,[1.])

sess.run([fixW,fixb])

print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))



optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# reset values
sess.run(init)

for i in range(1000):
    sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
    
print 'should ~0:',sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]})    
print sess.run([W,b])






















 
    
    








































