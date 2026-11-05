import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "Netflix_cleaned_dataset.csv"

df = pd.read_csv(DATA_PATH)

st.set_page_config('TV shows 🍿')


st.markdown('<h3 style="background-color:lightgray ; color: darkblue ;">A chart for distribution of the durations of the TV shows :</h3>',unsafe_allow_html=True)

st.divider()

shows_durations = (
    df[df['duration_unit'].str.contains('Season', na=False)]
    ['duration_value']
    .value_counts()
    .rename_axis('duration_value')
    .reset_index(name='count')
    .sort_values(by='count')
)
st.plotly_chart(px.bar(shows_durations,x='duration_value' , y='count'
       ,template='plotly_dark'
       ,labels={'duration_value' : 'Show sesons' , 'count' : 'Counts'}
       ,color='count'
       ,color_continuous_scale='Tealgrn')
)
