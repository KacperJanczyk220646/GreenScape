import streamlit as st



with st.container():
    st.title('Conclusion')
    st.divider()
    
    st.write('The model is able to predict a change in green score according to a change of value in one of the selected criterias. However, we would like to highlight the central pain-point with any project of this nature.')
    st.divider()
    st.subheader('Correlation does not equal Causation.')
    st.divider()
    st.write('Even though the algorithm predicts a change in value if average income value increases, it does not mean that the change in green score is a direct consequence of a higher average salary.')
    st.write('We realize this is due to the fact that green score is calculated based on the total amount of green area visible in a geographic region.')
    st.write('Despite this, we believe that the factors presented in the algorithm go a long way in enabling more green areas being added to certain neighborhoods.')
