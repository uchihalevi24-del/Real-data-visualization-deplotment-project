import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "Netflix_cleaned_dataset.csv"

df = pd.read_csv(DATA_PATH)

st.set_page_config("Movies 🎞️")

st.markdown('<h3 style="background-color:lightgray ; color: darkgreen ;">A chart for distribution of the durations of the movies :</h3>',unsafe_allow_html=True)

st.divider()

movies_durations =  df[df['duration_unit'].str.contains('Minute', na=False)].duration_value.value_counts().reset_index().sort_values(by='count')

st.plotly_chart(px.box(movies_durations , x = 'duration_value'
       ,template='simple_white'
       ,labels={'duration_value' : 'Movie duration in minutes'}))
