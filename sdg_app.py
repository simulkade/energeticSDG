import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("energy_CO2_sdg.csv")

data = load_data()

# Dictionary mapping goals to their titles
titles = {
    "energy_per_capita": "Energy per Capita [kWh/(day.person)]",
    "gdp_per_capita": "GDP per Capita [USD]",
    "Annual CO₂ emissions (per capita)": "Annual CO₂ emissions (per capita) [tonnes]",
    "Goal 1 Score": "No Poverty",
    "Goal 2 Score": "Zero Hunger",
    "Goal 3 Score": "Good Health and Well-being",
    "Goal 4 Score": "Quality Education",
    "Goal 5 Score": "Gender Equality",
    "Goal 6 Score": "Clean Water and Sanitation",
    "Goal 7 Score": "Affordable and Clean Energy",
    "Goal 8 Score": "Decent Work and Economic Growth",
    "Goal 9 Score": "Industry, Innovation, and Infrastructure",
    "Goal 10 Score": "Reduced Inequality",
    "Goal 11 Score": "Sustainable Cities and Communities",
    "Goal 12 Score": "Responsible Consumption and Production",
    "Goal 13 Score": "Climate Action",
    "Goal 14 Score": "Life Below Water",
    "Goal 15 Score": "Life on Land",
    "Goal 16 Score": "Peace and Justice Strong Institutions",
    "Goal 17 Score": "Partnerships to achieve the Goal",
}

# Streamlit app
st.title("Sustainable development scores vs. Energy, GDP, and CO₂ emissions")

# Dropdown boxes for selecting goals
title_values = list(titles.values())
selected_x = st.selectbox("X axis", title_values[0:3])
selected_y = st.selectbox("Y axis", title_values[2:])

# Map selected values back to their corresponding keys
column_x = list(titles.keys())[list(titles.values()).index(selected_x)]
column_y = list(titles.keys())[list(titles.values()).index(selected_y)]

# Filter data based on selected goals
data_x = data[column_x]
data_y = data[column_y]

# Create a scatter plot
fig = px.scatter(data, x=column_x, y=column_y, hover_data=["country"])
fig.update_xaxes(title_text=titles[column_x])
fig.update_yaxes(title_text=titles[column_y])

# Display the plot in the Streamlit app
st.plotly_chart(fig)

# add the references
st.markdown("Sustainability data downloaded from the [SDG index website](https://dashboards.sdgindex.org/downloads)")
st.markdown("Energy and CO₂ emissions data downloaded from the [World Bank Open Data](https://data.worldbank.org/) and amazing [Our World in Data](https://ourworldindata.org/)")

