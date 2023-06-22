import streamlit as st
import streamlit_folium as st_folium
import folium
from folium.plugins import MarkerCluster, Geocoder
import pandas as pd

# Set the title and subheaders for the Streamlit application
st.title("Green Index Score Map - distribution within Gemeente Breda")
st.subheader(
    "This map represents green index score points for individual geographical coordinates on the map of Breda."
)
st.subheader("This map was created using Folium library in Python!")

# Function to load data from a CSV file and return it as a DataFrame


@st.cache_data
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


# Function to create a folium map with markers representing neighborhoods and their information


def create_map(filtered_df, zoom_level):
    """
    Creates a folium map with markers representing neighborhoods and their information.

    Parameters:
        filtered_df (pandas.DataFrame): The filtered dataframe containing neighborhood information.
        zoom_level (int): The initial zoom level of the map.

    Returns:
        folium.Map: The created folium map.
    """
    # Create the initial map centered at the coordinates of Breda
    map_breda = folium.Map(location=[51.5886, 4.7754], zoom_start=zoom_level)

    # Create a marker cluster for efficient rendering of many markers
    marker_cluster = MarkerCluster().add_to(map_breda)

    # HTML and CSS for the legend displayed on the map
    legend_html = """
    <div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background-color: white; padding: 10px; border: 1px solid black;">
        <p><strong>Legend</strong></p>
        <p><i class="fa fa-circle" style="color:green"></i> Green Score >= 25</p>
        <p><i class="fa fa-circle" style="color:red"></i> Green Score < 25</p>
    </div>
    """

    legend_css = """
    <style>
    .fa {
        margin-right: 5px;
    }
    </style>
    """

    # Add the legend to the map
    map_breda.get_root().header.add_child(folium.Element(legend_css + legend_html))

    # Add markers for each neighborhood in the filtered DataFrame
    for index, row in filtered_df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"Neighborhood: {row['neighborhood_name']}<br>Population: {row['Population']}<br>Total Houses: {row['TotalHouses']}<br>Date of measurement: {row['date']}",
            icon=folium.Icon(color="green" if row["green_score"] >= 25 else "red"),
        ).add_to(marker_cluster)

    # Add layer control and geocoder to the map
    folium.LayerControl().add_to(map_breda)
    Geocoder().add_to(map_breda)

    return map_breda


# Main function that runs the Streamlit application


def main():
    """
    The main function that runs the Streamlit application.
    """
    # Path to the CSV file containing the data
    file_path = "EDA/Kacper/greenlivability_final.csv"
    merged_df = load_data(file_path)

    # Create a sidebar with map options
    st.sidebar.title("Map Options")

    # Select a year from the available options
    years = merged_df["year"].unique()
    selected_year = st.sidebar.selectbox("Select Year", years)

    # Filter the data based on the selected year
    filtered_df = merged_df[merged_df["year"] == selected_year]

    # Slider to adjust the zoom level of the map
    zoom_level = st.sidebar.slider("Zoom Level", min_value=1, max_value=18, value=12)

    # Create the map using the filtered data and zoom level
    map_breda = create_map(filtered_df, zoom_level)

    # Display the map in the Streamlit app
    st_folium.folium_static(map_breda)


if __name__ == "__main__":
    main()
