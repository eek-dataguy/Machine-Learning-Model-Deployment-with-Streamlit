import streamlit as st
import pandas as pd


st.title("Data Display Elements")

df = pd.read_csv('/workspaces/Machine-Learning-Model-Deployment-with-Streamlit/data/students-score.csv')

st.dataframe(df)

# st.write(df)

# st.table(df)

# Metrix
st.metric(
    label="Student KPI",
    value=90,
    delta= 12,
    delta_color='normal'
    )

st.metric(
    label="Student KPI",
    value=80,
    delta= -12,
    delta_color='normal'
    )


st.metric(
    label="Cancer Chance",
    value=60,
    delta= -12,
    delta_color='inverse'
    )

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Student KPI", value=90, delta=12, delta_color='normal')

with col2:
    st.metric(label="Student KPI", value=80, delta=-12, delta_color='normal')

with col3:
    st.metric(label="Cancer Chance", value=60, delta=-12, delta_color='inverse')
