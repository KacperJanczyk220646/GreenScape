import unittest
from unittest.mock import patch
import pandas as pd
from MachineLearning import load_data, train_model, predict_score

class TestApp(unittest.TestCase):
    def setUp(self):
        """
        Set up the test data.

        This method is called before each test case is executed.

        It initializes a sample DataFrame that represents the test data.

        """
        self.df = pd.DataFrame({
            'year_x': [2022],
            'livability_score_x': [2.5],
            'TotalHouses': [90000],
            'Population': [3500],
            'income': [2800],
            'working_population': [2600],
            'total_job_growth': [-0.02],
            'green_score': [70]
        })
    
    def test_load_data(self):
        """
        Test the load_data function.

        This test case verifies that the load_data function correctly loads the data from a CSV file.

        It patches the pandas.read_csv function to return the sample DataFrame,
        calls the load_data function, and checks if the returned DataFrame is equal to the sample DataFrame.

        """
        with patch('pandas.read_csv', return_value=self.df) as mock_read_csv:
            data = load_data()
            mock_read_csv.assert_called_once_with('C:/Users/kacpe/Documents/2022-23d-1fcmgt-reg-ai-01-KacperJanczyk220646/Deployment/MLtask.csv')
            self.assertEqual(data.equals(self.df), True)
    
    def test_train_model(self):
        """
        Test the train_model function.

        This test case verifies that the train_model function correctly trains a machine learning model.

        It prepares the input features and target variable from the sample DataFrame,
        calls the train_model function, and checks if the returned model is not None,
        and if it has the expected number of estimators and random state.

        """
        X_train = self.df.drop('green_score', axis=1)
        y_train = self.df['green_score']
        model = train_model(X_train, y_train)
        self.assertIsNotNone(model)
        self.assertEqual(model.n_estimators, 100)
        self.assertEqual(model.random_state, 42)
    
    def test_predict_score(self):
        """
        Test the predict_score function.

        This test case verifies that the predict_score function correctly predicts the green score.

        It trains a model using the sample DataFrame, prepares new data for prediction,
        calls the predict_score function, and checks if the predicted score is within a certain tolerance.

        """
        X_train = self.df.drop('green_score', axis=1)
        y_train = self.df['green_score']
        model = train_model(X_train, y_train)
        new_data = pd.DataFrame({
            'year_x': [2023],
            'livability_score_x': [3.0],
            'TotalHouses': [80000],
            'Population': [4000],
            'income': [3000],
            'working_population': [2700],
            'total_job_growth': [-0.01]
        })
        predicted_score = predict_score(model, new_data)
        self.assertAlmostEqual(predicted_score, 70.0, places=2)

if __name__ == '__main__':
    unittest.main()
