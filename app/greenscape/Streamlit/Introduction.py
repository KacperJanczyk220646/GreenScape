"""
Introduction Page for GreenScape Project in Streamlit

This script creates a Streamlit web page for the GreenScape project, which aims to improve the Green score in Breda. The page contains 5 multiple tabs, each displaying different information related to the project.

Usage:
    - Run the script to launch the introduction page in Streamlit.

Dependencies:
    - streamlit
    - PIL (Python Imaging Library)

"""

import streamlit as st
from PIL import Image


def main():
    """
    Main function to create the Streamlit page for the GreenScape project.
    """
    st.title("Project for improving Green score in Breda (GreenScape)")

    # Display image
    image1 = Image.open("app/greenscape/Streamlit/Data/park.png")
    st.image(image1)

    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Business Understanding", "AI Canvas", "Roadmap", "Team members", "Conclusion"])

    with tab1:
        st.header("Business Understanding")
        st.write("By analyzing the factors that have an impact on the Green Index score, the client can allocate resources efficiently and effectively to address the most pressing environmental challenges. By tracking changes in each factor over time, Breda can set realistic goals and monitor its progress toward becoming more sustainable in a completely data-driven manner. We will analyze the correlation between Quality of life, Public Safety, Segregation, and Environmental statistics with the green index score to determine if we are able to predict a green index score using regression task for each neighborhood in Breda.")
        st.subheader("Research questions:")
        st.write("1. What are the factors that contribute to the green index score?")
        st.write("2. Based on these factors, can we predict a green index score?")

    with tab2:
        st.header("AI Canvas")
        image2 = Image.open("app/greenscape/Streamlit/Data/AI_Canvas.png")
        st.image(image2)

    with tab3:
        st.header("Project's Roadmap")
        image3 = Image.open("app/greenscape/Streamlit/Data/Roadmap_Image.png")
        st.image(image3)
        st.subheader("Week 4: Business & Data Understanding")
        business_steps = [
            "Familiarize ourselves with the project goals and objectives. (including working with Trello workspace)",
            "Conduct meetings with the client to gain a deeper understanding of their requirements.",
            "Identify the key factors affecting the Green Index score (Quality of life, Public Safety, Segregation, Environmental statistics).",
            "Gather relevant data sources for each factor and understand their structure and format.",
            "Conduct exploratory data analysis (EDA) to gain insights into the data and identify any data quality issues or missing values."
        ]
        st.markdown(f"1. {business_steps[0]}")
        st.markdown(f"2. {business_steps[1]}")
        st.markdown(f"3. {business_steps[2]}")
        st.markdown(f"4. {business_steps[3]}")
        st.markdown(f"5. {business_steps[4]}")

        st.subheader("Week 5: Data Preparation")
        data_steps = [
            "Cleanse and preprocess the data to address any data quality issues, such as missing values, outliers, or inconsistencies.",
            "Perform feature engineering to create new variables or transformations that may improve the predictive power of the model.",
            "Integrate the data from different sources and ensure it is in a suitable format for modeling.",
            "Split the dataset into training, validation, and testing sets to evaluate the performance of the model accurately.",
            "Document the data preparation steps taken for transparency and reproducibility."
        ]
        st.markdown(f"1. {data_steps[0]}")
        st.markdown(f"2. {data_steps[1]}")
        st.markdown(f"3. {data_steps[2]}")
        st.markdown(f"4. {data_steps[3]}")
        st.markdown(f"5. {data_steps[4]}")

        st.subheader("Week 6: Modeling")
        modeling_steps = [
            "Select an appropriate regression algorithm to predict the Green Index score based on the identified factors.",
            "Train the regression model on the prepared dataset.",
            "Optimize the model by tuning hyperparameters and using techniques such as cross-validation.",
            "Evaluate the model's performance using appropriate evaluation metrics (e.g., mean squared error, R-squared).",
            "Consider ensemble methods or feature selection techniques to improve model performance if necessary."
        ]
        st.markdown(f"1. {modeling_steps[0]}")
        st.markdown(f"2. {modeling_steps[1]}")
        st.markdown(f"3. {modeling_steps[2]}")
        st.markdown(f"4. {modeling_steps[3]}")
        st.markdown(f"5. {modeling_steps[4]}")

        st.subheader("Week 7: Evaluation")
        evaluation_steps = [
            "Assess the model's predictive accuracy by comparing the predicted Green Index scores with the actual scores in the validation set.",
            "Perform additional analysis to understand the model's strengths and limitations.",
            "Identify any biases or limitations in the data and model, and discuss potential ways to mitigate them.",
            "Collaborate with the client to validate the model's usefulness in addressing their goals and requirements.",
            "Document the evaluation results and recommendations for future improvements."
        ]
        st.markdown(f"1. {evaluation_steps[0]}")
        st.markdown(f"2. {evaluation_steps[1]}")
        st.markdown(f"3. {evaluation_steps[2]}")
        st.markdown(f"4. {evaluation_steps[3]}")
        st.markdown(f"5. {evaluation_steps[4]}")

        # Week 8: Deployment
        st.subheader("Week 8: Deployment")
        deployment_steps = [
            "Finalize the regression model based on the evaluation and feedback received.",
            "Apply the trained model to predict the Green Index scores for each neighborhood in Breda.",
            "Generate a comprehensive report summarizing the findings, including the model's performance, feature importance, and insights into the factors affecting the Green Index score.",
            "Present the report to the client and stakeholders, explaining the results and potential implications for resource allocation and sustainability efforts.",
            "Provide recommendations on how to monitor and update the model in the future as new data becomes available.",
            "Collaborate with the client to develop an implementation plan for integrating the model into their decision-making processes."
        ]
        st.markdown(f"1. {deployment_steps[0]}")
        st.markdown(f"2. {deployment_steps[1]}")
        st.markdown(f"3. {deployment_steps[2]}")
        st.markdown(f"4. {deployment_steps[3]}")
        st.markdown(f"5. {deployment_steps[4]}")
        st.markdown(f"6. {deployment_steps[5]}")

    with tab4:
        st.header("Our team")
        image4 = Image.open(
            "app/greenscape/Streamlit/Data/Our_team.png")
        st.image(image4, width=800)

    with tab5:
        st.header("Conclusion")
        st.divider()
        st.write('The model is able to predict a change in green score according to a change of value in one of the selected criteria. However, we would like to highlight the central pain-point with any project of this nature.')
        st.divider()
        st.subheader('Correlation does not equal Causation.')
        st.divider()
        st.write('Even though the algorithm predicts a change in value if average income value increases, it does not mean that the change in green score is a direct consequence of a higher average salary.')
        st.write('We realize this is due to the fact that the green score is calculated based on the total amount of green area visible in a geographic region.')
        st.write('Despite this, we believe that the factors presented in the algorithm go a long way in enabling more green areas being added to certain neighborhoods.')


if __name__ == "__main__":
    main()
