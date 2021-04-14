import torch
import tensorflow as tf
import numpy as np

print(torch.__version__)
a = np.random.random(10)

print(torch.fft.fft(torch.Tensor(a)))
print(np.fft(a))
print(tf.signal.fft(tf.convert_to_tensor(a)))
#def fft3d(x,gamma):
