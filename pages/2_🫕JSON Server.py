import streamlit as st
from utils import st_def

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()
#------------------------------------------------------------------------------------------------
tab1, tab2 = st.tabs(["JSON Server", "Display the Data"])
with tab1:
    st.markdown('npx json-server --port 3001 --watch part1/data/db.json')
  

with tab2:
        st.warning("Please upload a PDF to display the data.")
    