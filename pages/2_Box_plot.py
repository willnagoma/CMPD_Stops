import streamlit as st
import pandas as pd
import altair as alt
import main


stops=main.load_csv('Data/Officer_Traffic_Stops.csv')
st.dataframe(stops)
boxPlot=alt.Chart(stops).mark_boxplot().encode(
    alt.X('Was_a_Search_Conducted'),
    alt.Y('Driver_Age'),
    color='Was_a_Search_Conducted'
).properties(
    width=600,
    height=400
)

st.altair_plot(boxPlot)