import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"- We believe comparing average images of each MRI scan classification, as well as average category"
        f" differences can provie  visual insights and  support radiologists’ diagnoses. "
        f"- Typically healthy scans are easy to distinguish visually from non healthy scans \n\n"
        f"- Other than healthy scans, the average of the images and variability, as well as "
        f" the difference between Averages studies did not reveal "
        f" any clear pattern to differentiate one from another.")
    
    st.success(    
        f" - We believe a machine learning-based classification system, utilizing convolutional neural"
        f" networks (CNNs), can accurately categorize MRI brain scans into four distinct categories: \n"
        f" glioma, meningioma, pituitary tumors, and healthy cases.")