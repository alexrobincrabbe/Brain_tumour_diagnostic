import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_mriscans_visualizer_body():
    st.write("### MRI Scans Visualizer")
    st.info(
        f"* Addresses business requirement 1 \n"
        f"* The client would like a study to visually differentiate "
        f"scans by category.")
    
    version = 'v1'
    if st.checkbox("Average and variability images"):
        avg_glioma = plt.imread(f"outputs/{version}/avg_var_glioma.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_meningioma = plt.imread(f"outputs/{version}/avg_var_meningioma.png")
        avg_pituitary = plt.imread(f"outputs/{version}/avg_var_pituitary.png")

        st.warning(
            f"* The average and variability show some differences accross labels,"
            f" Most notably for the healthy scans. The difference appears however to" 
            f" be due to a bias in the angle of the scans. In the case of the healthy scans,"
            f" the average suggest the scans are monstly taken in the tranverse plane "
            f" (from the top of the head). ")


        st.image(avg_glioma, caption='Glioma - Average and Variability')
        st.image(avg_healthy, caption='Healthy - Average and Variability')
        st.image(avg_meningioma, caption='Meningioma - Average and Variability')
        st.image(avg_pituitary, caption='Pituitary - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between labels"):
        my_data_dir = 'inputs/brain_tumour_dataset'
        labels = os.listdir(my_data_dir+ '/validation')
        l_1 = st.selectbox(label="Select label", key="l1",options=labels, index=0)
        # Remove first selection from second selection box options list
        labels_2 = [label for label in labels if label != l_1]
        l_2 = st.selectbox(label="Select label", key="l2", options=labels_2)
        # Swap labels to match filename
        if l_2 == "healthy" or (l_2 == "glioma" and l_1 == "meningioma") or l_1 == "pituitary":
            x = l_1
            y = l_2
            l_1 = y
            l_2 = x

        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff_{l_1}_{l_2}.png")
        if l_1 == "healthy":
            st.warning(
                f"* The difference between healthy scans and the other"
                f" scans is noticable, however suggests a bias in the angle of the scans.")
        else:
             st.warning(
                f"* There are no significant differnces between the "
                f" average of the images.")
        st.image(diff_between_avgs, caption='Difference between average images')


    if st.checkbox("Image Montage"): 
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        my_data_dir = 'inputs/brain_tumour_dataset'
        labels = os.listdir(my_data_dir+ '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):      
            image_montage(dir_path= my_data_dir + '/validation',
                        label_to_display=label_to_display,
                        nrows=8, ncols=3, figsize=(10,25))
        st.write("---")



def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    # how many images in that folder
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)
    # plt.show()


  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")