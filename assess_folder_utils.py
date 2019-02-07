# Module for assessing a folder
#
# Author: Charlene V. San Buenaventura, MSc., ECE
#
# ==============================================================================


from data_aug.data_aug import *
from data_aug.bbox_util import *
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

def assess_folder(input_folder, label_folder):
    """Define function for counting of instances per class, and returning
    the list of filenames that contains each class

    Parameters
    __________

    input_folder : string
                folder containing images
    label_folder : string
                folder containing labelss

    Returns
    _______

    filename_list_pallet, filename_list_person, filename_list_forklift
        list of filenames containing each class
        
    pallet_counter, person_counter, forklift_counter
        number of instances for each class

    """
    
    # Initialize class counters
    pallet_counter = 0
    person_counter = 0
    forklift_counter = 0

    # Initialize number of files
    num_files = 0

    # List of filenames for each class
    filename_list_pallet = []
    filename_list_forklift = []
    filename_list_person = []

    # Iterate through entire folder
    for filename in os.listdir(input_folder):
        # Iterate through images only
        if filename.endswith(".jpg"): 

            # Get current image name
            input_img = filename

            # Get image prefix
            img_prefix = input_img.replace('.jpg','')

            # Get current image path
            input_img_path = os.path.join(input_folder, filename)
            # Get current xml path
            label_xml_path = os.path.join(label_folder, img_prefix + ".xml")

            img = cv2.imread(input_img_path)[:,:,::-1]
            
            
            if os.path.exists(label_xml_path) == True:

                # Define tree
                tree = et.parse(label_xml_path)
                # Get root
                root = tree.getroot()


                for child in root:
                    if (child.tag == "object"):
                        for element in child:

                            if element.tag == "name":
                                if element.text == "pallet":   
                                    pallet_counter = pallet_counter + 1
                                    if filename not in filename_list_pallet:
                                        filename_list_pallet.append(filename)
                                if element.text =="person":      
                                    person_counter = person_counter + 1
                                    if filename not in filename_list_person:
                                        filename_list_person.append(filename)
                                if element.text == "forklift":  
                                    forklift_counter = forklift_counter + 1
                                    if filename not in filename_list_forklift:
                                        filename_list_forklift.append(filename)



            num_files = num_files + 1
            
            """print(input_img_path, label_xml_path, pallet_counter, person_counter, forklift_counter)
    print(pallet_counter)
    print(person_counter)
    print(forklift_counter)"""
    return filename_list_pallet, filename_list_person, filename_list_forklift, pallet_counter, person_counter, forklift_counter


def copyFilesPerObject(filename_list_obj, src_img_folder, src_xml_folder, dst_folder):
    """Copy all images with pallet to a folder

    Parameters
    ----------

    filename_list_obj : numpy.array
        list of filenames for specific class    

    src_img_folder : string
        source folder containing images

    src_xml_folder : string
        source folder containing labels

    dst_folder : string
        destination folder
    
    """

    for img_obj in filename_list_obj:
        src_img = os.path.join(src_img_folder, img_obj)
        src_xml = os.path.join(src_xml_folder, img_obj.replace('.jpg', '.xml'))
        """src_img = '/Users/cvsanbuenaventura/Downloads/Ch12_20180513145959_20180513180000/' + img_pallet
        src_xml = '/Users/cvsanbuenaventura/Downloads/labelled_Ch12_20180513145959_20180513180000/' + img_pallet.replace('.jpg', '.xml')"""
        
        if os.path.exists(dst_folder) == False:
            os.mkdir(dst_folder)
            
        ##dst_img = os.path.abspath('./PalletImgs/' + img_pallet)
        dst_img = os.path.abspath(os.path.join(dst_folder, img_obj))
        copyfile(src_img, dst_img)

        dst_xml = os.path.abspath(os.path.join(dst_folder, img_obj.replace('.jpg', '.xml')))
        ##dst_xml = os.path.abspath('./PalletImgs/' + img_pallet.replace('.jpg', '.xml'))
        copyfile(src_xml, dst_xml)


def splitFolderTrainTest(dataset_src_img_folder, dataset_src_xml_folder, train_dst_folder, test_dst_folder, split_ratio = 0.8):
    """Splits folder into train and test sets

    Parameters
    ----------
    
    dataset_src_img_folder : string
        source folder containing image dataset

    dataset_src_xml_folder : string
        source folder containing label dataset

    train_dst_folder : string
        train folder

    test_dst_folder : string
        test folder

    split_ratio : integer
        split ratio
    
    """
    
    import fnmatch
    
    img_counter = 0
    train_counter = 0
    test_counter = 0
    
    tot_num_imgs = len(fnmatch.filter(os.listdir(dataset_src_img_folder), '*.jpg'))

    
    for filename in os.listdir(dataset_src_img_folder):
        # Iterate through images only
        if filename.endswith(".jpg"): 
            img_counter = img_counter + 1
            
            if img_counter < round(split_ratio*tot_num_imgs):
                src_img = os.path.join(dataset_src_img_folder, filename)
                src_xml = os.path.join(dataset_src_xml_folder, filename.replace('.jpg', '.xml'))
                
                if os.path.exists(train_dst_folder) == False:
                        os.mkdir(train_dst_folder)
                        
                dst_img = os.path.abspath(os.path.join(train_dst_folder, filename))
                dst_xml = os.path.abspath(os.path.join(train_dst_folder, filename.replace('.jpg', '.xml')))
                    
                if os.path.exists(src_xml) == True:
                    
                    copyfile(src_img, dst_img)

                    copyfile(src_xml, dst_xml)
                    train_counter = train_counter + 1
                
            else:
                src_img = os.path.join(dataset_src_img_folder, filename)
                src_xml = os.path.join(dataset_src_xml_folder, filename.replace('.jpg', '.xml'))
                
                if os.path.exists(test_dst_folder) == False:
                        os.mkdir(test_dst_folder)

                dst_img = os.path.abspath(os.path.join(test_dst_folder, filename))
                dst_xml = os.path.abspath(os.path.join(test_dst_folder, filename.replace('.jpg', '.xml')))
                    
                if os.path.exists(src_xml) == True:
                    
                    copyfile(src_img, dst_img)

                    copyfile(src_xml, dst_xml)
                    test_counter = test_counter + 1
    print("total number of test images transferred: ", test_counter)
    print("total number of train images transferred: ", train_counter)
            
            
            
        
