import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_probas, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0, 0, 0],
        index={'glioma': 0, 'healthy': 1, 'meningioma': 2, 'pituitary': 3}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    i = 0
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = pred_probas[i]
        i += 1
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/brain_tumour_model.h5")
    class_indices = load_pkl_file(f'outputs/{version}/class_indices.pkl')
    maxvalue = model.predict(my_image)[0].max()
    class_index = np.where(model.predict(my_image)[0] == maxvalue)[0][0]
    target_map = {v: k for k, v in class_indices.items()}
    pred_class = target_map[class_index]

    pred_proba = maxvalue
    pred_probas = model.predict(my_image)[0]

    st.write(
        f"The predictive analysis indicates: "
        f"**{pred_class.lower()}** : {round(pred_proba*100, 1)}%")
    

    return pred_proba, pred_probas, pred_class