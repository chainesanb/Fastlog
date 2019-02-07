# Tile four images into new image
#
# Author: Charlene V. San Buenaventura, ECE, MSc.
#         Data Scientist
#         Trends & Technologies, Inc.
# ==============================================================================

r"""Executable for creating tiled images.

Example usage:
    python tile_utils.py \
        --input_img1=path/to/input_img1.jpg \
        --input_img2=path/to/input_img2.jpg \
        --input_img3=path/to/input_img3.jpg \
        --input_img4=path/to/input_img4.jpg \
        --output_img output.jpg 
"""

from __future__ import print_function
import os

import tensorflow as tf

from PIL import Image


flags = tf.app.flags

flags.DEFINE_string('input_img1', '',
                    'Image 1 that will be tiled into an output image.')
flags.DEFINE_string('input_img2', '',
                    'Image 2 that will be tiled into an output image.')
flags.DEFINE_string('input_img3', '',
                    'Image 3 that will be tiled into an output image.')
flags.DEFINE_string('input_img4', '',
                    'Image 4 that will be tiled into an output image.')
flags.DEFINE_string('output_img', '',
                    'Image 4 that will be tiled into an output image.')


FLAGS = flags.FLAGS

def main(_):
    files = [FLAGS.input_img1, FLAGS.input_img2, FLAGS.input_img3, FLAGS.input_img4]

    result = Image.new("RGB", (640, 480))

    for index, file in enumerate(files):
        path = os.path.expanduser(file)
        img = Image.open(path)
        img.thumbnail((320, 240), Image.ANTIALIAS)
        x = index // 2 * 320
        y = index % 2 * 240
        w, h = img.size
        print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
        result.paste(img, (x, y, x + w, y + h))

        result.save(os.path.expanduser(FLAGS.output_img))

if __name__ == '__main__':
    tf.app.run()
