import streamlit as st
from utils import st_def

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()
#------------------------------------------------------------------------------------------------
tab1, tab2 = st.tabs(["Start", "Structure"])
with tab1:
    st.markdown('''
    
    1. 初始化命令        `npm init vite`

    2. 项目名称
    3. 选择框架选择语言
    4. 安装依赖`npm install`
    
    5. 为项目添加路由组件依赖
    
        `npm i react-router-dom -S`
        
        `npm i @types/react-router-dom -S`
        
    6. 增加antd UI
        `npm i antd --save`
    7. 启动
        `npm run dev`
    8. 支持scss
        `npm i sass -D`
    9. 创建assets/styles/index.scss文件
        `$red:red;`
        
    10.引入index.scss文件
    ''')
    st.code("""
        //打开vite.config.ts,添加scss的预编译选项
        export default defineConfig({
          ...
          css: {
            preprocessorOptions: {
              scss: {
                additionalData: `@import "./assets/styles/index.scss";`
              },
            }
          }
        })""")
        
    st.code('''
    11.调用
        //1、修改App.css > App.scss
        //2、添加scs语法设置字体颜色
        h1{
          color:$red;
        }
        //3、修改引入的文件名
        //import './App.css'
        修改为：
        import './App.scss'

    ''')
  

with tab2:
    st.text('''
    
    项目目录：
├─node_modules		//第三方依赖
├─public			//静态资源（不参与打包）
└─src
    ├─assets		//静态资源
    ├─components	//组件
    ├─config		//配置
    ├─http			//请求方法封装
    ├─layout		//页面布局
    ├─pages			//页面
    ├─routes		//路由
    ├─service		//请求
    ├─store			//状态管理
    └─util			//通用方法
    └─App.css
    └─App.tsx
    └─index.css
    └─main.tsx
    └─vite-env.d.ts
├─.eslinttrc.cjs
├─.gitignore		
├─index.html		//项目页面总入口
├─package.json	
├─tsconfig.json		//ts配置文件
├─tsconfig.node.json
├─vite.config.ts	//vite配置文件
    ''')

    