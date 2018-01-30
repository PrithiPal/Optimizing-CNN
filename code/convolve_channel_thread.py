import threading

import numpy as np
import scipy


## arguments is a dict with all necessary arguments.

def sigmoid(self, x):
    return (1 / (1 + numpy.exp(-x)))


def convolve_channel_thread(featuredict) :

    num_features = featuredict['feature_num']
    conv_dim = featuredict['conv_dim']
    image_channels = featuredict['image_channels']
    patch_dim = featuredict['patch_dim']
    W = featuredict['W']
    image_num = featuredict['image_num']
    b = featuredict['b']
    input_images=featuredict['input_images']


    for feature_num in range(num_features):
        convolved_image = numpy.zeros((conv_dim, conv_dim))

        for channel in range(image_channels):

            limit0  = patch_dim * patch_dim * channel
            limit1  = limit0 + patch_dim * patch_dim
            feature = W[feature_num, limit0 : limit1].reshape(patch_dim,patch_dim)
            image = input_images[:, :, channel, image_num]
            convolved_image = convolved_image + scipy.signal.convolve2d(image, feature, 'valid');


        convolved_image = sigmoid(convolved_image + b[feature_num, 0])
        convolved_features[feature_num, image_num, :, :] = convolved_image
