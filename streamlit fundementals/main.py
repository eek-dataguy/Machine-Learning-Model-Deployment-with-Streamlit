import streamlit as st

# Give your app a title
st.title("Machine Learning Model with Streamlit")

# Header
st.header("Streamlit Fundementals")

# Subheader
st.subheader("Text Elements in Streamlit")

#Markdown
st.markdown("""
    This is **Markdown** Text
    # Header - 1
    ## Sub Header - 1.1
    ## Sub Header - 1.2
    # Header - 2
    ## Sub Header - 2.1
    ## Sub Header - 2.2     
""")

# Caption
st.caption('This is caption')

# Code block
st.code("""
        import streamlit as st
        
""")

# Preformatted Text
st.text('Hi, this is just a text')

# Latex
st.latex(" x = 2^2 ")

# Divider
st.divider()

# st.write
st.write("Some Text")
