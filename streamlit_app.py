import streamlit as st
import streamlit.components.v1 as components

st.title("Your Quantum-Grown Zine Preview 💚")

components.html(
    """
    <iframe src="https://yourpreviewlink.com" width="100%" height="600" frameborder="0"></iframe>
    """,
    height=600
)

