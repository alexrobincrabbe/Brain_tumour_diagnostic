import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation
import os


def page_ml_performance_metrics():
    version = 'v9'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Categorical Accuracy', 'precision_glioma', 'recall_glioma', 'precision_healthy', 'recall_healthy', 'precision_meningioma', 'recall_meningioma', 'precision_pituitary', 'recall_pituitary']))

    if st.checkbox("Check performance by label"):

        my_data_dir = 'inputs/brain_tumour_dataset'
        labels = os.listdir(my_data_dir+ '/validation')
        label = st.selectbox(label="Select label",options=labels, index=0)
        precision = plt.imread(f"outputs/{version}/model_training_prec_{label}.png")
        recall = plt.imread(f"outputs/{version}/model_training_rec_{label}.png")
        col3, col4 = st.beta_columns(2)
        with col3:
            st.image(precision, caption='Precision')
        with col4:
            st.image(recall, caption='Recall')





    
    