import streamlit as st


def rest():
    st.markdown("""
        REST terminology, refers to individual data objects, such as the notes in our app, as `resources`. 
        
        Every `resource` has a unique address associated with it - its `URL`. 
        
        `Resources` are fetched from the server with `HTTP GET` requests. 
        
        Creating a new `resource` for storing a note is done by making an `HTTP POST` request to the notes `URL` according to the `REST` convention.
        The data for the new note resource is sent in the body of the request.
    """)

def fc():
    st.markdown("🚀) 🍨📄Rule Extraction📚: Python Libraries  Approaches📰🍨 ")
