import streamlit as st
from PIL import Image

st.title("Project for improving Green score in Breda (GreenScape)")
image1 = Image.open(r"C:\Users\User\Desktop\GreenScape\EDA\Yuliia\Intro page for streamlit\park.png")
st.image(image1)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Business Understanding", "AI Canvas", "Roadmap", "Team members", "Conclusion"])

def main():
    with tab1:
        st.header("Business Understanding")
        st.write("By analyzing the factors that have an impact on the Green Index score, the client can allocate resources efficiently and effectively to address the most pressing environmental challenges. By tracking changes in each factor over time, Breda can set realistic goals and monitor its progress toward becoming more sustainable in a completely data-driven manner. We will analyze the correlation between Quality of life, Public Safety, Segregation, and Environmental statistics with the green index score to determine if we are able to predict a green index score using regression task for each neighborhood in Breda.")
        st.subheader("Research questions:")
        st.write("1. What are the factors that contribute to the green index score?")
        st.write("2. Based on these factors, can we predict a green index score?")

    with tab2:
        st.header("AI Canvas")
        image2 = Image.open(r"C:\Users\User\Desktop\GreenScape\EDA\Yuliia\Intro page for streamlit\AI Canvas.png")
        st.image(image2)

    with tab3:
        st.header("Project's Roadmap")
        image3 = Image.open(r"C:\Users\User\Desktop\GreenScape\EDA\Yuliia\Intro page for streamlit\Roadmap_Image.png")
        st.image(image3)

    with tab4:
        st.header("Our team")
        image4 = Image.open(r"C:\Users\User\Desktop\GreenScape\EDA\Yuliia\Intro page for streamlit\Our team.png")
        st.image(image4, width = 800)


    with tab5:
        st.header("Conclusion")
        st.divider()
        st.write('The model is able to predict a change in green score according to a change of value in one of the selected criterias. However, we would like to highlight the central pain-point with any project of this nature.')
        st.divider()
        st.subheader('Correlation does not equal Causation.')
        st.divider()
        st.write('Even though the algorithm predicts a change in value if average income value increases, it does not mean that the change in green score is a direct consequence of a higher average salary.')
        st.write('We realize this is due to the fact that green score is calculated based on the total amount of green area visible in a geographic region.')
        st.write('Despite this, we believe that the factors presented in the algorithm go a long way in enabling more green areas being added to certain neighborhoods.')

if __name__ == "__main__":
    main()