import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_ml_performance import page_ml_performance_metrics


app = MultiPage(app_name="Brain Tumour Classifier")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("ML performance Metrics", page_ml_performance_metrics)

app.run()