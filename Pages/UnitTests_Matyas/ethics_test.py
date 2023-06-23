import streamlit as st
import base64
from ethics import displayPDF

def test_displayPDF():
    file_path = 'ETHICS/LegalEthics_Final.pdf'

    # Test file opening and base64 encoding
    with open(file_path, "rb") as f:
        expected_base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Mock the markdown display
    def mock_markdown(html, unsafe_allow_html=True):
        assert html == f'<iframe src="data:application/pdf;base64,{expected_base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        assert unsafe_allow_html is True

    st.markdown = mock_markdown

    # Call displayPDF function
    displayPDF(file_path)


# Run the unit test
test_displayPDF()

