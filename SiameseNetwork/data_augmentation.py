import typing
import numpy as np
import tensorflow_addons as tfa
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras

def get_image_info(dataset: tf.data.Dataset): 
    height = []
    width = []
    labels = {}
    for sample in dataset:
        shape = sample[0].shape
        height.append(shape[0])
        width.append(shape[1])
        cur_count = labels.get(sample[1].numpy(), 0)

        labels[sample[1].numpy()] = cur_count + 1

    return height, width, labels

def plot_histograms(lens, subtitle):
    fig = plt.figure(1, figsize=(10, 5))
    ax1 = plt.subplot(1, 2, 1)
    plt.hist(lens, bins=50)
    plt.title("Length")
    plt.ylabel("Number of samples")
    ax1.tick_params('x', labelrotation=-45)
    ax2 = plt.subplot(1, 2, 2)
    plt.hist(lens, bins=20, cumulative=True)
    plt.title("Cumulative lengths")
    ax2.tick_params('x', labelrotation=-45)

    fig.supxlabel(subtitle)

    plt.subplots_adjust(bottom=0.2)

