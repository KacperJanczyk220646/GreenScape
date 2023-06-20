import plotly.graph_objs as go
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title='Exploritory Data Analysis', layout="wide")
st.title('Exploritory Data Analysis')

streamlit_path = 'EDA\Simona\scripts\dashboard.py'
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
    fig = px.bar(df, x='date', y=y, color='months',
                 title='Barchart on Monthly level')
    fig1 = px.bar(df, x='Year', y=y, color='Year',
                  title='Barchart on Yearly level')

    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))
    fig1.update_xaxes(minor=dict(ticks="inside", showgrid=True))

    return fig, fig1


def histogram(df, y):
    fig = px.histogram(df, x="date", y=y, histfunc="avg",
                       nbins=30, text_auto='.2f', title='Histogram on Mothly level')
    fig.add_hline(y=df[y].mean(), line_dash="dot",
                  annotation_text="Average green score of all time",
                  annotation_position="bottom right")
    fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))

    return fig


def headmap(df):
    df_groupby = df.groupby(by='regions')[
        ['green_score', 'income', 'livability_score_x', 'Registered nuisance (number)', 'Population']].mean().reset_index()
    fig = px.imshow(df_groupby.corr(), text_auto=True)
    return fig


def linechart(df, y):
    fig = px.line(df, x="Year", y=y)
    fig.update_traces(textposition="bottom right")

    return fig


def pie_charts(df, regions):
    fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}],
                                               [{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=df_sorted['regions'], values=df_sorted['green_score'], name="Green Score"),
                  1, 1)
    fig.add_trace(go.Pie(labels=df_sorted['regions'], values=df_sorted['income'], name="Income"),
                  1, 2)
    fig.add_trace(go.Pie(labels=df_sorted['regions'], values=df_sorted['livability_score_x'], name="Livability"),
                  2, 1)
    fig.add_trace(go.Pie(labels=df_sorted['regions'], values=df_sorted['Registered nuisance (number)'], name="Public Nuisance"),
                  2, 2)
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig.update_layout(template='plotly_dark')
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
pie_charts_plot = pie_charts(df_sorted, 'regions')

df_groupby_years = df_sorted.groupby(by="Year").agg(avg_green_score=("green_score", 'mean'),
                                                    avg_livability_score_x=(
                                                        'livability_score_x', 'mean'),
                                                    avg_total_houses=(
                                                        'TotalHouses', 'mean'),
                                                    avg_population=(
                                                        'Population', 'mean'),
                                                    avg_income=('income', 'mean')).round(2)
df_groupby_months = df_sorted.groupby(by="months").agg(avg_green_score=("green_score", 'mean'),
                                                       avg_livability_score_x=(
                                                           'livability_score_x', 'mean'),
                                                       avg_total_houses=(
                                                           'TotalHouses', 'mean'),
                                                       avg_population=(
                                                           'Population', 'mean'),
                                                       avg_income=('income', 'mean')).round(2)
df_groupby_neighborhoods = df_sorted.groupby(by="Neighborhood").agg(avg_green_score=("green_score", 'mean'),
                                                                    avg_livability_score_x=(
                                                                        'livability_score_x', 'mean'),
                                                                    avg_total_houses=(
                                                                        'TotalHouses', 'mean'),
                                                                    avg_population=(
                                                                        'Population', 'mean'),
                                                                    avg_income=('income', 'mean')).round(2)
df_groupby_regions = df_sorted.groupby(by="regions").agg(avg_green_score=("green_score", 'mean'),
                                                         avg_livability_score_x=(
                                                             'livability_score_x', 'mean'),
                                                         avg_total_houses=(
                                                             'TotalHouses', 'mean'),
                                                         avg_population=(
                                                             'Population', 'mean'),
                                                         avg_income=('income', 'mean')).round(2)


def reset_index(df):
    df_reset_index = df.reset_index()
    return df_reset_index


df_reset_index = reset_index(df_groupby_years)
linechart_years = linechart(df_reset_index, 'avg_green_score')


dropdown_options = ['Months', 'Years']
selected_option = st.selectbox(
    'Select an option:', dropdown_options, format_func=lambda x: x)

col1, col2 = st.columns(2)
if selected_option == 'Months':
    with col1:
        st.plotly_chart(barplot_months, theme='streamlit')
    with col2:
        st.plotly_chart(histogram_months, theme='streamlit')
elif selected_option == 'Years':
    with col1:
        st.plotly_chart(barplot_years, theme='streamlit',
                        use_container_width=True)
    with col2:
        st.plotly_chart(linechart_years, theme='streamlit',
                        use_container_width=True)


tab3, tab4, tab5 = st.tabs(['Livability', 'Income', 'Public Nuisance'])
col3, col4 = st.columns(2)

with tab3:
    st.plotly_chart(scatterplot_livability,
                    theme="streamlit", use_container_width=True)
with tab4:
    st.plotly_chart(scatterplot_income,
                    theme="streamlit", use_container_width=True)
with tab5:
    st.plotly_chart(scatterplot_public_nuisance,
                    theme="streamlit", use_container_width=True)

with col3:
    st.plotly_chart(headmap_plot, theme="streamlit", use_container_width=True)
with col4:
    dropdown_options1 = ['Years', 'Months', 'Regions', 'Neighborhoods']
    tables = {'Years': df_groupby_years['avg_green_score'],
              'Months': df_groupby_months['avg_green_score'],
              'Regions': df_groupby_regions['avg_green_score'],
              'Neighborhoods': df_groupby_neighborhoods['avg_green_score']}
    selected_option = st.selectbox(
        'Select an option:', dropdown_options1, format_func=lambda x: x)
    if selected_option in tables.keys():
        st.write("Table for", selected_option)
        st.dataframe(tables[selected_option], use_container_width=True)
    else:
        st.write("No table selected.")
