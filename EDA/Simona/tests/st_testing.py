import streamlit as st
import plotly.express as px
import pandas as pd


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


file_path = 'EDA/Simona/tests/Main.csv'
file_content = read_file_from_relative_path(file_path)
if file_content:
    df_read = pd.read_csv(file_path, index_col=0)
    print('Sucessfully read the .csv!')


def transform_datetime(df):
    df[['Year', 'year_y', 'year_x', 'date']] = df[[
        'Year', 'year_y', 'year_x', 'date']].apply(pd.to_datetime)
    df = df.sort_values(by='Year', ascending=True)
    return df


df = transform_datetime(df_read)

print('Datetime types :', list(df.select_dtypes(['datetime64']).columns))
print('Object types :', list(df.select_dtypes(['object']).columns))
print('Int types :', list(df.select_dtypes(['int64']).columns))
print('Float types :', list(df.select_dtypes(['float64']).columns))


def scatter_plot_livability_income(df):
    fig = px.scatter(df,
                     x="livability_score_x",
                     y="Income Index",
                     animation_frame="year_y",
                     size="Population",
                     animation_group="neighborhood",
                     hover_name="neighborhood",
                     log_x=True,
                     size_max=60,
                     color="regions",
                     title='Correlation between Income Index and Livability Score')
    fig["layout"].pop("updatemenus")
    return fig


tab1, tab2 = st.tabs(
    ["Correlation between income and livability", "Plotly native theme"])

with tab1:
    fig = scatter_plot_livability_income(df)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
