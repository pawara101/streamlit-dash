import streamlit as st
import numpy as np
import pandas as pd

Y = st.checkbox('Yes')
print(Y)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data