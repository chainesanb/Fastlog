# Split folder into train and test sets
#
# Author: Charlene V. San Buenaventura, MSc., ECE
#
# ==============================================================================

r"""Executable for splitting folder into train and test sets.

Example usage:
    python  split_folder_train_test.py \
        --src_img_folder=path/to/src_img_dir\
        --src_xml_folder=path/to/src_xml_dir \
        --split_ratio 0.8
"""

import tensorflow as tf
from data_aug.data_aug import *
from data_aug.bbox_util import *
import numpy as np
import shutil
import cv2 
import matplotlib.pyplot as plt 
import pickle as pkl
##get_ipython().run_line_magic('matplotlib', 'inline')

import xml.etree.ElementTree as et  

from yattag import Doc, indent
import os.path

import fnmatch
from shutil import copyfile

import os

# import newly created
from fastlog_aug_utils.aug_horflip import *
from fastlog_aug_utils.aug_randrotate import *
from fastlog_aug_utils.aug_randscale import *
from fastlog_aug_utils.aug_randshear import *
from fastlog_aug_utils.aug_randtranslate import *
from fastlog_aug_utils.aug_randhsv import *
from fastlog_aug_utils.aug_resize import *
from fastlog_aug_utils.aug_seq import *
from fastlog_aug_utils.aug_seq_spec import *

import assess_folder_utils
from assess_folder_utils import *

#rom playHallelujah import *

flags = tf.app.flags

"""flags.DEFINE_string('train_dst_folder', '',
                    'Train destination folder where train dataset will be stored.')
flags.DEFINE_string('test_dst_folder', '',
                    'Test destination folder where test dataset will be stored.')"""
flags.DEFINE_string('src_img_folder', '',
                    'Source image folder which will be split into train and test sets.')
flags.DEFINE_string('src_xml_folder', '',
                    'Source xml folder which will be split into train and test sets.')
flags.DEFINE_float('split_ratio', 0.8, 'Number of worker+trainer '
                     'Split ratio between train and test sets.')


FLAGS = flags.FLAGS



def main(_):

    train_dst_folder = FLAGS.src_img_folder + '_train'
    test_dst_folder = FLAGS.src_img_folder + '_test'

    """if os.path.exists(train_dst_folder) == False:
        os.mkdir(train_dst_folder)"""
    if os.path.exists(train_dst_folder) == True:
        shutil.rmtree(os.path.abspath(train_dst_folder))
        os.mkdir(os.path.abspath(train_dst_folder))
    else:
        os.mkdir(os.path.abspath(train_dst_folder))
            
    """if os.path.exists(test_dst_folder) == False:
        os.mkdir(test_dst_folder)"""

    if os.path.exists(test_dst_folder) == True:
        shutil.rmtree(os.path.abspath(test_dst_folder))
        os.mkdir(os.path.abspath(test_dst_folder))
    else:
        os.mkdir(os.path.abspath(test_dst_folder))

    assess_folder_utils.splitFolderTrainTest(FLAGS.src_img_folder, FLAGS.src_xml_folder, train_dst_folder, test_dst_folder, FLAGS.split_ratio)


if __name__ == '__main__':
  tf.app.run()
