import streamlit as st
import pandas as pd

# Sidebar
with st.sidebar:
    st.write("Streamlit Sidebar")

# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Search by CIF_NO", placeholder='0001432')

with col2:
    st.date_input("Filter by Date")

with col3:
    st.multiselect("Corporate, Individual or Banking", options=['C', 'I' ,'B'], default=['C', 'I', 'B'])

# Tabs
tab1, tab2 = st.tabs(["Line Chart", 'Bar Chart'])
df = pd.read_csv("/workspaces/Machine-Learning-Model-Deployment-with-Streamlit/data/students-score.csv")

with tab1:
    st.line_chart(df, x='id', y=['chemistry', 'physic'])

with tab2:
    st.bar_chart(df, x='id', y=['chemistry', 'physic'])

# Expander (collapsible element)
with st.expander("Math Fomual"):
    st.latex(r"""
    \tilde{X} = X - \mu, \quad \mu = \frac{1}{n} \sum_{i=1}^{n} x_i
    \Sigma = \frac{1}{n} \tilde{X}^T \tilde{X}
    \Sigma v_i = \lambda_i v_i
    W_k = [v_1, v_2, \dots, v_k]
    Z = \tilde{X} W_k
    """)

# Container
with st.container():
    st.write('This is inside container')

st.write("This is outside container")