import streamlit as st
import streamlit_folium as st_folium
import folium
from folium.plugins import MarkerCluster, Geocoder
import pandas as pd

st.title("Green Index Score Map - distribution within Gemeente Breda")
st.subheader('This map represents green index score points for individual geographical coordinates on the map of Breda.')
st.subheader('This map was created using Folium library in Python!')

def load_data(file_path):
    """
    Loads and returns the data from the specified file path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded data.
    """
    merged_df = pd.read_csv(file_path)
    return merged_df

def create_map(filtered_df, zoom_level):
    """
    Creates a folium map with markers representing neighborhoods and their information.

    Parameters:
        filtered_df (pandas.DataFrame): The filtered dataframe containing neighborhood information.
        zoom_level (int): The initial zoom level of the map.

    Returns:
        folium.Map: The created folium map.
    """
    map_breda = folium.Map(location=[51.5886, 4.7754], zoom_start=zoom_level)

    marker_cluster = MarkerCluster().add_to(map_breda)

    legend_html = '''
    <div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background-color: white; padding: 10px; border: 1px solid black;">
        <p><strong>Legend</strong></p>
        <p><i class="fa fa-circle" style="color:green"></i> Green Score >= 25</p>
        <p><i class="fa fa-circle" style="color:red"></i> Green Score < 25</p>
    </div>
    '''

    legend_css = '''
    <style>
    .fa {
        margin-right: 5px;
    }
    </style>
    '''

    map_breda.get_root().header.add_child(folium.Element(legend_css + legend_html))

    for index, row in filtered_df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Neighborhood: {row['neighborhood_name']}<br>Population: {row['Population']}<br>Total Houses: {row['TotalHouses']}<br>Date of measurement: {row['date']}",
            icon=folium.Icon(color='green' if row['green_score'] >= 25 else 'red')
        ).add_to(marker_cluster)

    folium.LayerControl().add_to(map_breda)
    Geocoder().add_to(map_breda)

    return map_breda

def main():
    """
    The main function that runs the Streamlit application.
    """
    file_path = 'C:/Users/kacpe/Documents/2022-23d-1fcmgt-reg-ai-01-KacperJanczyk220646/usecase/greenlivability_final.csv'
    merged_df = load_data(file_path)

    st.sidebar.title("Map Options")

    years = merged_df['year'].unique()
    selected_year = st.sidebar.selectbox("Select Year", years)

    filtered_df = merged_df[merged_df['year'] == selected_year]

    zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=18, value=12)

    map_breda = create_map(filtered_df, zoom_level)

    st_folium.folium_static(map_breda)

if __name__ == '__main__':
    main()
