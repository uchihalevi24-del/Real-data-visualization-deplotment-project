import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Netflix_cleaned_dataset.csv"

df = pd.read_csv(DATA_PATH)

st.set_page_config('Home',page_icon='🏠' , layout='centered')

with st.sidebar:
    st.title('Filters :' , help='This will filter all the pages')
    years = df.year_added.unique()
    st.selectbox(label='Choose year :' , options=years )

st.markdown('<h1 style=" background-color:black;color:crimson">📊 Netflix\'s shows data analysis </h1>',unsafe_allow_html=True)

st.subheader('A sample of the data :')

st.dataframe(df.head(8))

st.divider()

insights = st.button(label='Go to the insights')

if insights :
    # st.snow()
    # st.toast('Insights', icon='🚀')
    # st.success('You reached insights! ✅' )
    # Theese will happen ⬆️ without the next line
    st.switch_page('pages/Insights.py')




st.divider()


# Selectbox , columns , containers ,metrics

shows = df.title.unique()

show = st.selectbox(label='Choose a show to know it\'s duration ', options=shows)

col1,col2 = st.columns(2)

con1 = col1.container(border=True)
con2 = col2.container(border=True)



con1.metric(label='Show duration : ' , value=f'{int(df[df.title == show].duration_value.values[0])}') #,delta='1',delta_color='green'
con2.metric(label='The unit : ' , value=f'{df[df.title == show].duration_unit.values[0]}')

