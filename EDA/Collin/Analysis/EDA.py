import plotly.express as px
import geopandas as gpd
import streamlit as st
import pandas as pd

merged = pd.read_csv("/Users/collin/Desktop/School/Github/GreenScape/EDA/Collin/Analysis/Datasets/Merged.csv")

shapefile = gpd.read_file("/Users/collin/Desktop/School/Github/GreenScape/EDA/Collin/Analysis/Shapefiles/Breda.shp")
geodata = shapefile.merge(merged, left_on="BUURT", right_on="Neighborhood", how="left")

incomekey = {None: "No data", 1: "€21,100 to €30,300", 2: "€30,300 to €42,800", 3: "€42,800 to €59,800", 4: "€59,800 +"}

st.title("GreenScape Data Analysis")
st.write("This is an example of displaying plots using Streamlit.")

tabs = st.tabs(["Average Green Score", "Average Income"])

with tabs[0]:
    st.subheader("Average Green Score")
    fig1 = px.choropleth(
        geodata, geojson=geodata.geometry, locations=geodata.index,
        color="Average Green Score", color_continuous_scale="Greens",
        hover_name="Neighborhood", labels={"Average Green Score": "Average Green Score"}
    )
    fig1.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig1)

with tabs[1]:
    st.subheader("Average Income")
    fig2 = px.choropleth(
        geodata, geojson=geodata.geometry, locations=geodata.index,
        color="Income Index", color_continuous_scale="Reds",
        hover_name="Neighborhood", labels={"Income Index": "Average Income"}
    )
    fig2.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig2)

st.subheader("Scatterplot: Average Green Score vs. Average Income")
fig3 = px.scatter(
    merged,
    x="Income Index",
    y="Average Green Score",
    color="Average Green Score",
    color_continuous_scale="Blues",
    labels={"Income Index": "Income", "Average Green Score": "Green Score"}
)

fig3.update_xaxes(
    ticktext=[incomekey.get(x) for x in range(len(incomekey))],
    tickvals=list(range(len(incomekey)))
)

st.plotly_chart(fig3)