import unittest
from unittest.mock import patch
from io import StringIO
import sys
from PIL import Image

# Import the module containing the `main` function
import INTRODUCTION

class TestGreenScapeApp(unittest.TestCase):
    @patch("streamlit.image")
    @patch("builtins.open")
    @patch("sys.stdout", new_callable=StringIO)
    def test_main(self, mock_stdout, mock_open, mock_st_image):
        # Mock the return value of the Image.open function
        mock_image = Image.new("RGB", (100, 100))
        mock_open.return_value.__enter__.return_value = mock_image

        # Capture the output of the main function
        with patch.object(sys, "argv", ["your_script_name.py"]):
            INTRODUCTION.main()

        # Assert that the expected output is printed
        self.assertIn("Project for improving Green score in Breda (GreenScape)", mock_stdout.getvalue())
        self.assertIn("Our team", mock_stdout.getvalue())
        self.assertIn("Business Understanding", mock_stdout.getvalue())
        self.assertIn("Business Metrics for Greenery Improvement in Breda", mock_stdout.getvalue())
        self.assertIn("Tools and Resources for Meeting Business Case", mock_stdout.getvalue())
        self.assertIn("AI Canvas", mock_stdout.getvalue())
        self.assertIn("Project's Roadmap", mock_stdout.getvalue())

        # Assert that the Image.open and st.image functions are called
        mock_open.assert_called_with("app/greenscape/Streamlit/Data/park.png")
        mock_st_image.assert_called_with(mock_image)

if __name__ == "__main__":
    unittest.main()