import streamlit as st
from PIL import Image

ethics_title = st.container()
ethics_overview = st.container()
ethics_explanation = st.container()

ethics_file = 'ETHICS/LegalEthics_Final.pdf'

with ethics_title:
    st.title('Ethical and Legal Assessment')
    st.divider()

with ethics_overview:
    
    st.header("What was included in the assessment?")
    st.write('Well, we believe talking about what was NOT included is a much simpler way to go.')

    text_column1, text_column2 = st.columns((1,1))
    with text_column1:
        st.write('The assessment was conducted according to the following frameworks:')
        st.markdown('- [Assessment List for Trustworthy Artificial Intelligence (ALTAI)](https://altai.insight-centre.org/)')
        st.markdown('- [Data Ethics Decision Aid (DEDA)](https://dataschool.nl/en/deda/)')

    with text_column2:
        altai_column, deda_column = st.columns((1,1))

        with altai_column:
            st.markdown('**Exclusions from ALTAI**')
            st.divider()
            st.markdown('- Parts of Human Autonomy and Oversight')
            st.markdown('- Parts of Diversity, Non-discrimination and Fairness')

        with deda_column:
            st.markdown('**Exclusions from DEDA**')
            st.divider()
            st.write('All components of DEDA have been Answered')
    st.divider()

with ethics_explanation:
    st.write('The core values observed and ensured through answering the DEDA framework are the following:')

    principles, explanations = st.columns((1,1))
    with principles:
        st.markdown('- Openness')
        st.markdown('- Respect for Autonomy')
        st.markdown('- Efficiency')
        st.markdown('- Integrity')
        st.markdown('- Inclusion')
        st.markdown('- Justice')
        st.markdown('- Legitimacy')

    with explanations:
        st.write('We believe that these core principles the DEDA framework is set out to ensure are synonymous with those of the ALTAI framework, even though the latter goes more in detail.')
        st.write('Since our project is not concerned with Personal Data, or other forms of sensitive information, privacy and data governance is not extensive. It is meant to be a decision-making aid/tool which does not affect Human autonomy in any way whatsoever. The algorithm does not operate autonomously, and has miniscule chances of causing adverse effects.')

def displayPDF(file):
    # Display PDF using <embed> tag in st.markdown
    st.markdown(f'<embed src="{file}" width="700" height="1000" type="application/pdf">', unsafe_allow_html=True)

displayPDF(ethics_file)

'''
with st.container():
    def displayPDF(file):
        # Opening file from file path
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
    '''

