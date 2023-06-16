import plotly.graph_objs as go
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
st.set_page_config(layout="wide")


streamlit_path = 'EDA\Simona\scripts\st_testing.py'
file_path = 'EDA/Simona/scripts/Preprocessed_Dataset.csv'


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
    df = df.sort_values(by='date', ascending=True)
    df = df.groupby(by=['date', 'Year', 'months',
                    'Neighborhood', 'regions']).mean()
    df.reset_index(inplace=True)
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


def barplot(df, y):
    fig = px.bar(df, x='date', y=y, color='months')
    fig1 = px.bar(df, x='Year', y=y, color='Year')

    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))
    fig1.update_xaxes(minor=dict(ticks="inside", showgrid=True))

    return fig, fig1


def histogram(df, y):
    fig = px.histogram(df, x="date", y=y, histfunc="avg",
                       nbins=30, text_auto='.2f')

    fig.add_hline(y=df[y].mean(), line_dash="dot",
                  annotation_text="Average green score of all time",
                  annotation_position="bottom right")

    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))

    return fig


def headmap(df):
    df_groupby = df.groupby(by='regions')[
        ['green_score', 'income', 'livability_score_x', 'Registered nuisance (number)']].mean().reset_index()
    fig = px.imshow(df_groupby.corr(), text_auto=True)
    return fig


df_sorted = preprocess(df_read)
scatterplot_livability = scatterplot(df_sorted, 'livability_score_x', 'green_score',
                                     'Correlation between Livability Score and Green Score Index')
scatterplot_income = scatterplot(df_sorted, 'income', 'green_score',
                                 'Correlation between Income score and Green Score Index')
scatterplot_public_nuisance = scatterplot(df_sorted, 'Registered nuisance (number)', 'green_score',
                                          'Correlation between Public Nuisance and Green Score Index')
barplot_months, barplot_years = barplot(df_sorted, 'green_score')
histogram_months = histogram(df_sorted, 'green_score')

headmap_plot = headmap(df_sorted)


tab1, tab2 = st.tabs(['Years', 'Months'])
col1, col2 = st.columns(2)

tab3, tab4, tab5 = st.tabs(['Livability', 'Income', 'Public Nuisance'])
col3, col4 = st.columns(2)


# Bar Chart 1

with tab1:
    st.subheader("Yearly level")
    st.plotly_chart(barplot_years, theme="streamlit", use_container_width=True)

with tab2:
    st.subheader("Monthly level")
    with col1:
        st.plotly_chart(barplot_months, theme="streamlit")
    with col2:
        st.plotly_chart(histogram_months, theme="streamlit")

with col3:
    with tab3:
        st.plotly_chart(scatterplot_livability,
                        theme="streamlit", use_container_width=True)
        with tab4:
            st.plotly_chart(scatterplot_income,
                            theme="streamlit", use_container_width=True)
        with tab5:
            st.plotly_chart(scatterplot_public_nuisance,
                            theme="streamlit", use_container_width=True)
with col4:
    st.plotly_chart(headmap_plot, theme="streamlit", use_container_width=True)
