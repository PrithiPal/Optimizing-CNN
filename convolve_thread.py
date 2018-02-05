
import numpy
import scipy
import logging
import threading
import time



## num should be properly divisible by arr_size
def initiate_thread_pool(num,feature_dict,arr_size,t_id,l,logger) :


    thread_pool=[]
    range_array = numpy.arange(0,arr_size+1,arr_size/num)




    for i in range(num) :
        start = range_array[i]
        end = range_array[i+1]
        thread = cthread(feature_dict,start,end,t_id,l,logger)
        thread_pool.append(thread)
        thread.start()
        #logger.info('[ ThreadPool ] : cthread {} with range [{},{}] initiated'.format(i,start,end))

    return thread_pool

class conv_feature :
    def __init__(self,conv_feature_arr,log) :
        self.conv_feature_arr = conv_feature_arr
        self.log = log


    def append_conv_feat(self,partial_conv_feat_arr,a,b,thread_id) :
        l = threading.Lock()

        l.acquire()
        self.conv_feature_arr[a,b,:,:] = partial_conv_feat_arr
        #self.log.info(' [conv_feat] : cthread {} appended. New size={}'.format(thread_id,numpy.count_nonzero(self.conv_feature_arr)))
        l.release()


    def get_conv_feat() :
        return self.conv_feature_arr



def sigmoid(x):

    return (1 / (1 + numpy.exp(-x)))


class cthread(threading.Thread) :

    def __init__(self,feature_dict,start_iter,end_iter,thread_id,thread_lock,logger) :

        super(cthread,self).__init__()

        self.feature_dict=feature_dict
        self.start_iter=start_iter
        self.end_iter=end_iter
        self.logger=logger
        self.thread_id=thread_id
        self.thread_lock=thread_lock

    def run(self) :
        enter_lock = threading.Lock()
        #enter_lock.acquire()
        #self.logger.info('[ cthread {}] : start iterating [{},{}] '.format(self.thread_id,self.start_iter,self.end_iter))
        c = convolve_thread(self.feature_dict,self.start_iter,self.end_iter,self.thread_id,self.thread_lock,self.logger)
        #self.logger.info('[ cthread {}] : finished iterating [{},{}]'.format(self.thread_id,self.start_iter,self.end_iter))
        #enter_lock.release()
        return c



def convolve_thread(feature_dict,start_num_features,end_num_features,thread_id,thread_lock,logger) :



    conv_dim = feature_dict['conv_dim']
    image_channels = feature_dict['image_channels']
    patch_dim = feature_dict['patch_dim']
    W = feature_dict['W']
    image_num = feature_dict['image_num']
    b = feature_dict['b']
    input_images=feature_dict['input_images']
    convolved_features=feature_dict['convolved_features']
    convolved_features_obj=feature_dict['convolved_features_obj']
    num_features=feature_dict['num_features']


    #logger.info('[ convolve_thread ] : params : F = {}, C = {}'.format(num_features,image_channels))
    #for feature_num in range(start_num_features,end_num_features):

    t_id=0
    time1=time.time()
    for feature_num in range(start_num_features,end_num_features): ## runs 500 * 3 = 1500 times

        convolved_image = numpy.zeros((conv_dim, conv_dim))

        for channel in range(image_channels):
            limit0  = patch_dim * patch_dim * channel
            limit1  = limit0 + patch_dim * patch_dim
            feature = W[feature_num, limit0 : limit1].reshape(patch_dim,patch_dim)
            image = input_images[:, :, channel, image_num]
            convolved_image = convolved_image + scipy.signal.convolve2d(image, feature, 'valid')

    time2=time.time()-time1
    #logger.info('[ convolve thread ] : Time Taken : {}, [{}]'.format(time2,threading.activeCount()))
    convolved_image = sigmoid(convolved_image + b[feature_num, 0])
    convolved_features_obj.append_conv_feat(convolved_image,feature_num,image_num,thread_id)


    #new_convolved_features_arr = conv_feat(convolved_features,convolved_image,feature_num,image_num,logger,thread_id)
    #convolved_features[feature_num, image_num, :, :] = convolved_image


    ##logger.info('[ convolve_thread ] : convolved_feature non-zero size={}'.format(numpy.count_nonzero(convolved_features)))



    return
