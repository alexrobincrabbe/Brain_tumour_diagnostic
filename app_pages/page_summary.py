import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"Transfer learning and CNNs could be used for classifying these images, which could save patient lives through early tumor diagnosis."
        f"**Project Dataset**\n"
        f"* The available dataset contains 7023 MRI scans of brains split into four classes ")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Code-Institute-Solutions/WalkthroughProject01/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"healthy scans from scans with brain tumours visually.\n"
        f"* 2 - The client is interested in telling whether a brain scan is of a healthy brain, or one with a tumour, and classifying the tumour. "
        )