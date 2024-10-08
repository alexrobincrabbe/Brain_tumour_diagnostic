import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n \n"
        f"The demand for MRI-based diagnostics is increasing, with over a million MRI"
        f" brain scans conducted annually in hospitals and clinics worldwide. Radiologists"
        f" often face the challenge of reviewing large volumes of images under pressure,"
        f" which can lead to delays and diagnostic inconsistencies. Early and accurate diagnosis"
        f" is critical for treatment planning and improving patient outcomes, particularly for"
        f" conditions like glioma and meningioma that require timely intervention. There is a need"
        f" for an automated solution to assist radiologists in identifying and classifying brain"
        f" abnormalities swiftly and accurately. \n \n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 7023 MRI scans of brains split into four classes ")

    st.success(
        f"** The project has 2 business requirements:**\n"
        f"* 1 - The client would like a visual study to better understand the data. \n"
        f"* 2 - The client would like a machine learning solution  "
        f" to determine if an MRI scan belongs to the following classes: glioma, healthy, meningioma, pituitary.\n"
       
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/alexrobincrabbe/Brain_tumour_diagnostic/blob/main/README.md).")