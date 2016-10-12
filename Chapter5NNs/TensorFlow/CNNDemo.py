#This is a convolutional NN
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, shape = [None, 784])
y_ = tf.placeholder(tf.float32, shape = [None, 10])

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev = 0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape = shape)
    return tf.Variable(initial)
 
#Here we define the convolution function 
#Strides is the steps is going to take
#padding makes the output = input
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides = [1,1,1,1], padding = 'SAME')

#pooling layers
#k size is the size of the window
#stride is the size of the step
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
 
    
W_conv1 = weight_variable([5, 5, 1, 16]) #16convolutions of 5x5 3rd element is the numb of channels
b_conv1 = bias_variable([16])  
x_image = tf.reshape(x, [-1, 28, 28, 1])  #reshape input into a tensor
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1) #evaluate
h_pool1 = max_pool_2x2(h_conv1) #pool

W_conv2 = weight_variable([5, 5, 16, 8]) #next layer has 16 channels (output of previous) and 8 convolutions
b_conv2 = bias_variable([8])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2) #evaluate
h_pool2 = max_pool_2x2(h_conv2) #pooling

W_fc1 = weight_variable([7 * 7 * 8, 1024]) #fully connected layer with 1024 neurons (new size is 7)
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*8]) #flat what we got out of the pooling
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)#evaluate

#dropout (if time permits)
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob) #dropout units in this layer

W_fc2 = weight_variable([1024, 10]) #second fully connected layer
b_fc2 = bias_variable([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2) #final output

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv), reduction_indices=[1])) #cost
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy) #setup our optimizer (2014 optimizer)

#setup functions for accuracy
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(tf.initialize_all_variables())

for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict = {x: batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g"%(i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
print("test accuracy %g"%accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))

