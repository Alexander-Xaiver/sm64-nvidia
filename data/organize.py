import os
from os import listdir

#pulling image names from asl_original/* folders
#and spits them into appropriate file for purposes
#of organizing them into the expected format

folder_dir = "/home/nvidia/jetson-inference/python/training/detection/ssd/data/asl_original/test"

for images in os.listdir(folder_dir):
    if images.endswith(".jpg"):
            image_print = images[:-4]
            with open('/home/nvidia/jetson-inference/python/training/detection/ssd/data/asl_clean/ImageSets/Main/test.txt', 'a') as train:
                train.write(image_print)
                train.write('\n')