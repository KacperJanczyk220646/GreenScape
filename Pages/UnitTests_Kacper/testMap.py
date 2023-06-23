import unittest
import pandas as pd
import folium

# Import the functions to be tested
from Map import load_data, create_map

class TestScript(unittest.TestCase):
    def test_load_data(self):
        """
        Test the load_data function.

        This test case verifies that the load_data function correctly loads a CSV file into a DataFrame.

        It creates a sample CSV string to simulate the file data, loads the sample data into a DataFrame,
        and compares it with the expected DataFrame.

        The function being tested:
        - load_data(file_path: str) -> pd.DataFrame

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: The loaded DataFrame.
        """
        # Create a sample CSV string to simulate the file data
        csv_data = 'C:/Users/kacpe/Documents/2022-23d-1fcmgt-reg-ai-01-KacperJanczyk220646/usecase/greenlivability_final.csv'

        # Load the sample data into a DataFrame
        expected_df = pd.read_csv(csv_data)

        # Call the load_data function and check if the returned DataFrame is equal to the expected DataFrame
        file_path = 'C:/Users/kacpe/Documents/2022-23d-1fcmgt-reg-ai-01-KacperJanczyk220646/usecase/greenlivability_final.csv'
        actual_df = load_data(file_path)
        pd.testing.assert_frame_equal(actual_df, expected_df)

    def test_create_map(self):
        """
        Test the create_map function.

        This test case verifies that the create_map function correctly creates a folium.Map object based on the provided DataFrame.

        It creates a sample DataFrame to be used in the create_map function, calls the function with the DataFrame and a zoom level,
        and checks if the returned object is an instance of folium.Map.

        The function being tested:
        - create_map(data: pd.DataFrame, zoom_level: int) -> folium.Map

        Args:
            data (pd.DataFrame): The DataFrame containing location and attribute data.
            zoom_level (int): The initial zoom level of the map.

        Returns:
            folium.Map: The created folium.Map object.
        """
        # Create a sample DataFrame to be used in the create_map function
        df = pd.DataFrame({
            'neighborhood_name': ['Neighborhood 1', 'Neighborhood 2'],
            'latitude': [51.5886, 51.5896],
            'longitude': [4.7754, 4.7764],
            'Population': [1000, 2000],
            'TotalHouses': [200, 400],
            'green_score': [30, 20],
            'date': ['2023-06-19', '2023-06-19']
        })

        # Call the create_map function and check if it returns a folium.Map object
        zoom_level = 12
        map_obj = create_map(df, zoom_level)
        self.assertIsInstance(map_obj, folium.Map)

if __name__ == '__main__':
    unittest.main()
