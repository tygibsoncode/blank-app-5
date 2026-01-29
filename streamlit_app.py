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
