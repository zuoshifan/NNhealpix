import numpy as np
import tensorflow as tf
import nnhealpix.layers

# code to fix error: Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.InteractiveSession(config=config)


NSIDE_INPUT = 1
NSIDE_OUTPUT = 2

input_shape = (1, 12 * NSIDE_INPUT**2, 1)
inputs = np.random.randn(*input_shape).astype(np.float32)
up = nnhealpix.layers.UpSampling(NSIDE_INPUT, NSIDE_OUTPUT)(inputs)
max_pool = nnhealpix.layers.MaxPooling(NSIDE_OUTPUT, NSIDE_INPUT)(up)
av_pool = nnhealpix.layers.AveragePooling(NSIDE_OUTPUT, NSIDE_INPUT)(up)
up1 = nnhealpix.layers.UpSampling(NSIDE_INPUT, NSIDE_OUTPUT)(av_pool)

assert np.allclose(inputs, max_pool)
assert np.allclose(inputs, av_pool)
assert np.allclose(up, up1)
