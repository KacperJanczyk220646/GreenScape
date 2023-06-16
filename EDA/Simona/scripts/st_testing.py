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
    df['Year'] = df['Year'].astype(str)
    df['date'] = pd.to_datetime(df['date'])
    df['months'] = df['date'].dt.month_name(locale='English')
    df_sorted = df.sort_values(by='date', ascending=True)
    df_sorted = df_sorted.groupby(by=['date', 'Year', 'months']).mean()
    df_sorted.reset_index(inplace=True)
    return df_sorted


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


def barplot(df, y):
    fig = px.bar(df, x='date', y=y, color='months',
                 color_discrete_sequence=['blue'])
    fig1 = px.bar(df, x='Year', y=y, color='Year',
                  color_discrete_sequence=['blue'])

    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))
    fig1.update_xaxes(minor=dict(ticks="inside", showgrid=True))

    fig.update_layout(template='plotly_dark')
    fig1.update_layout(template='plotly_dark')
    return fig, fig1


'''def barplot(df, date):
    fig = px.bar(df, x=date, y='green_score')
    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))

    return fig
'''

df_sorted = preprocess(df_read)
scatterplot_livability = scatterplot(df_sorted, 'livability_score_x', 'green_score',
                                     'Correlation between Livability Score and Green Score Index')
scatterplot_income = scatterplot(df_sorted, 'income', 'green_score',
                                 'Correlation between Income score and Gareen Score Index')
barplot_months, barplot_years = barplot(df_sorted, 'green_score')


st.plotly_chart(scatterplot_livability, theme="streamlit",
                use_container_width=True)
st.plotly_chart(scatterplot_income, theme="streamlit",
                use_container_width=True)

tab1, tab2 = st.tabs(['Months', 'Year'])
with tab1:
    st.subheader("Monthly level")
    st.plotly_chart(barplot_months, theme="streamlit",
                    use_container_width=True)
with tab2:
    st.subheader("Yearly level")
    st.plotly_chart(barplot_years, theme="streamlit", use_container_width=True)
