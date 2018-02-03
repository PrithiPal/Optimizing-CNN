
import numpy
import scipy
import logging

def sigmoid(x):

    return (1 / (1 + numpy.exp(-x)))

def convolve_thread(feature_dict,start_num_features,end_num_features,thread_id) :

    global thread_logger
    thread_logger = logging.getLogger('simple_example')
    thread_logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(message)s')

    ch.setFormatter(formatter)
    thread_logger.addHandler(ch)

    conv_dim = feature_dict['conv_dim']
    image_channels = feature_dict['image_channels']
    patch_dim = feature_dict['patch_dim']
    W = feature_dict['W']
    image_num = feature_dict['image_num']
    b = feature_dict['b']
    input_images=feature_dict['input_images']
    convolved_features=feature_dict['convolved_features']

    #thread_logger.info('[Thread {}] : Features : [{},{}]'.format(thread_id,start_num_features,end_num_features))

    for feature_num in range(start_num_features,end_num_features):

        convolved_image = numpy.zeros((conv_dim, conv_dim))

        for channel in range(image_channels):

            limit0  = patch_dim * patch_dim * channel
            limit1  = limit0 + patch_dim * patch_dim
            feature = W[feature_num, limit0 : limit1].reshape(patch_dim,patch_dim)
            image = input_images[:, :, channel, image_num]
            convolved_image = convolved_image + scipy.signal.convolve2d(image, feature, 'valid');


    convolved_image = sigmoid(convolved_image + b[feature_num, 0])
    convolved_features[feature_num, image_num, :, :] = convolved_image

    #thread_logger.info('[ convolve ] : Convolve_thread[{}] ended'.format(thread_id))
    return convolved_features
