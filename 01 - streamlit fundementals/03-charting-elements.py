import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Charting Elements")

# Streamlit line plot
st.caption('Streamlit line plot')
df = pd.read_csv("/workspaces/Machine-Learning-Model-Deployment-with-Streamlit/data/students-score.csv")
st.line_chart(df, x='id', y=['physic', 'chemistry'])

# Streamlit area chart
st.caption('Streamlit area chart')
st.area_chart(df, x='id', y=['math', 'chemistry'])

# Streamlit Bar Chart
st.caption("Streamlit Bar Chart")
st.bar_chart(df, x='id', y=['math', 'chemistry'])

# Streamlit map
st.caption('Streamlit map')
geo_df = pd.read_csv("/workspaces/Machine-Learning-Model-Deployment-with-Streamlit/data/city.csv")
st.map(geo_df)

st.divider()
# Mathplotlib
st.caption('Mathplotlib')
fig, ax = plt.subplots()
ax.plot(df.id, df.math)
ax.set_title("Student Math Score")
ax.set_xlabel("Student ID")
ax.set_ylabel('Math Score')
st.pyplot(fig)