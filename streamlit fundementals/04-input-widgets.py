import streamlit as st
import pandas as pd

st.title("Input Widget")

# Button
st.caption("Button")

col1, col2 = st.columns(2)

with col1:
    primary_btn = st.button(label='Primary', type='primary')
with col2:
    secondary_btn = st.button(label='Secondary', type='secondary')

if primary_btn:
    st.write("Hello From Primary Button!!")

if secondary_btn:
    st.write("Hello From Secondary Button!!")

st.divider()
# Checkbox
st.caption("Checkbox")

checkbox = st.checkbox("Remember Me!!")

if checkbox:
    st.write("I'll remember you")
else:
    st.write("I won't remember you")

st.divider()
# Radio Buttons
st.caption("Radio Buttons")

df = pd.read_csv("/workspaces/Machine-Learning-Model-Deployment-with-Streamlit/data/students-score.csv")
radio = st.radio("Choose a Subject", options=df.columns[2:], index=0, horizontal=True)

# st.write(radio)

st.divider()
# Selectbox
st.caption("Selectbox")

select = st.selectbox("Choose a Subject", options=df.columns[2:], index=2)
st.write(select)

st.divider()
# MultiSelect
st.caption("MultiSelect")
multiSelect = st.multiselect("Choose Top 3 Subjects you like", options=df.columns[2:], max_selections=3)
st.write(multiSelect)

st.divider()
# Slider
st.caption("Slider")
slider = st.slider("Pick a number", min_value=0.0, max_value=5.0, value=0.0, step=0.5)
st.write(slider)

st.divider()
# Text Input
st.caption("Text Input")

text_input = st.text_input("What's your name", placeholder="John Doe")
st.write(f"your name is {text_input}")

st.divider()
# Number Input
st.caption("Number Input")
st.number_input("Type your age", min_value=0, max_value=150, value=0, step=1)


st.divider()
# Text Area
st.caption("Text Area")
tx_are = st.text_area("Type your feedback", height=200, placeholder='Your feedback here')

st.write(tx_are)