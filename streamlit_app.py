import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Streamlit App')

st.write(pd.DataFrame({
  'first column':[1,2,3,4],
  'second column' : [10,20,30,40]
}))

if st.button('Say hello'):
  st.write('why hello there!')
else:
  st.write('goodbye')

chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columns=['a','b','c'])
st.line_chart
