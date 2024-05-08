import streamlit as st
from utils import st_def

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()
tab1, tab2 = st.tabs(["Simple HTTP", "Express"])
#------------------------------------------------------------------------------------------------
with tab1:
    st.code("""
    1. create package.json
        {
              "name": "backend",
              "version": "0.0.1",
              "description": "",
              "main": "index.js",
              "scripts": {
                "start": "node index.js",
                "test": "echo \"Error: no test specified\" && exit 1"
              },
              "author": "Matti Luukkainen",
              "license": "MIT"
        }

    2. create index.js
    
            const http = require('http')
    
            const app = http.createServer((request, response) => {
              response.writeHead(200, { 'Content-Type': 'text/plain' })
              response.end('Hello World')
            })
            
            const PORT = 3001
            app.listen(PORT)
            console.log(`Server running on port ${PORT}`)

    3. >node index.js 
    4. >npm start    
        
    """)


with tab2:
    st.code('''
        npm install express
        npm install --save-dev nodemon
        node_modules/.bin/nodemon index.js
    
    
    ''')


    st.code('''
    
        npm install express
        npm install --save-dev nodemon
    
    
    
    ''')


    st.code('''
    
        npm install express
        npm install --save-dev nodemon
    
    
    
    ''')


    st.code('''
    
        npm install express
        npm install --save-dev nodemon
    
    
    
    ''')


    st.code('''
    
        npm install express
        npm install --save-dev nodemon
    
    
    
    ''')

    st.code('''
    
        npm install express
        npm install --save-dev nodemon
    
    
    
    ''')
