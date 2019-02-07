# Count number of instances for each class (forklift, person, pallet)
#
# From /DataAugmentationForObjectDetection-master/fastlog_aug_prep_utils_tutorial_folder.ipynb
#
# Author: Charlene V. San Buenaventura, MSc., ECE
#
# ============================================================================================

r"""Executable for creating tiled images.

Example usage:
    python count_instances.py \
        --input_folder=path/to/input_folder \
        --label_folder=path/to/label_folder
"""

from data_aug.data_aug import *
from data_aug.bbox_util import *
import tensorflow as tf
import numpy as np 
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

from fastlog_aug_utils.aug_horflip import *
from fastlog_aug_utils.aug_randrotate import *
from fastlog_aug_utils.aug_randscale import *
from fastlog_aug_utils.aug_randshear import *
from fastlog_aug_utils.aug_randtranslate import *
from fastlog_aug_utils.aug_randhsv import *
from fastlog_aug_utils.aug_resize import *
from fastlog_aug_utils.aug_seq import *
from fastlog_aug_utils.aug_seq_spec import *

from assess_folder_utils import *

##from playHallelujah import *

flags = tf.app.flags

flags.DEFINE_string('input_folder', '',
                    'Input folder containing input images.')
flags.DEFINE_string('label_folder', '',
                    'Label folder containing labels of images from input folder.')


FLAGS = flags.FLAGS

def main(_):

    filename_list_pallet, filename_list_person, filename_list_forklift, pallet_counter, person_counter, forklift_counter = assess_folder(FLAGS.input_folder, FLAGS.label_folder)

    print("Number of pallets in {}: ".format(FLAGS.input_folder), pallet_counter)
    print("Number of perons in {}: ".format(FLAGS.input_folder), person_counter)
    print("Number of forklifts in {}: ".format(FLAGS.input_folder), forklift_counter)
    print("\n")
    print("Number of files in {} with pallet labels: ".format(FLAGS.input_folder),
          len(filename_list_pallet))
    print("Number of files in {} with person labels: ".format(FLAGS.input_folder),
          len(filename_list_person))
    print("Number of files in {} with forklift labels: ".format(FLAGS.input_folder),
          len(filename_list_forklift))

if __name__ == '__main__':
    tf.app.run()
