import cv2
"""
import numpy as np
import os
from random import shuffle
from tqdm import tqdm

TRAIN_DIR = "D:\Python tutorial videos\DATA SETS\\train"
TEST_DIR = "D:\Python tutorial videos\DATA SETS\\test1"
IMG_SIZE = 50
LR = 1e-3

MODEL_NAME = "cats vs dogs-{}-{}.model".format(LR, "2conv-basic")


# helper functions
def label_image(img):
    word_label = img.split(".")[-3]
    if word_label == "cat": return [1, 0]
    elif word_label == "dog": return [0, 1]


def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = label_image(img)
        path = os.path.join(TRAIN_DIR, img)
        img = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (IMG_SIZE, IMG_SIZE))
        training_data.append([np.array(img), np.array(label)])
    shuffle(training_data)
    np.save("training_data.npy", training_data)
    return training_data


# test_data
def process_test_data():
    testing_data = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR, img)
        img_num = img.split(".")[0]
        img = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (IMG_SIZE, IMG_SIZE))
        testing_data.append([np.array(img), img_num])

    np.save("test_data.npy", testing_data)
    return testing_data

train_data = create_train_data()
"""
