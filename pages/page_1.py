import streamlit as st
import pandas as pd
# from streamlit_echarts import st_echarts
from PIL import Image
import numpy as np 
from datetime import datetime
import time
import plotly.express as px
import plotly.graph_objects as go 





df = pd.read_csv('data/Quikr_car.csv')
st.set_page_config(layout="wide")


col1,col2,col3=st.columns([0.1,0.8,0.1])
# with col1:
#     box_date=str(datetime.datetime.now().strftime("%d %B %Y"))
#     st.write(f"Current date and time: \n{box_date}")

with col2:
    fig = px.bar(df, x="Name", y= "Company", labels = {"Company": "Company{🛞}"},
                title= "Company's in India", hover_data=["Company"],
                template="gridon", height =500 )
    st.plotly_chart(fig,use_container_width=True)
