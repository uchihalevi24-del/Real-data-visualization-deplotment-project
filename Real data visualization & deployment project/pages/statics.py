import pandas as pd
import plotly.express as px
import streamlit as st
import calendar
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "Netflix_cleaned_dataset.csv"

df = pd.read_csv(DATA_PATH)

st.set_page_config('Statistics 📈')


st.markdown('<h3 style="background-color:lightgray ; color: darkgreen ;">A chart for proportions of TV shows and movies :</h3>',unsafe_allow_html=True)

st.divider()

type_counting = df.type.value_counts().reset_index()

st.plotly_chart(px.pie(type_counting
       ,names='type'
       ,values='count'
       ,template='ggplot2'
       ,hole=0))


st.divider()
st.divider()

st.markdown('<h3 style="background-color:lightyellow ; color: darkgreen ;">A chart for distribution of the age rating :</h3>',unsafe_allow_html=True)

st.divider()

age_ratings = df.age_rating.value_counts().reset_index()

st.plotly_chart(px.histogram(age_ratings,x='age_rating',y='count'
             ,template='simple_white'
             ,labels={'sum of count':'counts' , 'age_rating' : 'Age rating'}))

st.divider()
st.divider()

st.markdown('<h3 style="background-color:lightgray ; color: darkgreen ;">A chart for distribution of the top 10 countries has movies:</h3>',unsafe_allow_html=True)


st.divider()

countries = df['country'].dropna().str.split(', ').explode().str.strip()

top10_countries = (
    countries.value_counts()
    .head(10)
    .rename_axis('country')
    .reset_index(name='count')
)

st.plotly_chart(px.bar(top10_countries,x='country',y='count'
       ,labels={'country':'Country','count':'Repetitions'}
       ,template='plotly_dark'
       ,color_continuous_scale='Emrld'
       ,color='count'
       ))


st.divider()
st.divider()


col1 , col2 = st.columns(2)

con1 = col1.container(border=True)
con2 = col2.container(border=True)

con1.markdown('<h3 style="background-color:lightyellow ; color: darkgreen ;">A chart for distribution of the months  :</h3>',unsafe_allow_html=True)

con1.divider()
month_order = list(calendar.month_name)[1:]
df['month_name'] = pd.Categorical(df['month_name'], categories=month_order, ordered=True)

month_repetitions = df.month_name.value_counts().reset_index().sort_values(by='month_name')

con1.plotly_chart(px.line(month_repetitions,x='month_name',y='count'
           ,template='simple_white'
           , markers=True
           ,labels={'month_name':'Month name' , 'count' : 'counts'})
)


con2.markdown('<h3 style="background-color:lightyellow ; color: darkgreen ;">A chart for distribution of the years :</h3>',unsafe_allow_html=True)

con2.divider()

year_counts = df.year_added.value_counts().reset_index().sort_values(by='year_added')

con2.plotly_chart(px.line(year_counts,x='year_added',y='count'
        ,labels={'year_added':'Year'}
        ,template='plotly_dark'
        ,markers=True )
)

