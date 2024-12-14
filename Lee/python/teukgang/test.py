import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf

import matplotlib.pyplot as plt

(a, b), _ = tf.keras.datasets.cifar10.load_data()
print(a.shape, b.shape)

print(a[0])
plt.imshow(a[0])