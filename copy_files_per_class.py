# Copy images into class folders
#
# From /DataAugmentationForObjectDetection-master/fastlog_aug_prep_utils_tutorial_folder.ipynb
#
# Author: Charlene V. San Buenaventura, ECE, MSc.
#
# ============================================================================================

r"""Executable for copying image into class folder.

Example usage:
    python copy_files_per_class.py \
        --src_img_folder=path/to/src_img_folder \
        --src_xml_folder=path/to/src_xml_folder \
        --dst_folder=path/to/dst_folder \
        --curr_class=<pallet, forklift, person>
"""


import importlib
importlib.reload(assess_folder_utils)

flags = tf.app.flags

flags.DEFINE_string('src_img_folder', '',
                    'Input folder containing input images.')
flags.DEFINE_string('src_xml_folder', '',
                    'Label folder containing labels of images from input folder.')
flags.DEFINE_string('dst_folder', '',
                    'Label folder containing labels of images from input folder.')
flags.DEFINE_string('curr_class', '',
                    'Find images that contains this class.')


FLAGS = flags.FLAGS

def main(_):

    filename_list_pallet, filename_list_person, filename_list_forklift, pallet_counter, person_counter, forklift_counter = assess_folder(FLAGS.src_img_folder, FLAGS.src_xml_folder)

    if FLAGS.curr_class == "pallet":
        assess_folder_utils.copyFilesPerObject(FLAGS.filename_list_pallet, FLAGS.src_img_folder, FLAGS.src_xml_folder, FLAGS.dst_folder)
    elif FLAGS.curr_class == "forklift":
        assess_folder_utils.copyFilesPerObject(FLAGS.filename_list_forklift, FLAGS.src_img_folder, FLAGS.src_xml_folder, FLAGS.dst_folder)
    elif FLAGS.curr_class == "person":
        assess_folder_utils.copyFilesPerObject(FLAGS.filename_list_person, FLAGS.src_img_folder, FLAGS.src_xml_folder, FLAGS.dst_folder)
    

if __name__ == '__main__':
    tf.app.run()
