import plotly.graph_objs as go
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


file_path = 'EDA/Simona/tests/Preprocessed_Dataset.csv'


def read_file_from_relative_path(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content.index
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error reading file '{file_path}'.")
        return None


file_content = read_file_from_relative_path(file_path)
if file_content:
    df_read = pd.read_csv(file_path, index_col=0)
    print('Sucessfully read the .csv!')


def preprocess(df):
    df = df.sort_values(by='Year', ascending=True)
    df['date'] = pd.to_datetime(df['date'])
    return df


def scatterplot(df, x, y, title):
    fig = px.scatter(df,
                     x=x,
                     y=y,
                     animation_frame="Year",
                     size="Population",
                     animation_group="Neighborhood",
                     hover_name="Neighborhood",
                     log_x=True,
                     size_max=60,
                     color="regions",
                     title=title)
    fig["layout"].pop("updatemenus")

    return fig


def barplot(df, date):
    fig = px.bar(df, x=date, y='green_score')
    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))

    return fig


df_sorted = preprocess(df_read)
fig = scatterplot(df_sorted, 'livability_score_x', 'green_score',
                  'Correlation between Livability Score and Green Score Index')
fig1 = scatterplot(df_sorted, 'income', 'green_score',
                   'Correlation between Income score and Gareen Score Index')
fig2 = barplot(df_sorted, 'date')
fig3 = barplot(df_sorted, 'Year')


st.plotly_chart(fig, theme="streamlit", use_container_width=True)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

tab1, tab2 = st.tabs(['Months', 'Year'])
with tab1:
    st.subheader("Monthly level")
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
with tab2:
    st.subheader("Yearly level")
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
