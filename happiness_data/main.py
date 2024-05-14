import pandas as pd
import streamlit as st
import plotly.express as px

# Read happiness data from CSV
df = pd.read_csv("happy.csv")

# Create a dictionary of title headings in CSV
title_dict = ["Country", "Happiness", "GDP", "Social support",
              "Life expectancy", "Freedom to make life choices",
              "Generosity", "Corruption"]

# Create a heading/title for the page in streamlit
st.title("In Search of Happiness")

# Create dropdown boxes to select the axes to display on the graph
x_axis = st.selectbox("Select the data for the x-axis", title_dict)
y_axis = st.selectbox("Select the data for the y-axis", title_dict)

# Titles to lower case and replace spaces with underscores to match data
x_data = df[f"{x_axis.lower().replace(' ', '_')}"]
y_data = df[f"{y_axis.lower().replace(' ', '_')}"]

# Sub-heading listing picked parameters
st.subheader(f"{x_axis} and {y_axis}")

# Data plot giving axis labels selected from drop down list
figure = px.scatter(x=x_data, y=y_data, labels={"x": f"{x_axis}", "y": f"{y_axis}", })
st.plotly_chart(figure)