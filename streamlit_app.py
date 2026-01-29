import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

st.title("Simple Dashboard")

basic_plots = st.checkbox("Basic Plots")
if basic_plots:
    table = pd.DataFrame(
        np.random.randn(20,3),
                         columns=["A","B","C"]
    )
    st.dataframe(table)
    st.line_chart(table)

sliders = st.checkbox("Sliders")
if sliders:
    age = st.slider("How old are you?",18,120,20)
    someRange = st.slider("Select a range",
                          0.0, 200.0, (25., 50))
    dentistAppointment = st.slider("Select a time",
                                   value=(time(10,30),
                                   time(12,30)))
