#Cod from the demo at :https://www.tensorflow.org/versions/r0.11/tutorials/mnist/pros/index.html#deep-mnist-for-experts
#This is going to be a logistic regression classifier

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
sess = tf.InteractiveSession() #This is to allow us to run an interactive session of TF



x = tf.placeholder(tf.float32, shape = [None, 784])
y_ = tf.placeholder(tf.float32, shape = [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

#initialize variables
sess.run(tf.initialize_all_variables())

y = tf.nn.softmax(tf.matmul(x,W) + b) 
#If there were only two classes you can do tf.sigmoid or tf.tanh
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y), reduction_indices = [1]))

#This is our cost function

l2reg = tf.reduce_sum(tf.square(W)) #Add some regularization

#Set-up gradient descent
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy+0.01*l2reg)

#Run 1000 iterations
for i in range(1000):
        batch = mnist.train.next_batch(50)
        train_step.run(feed_dict = {x: batch[0], y_:batch[1]})
		
		
		
#This returns a list of Booleans [True, False, True, .....]
		
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

#we cast them into floats and then take the mean #ASK ME ABOUT CASTING!
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#If we take the mean of the floats, it gives us the accuracy.

print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
#all of it was functions (graphs), we need to execute it.
