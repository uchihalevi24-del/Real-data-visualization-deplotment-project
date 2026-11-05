import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv(r'Netflix_cleaned_dataset.csv')

st.set_page_config('Home 🏠')

st.markdown('<h1 style=" background-color:black;color:crimson">📊 Netflix\'s shows data analysis </h1>',unsafe_allow_html=True)

st.subheader('A sample of the data :')

st.dataframe(df.head(8))

st.divider()

st.link_button(label='Go to the insights' , url='youtube.com')

st.divider()


# Selectbox , columns , containers ,metrics

shows = df.title.unique()

show = st.selectbox(label='Choose a show to know it\'s duration ', options=shows)

col1,col2 = st.columns(2)

con1 = col1.container(border=True)
con2 = col2.container(border=True)



con1.metric(label='Show duration : ' , value=f'{int(df[df.title == show].duration_value.values[0])}')
con2.metric(label='The unit : ' , value=f'{df[df.title == show].duration_unit.values[0]}')



