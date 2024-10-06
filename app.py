import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_ml_performance import page_ml_performance_metrics
from app_pages.page_brain_tumour_diagnostic import page_brain_tumour_diagnostic_body
from app_pages.page_mriscans_visualizer import page_mriscans_visualizer_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body

app = MultiPage(app_name="Brain Tumour Classifier")

app.add_page("Project Summary", page_summary_body)
app.add_page("MRI scans visualizer", page_mriscans_visualizer_body)
app.add_page("Brain Tumour Diagnostic", page_brain_tumour_diagnostic_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML performance Metrics", page_ml_performance_metrics)

app.run()