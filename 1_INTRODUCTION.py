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
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Team Members","Business Understanding", "DS&AI tools to meet Business Case", "Business metrics to DS/AI metrics", "AI Canvas", "Roadmap"])

    with tab1:
        st.header("Our team")
        image4 = Image.open(
            "app/greenscape/Streamlit/Data/Our_team.png")
        st.image(image4, width=800)

    with tab2:
        st.header("Business Understanding")
        st.write("By analyzing the factors that have an impact on the Green Index score, the client can allocate resources efficiently and effectively to address the most pressing environmental challenges. By tracking changes in each factor over time, Breda can set realistic goals and monitor its progress toward becoming more sustainable in a completely data-driven manner. We will analyze the correlation between Quality of life, Public Safety, Segregation, and Environmental statistics with the green index score to determine if we are able to predict a green index score using regression task for each neighborhood in Breda.")
        st.subheader("Research questions:")
        st.write("1. What are the factors that contribute to the green index score?")
        st.write("2. Based on these factors, can we predict a green index score?")
        
        # Define the metrics
        metrics = [
            {
                "Metric": "Green Score Index",
                "Description": "Quantifies the percentage of greenery in Breda based on 3D photos from Google Street View",
                "Elaboration": "Utilizes computer vision algorithms to analyze images and calculate the green score index",
            },
            {
                "Metric": "Livability Score",
                "Description": "Evaluates the quality of life in different neighborhoods of Breda",
                "Elaboration": "Considers factors like access to green spaces, air quality, safety, and transportation",
            },
            {
                "Metric": "Total Amount of Houses",
                "Description": "Refers to the count of residential properties in Breda",
                "Elaboration": "Provides insights into population density and distribution across the city",
            },
            {
                "Metric": "Registered Nuisance",
                "Description": "Refers to the number of complaints or reports filed by residents regarding environmental nuisances",
                "Elaboration": "Helps identify areas where improvements in greenery can mitigate environmental concerns",
            },
            {
                "Metric": "Population per Neighborhood",
                "Description": "Refers to the average number of residents in specific areas or districts of Breda",
                "Elaboration": "Helps identify areas where additional green spaces may be necessary",
            },
            {
                "Metric": "Average Income",
                "Description": "Refers to the mean income level of residents in Breda",
                "Elaboration": "Provides insights into the socioeconomic factors influencing green space accessibility",
            },
            {
                "Metric": "Job Growth",
                "Description": "Refers to the rate at which new employment opportunities are created in Breda",
                "Elaboration": "Assesses the impact of green initiatives on the local economy",
            },
            {
                "Metric": "Electricity Consumption",
                "Description": "Measures the amount of electricity used by households and businesses in Breda",
                "Elaboration": "Highlights areas for energy efficiency improvements and renewable energy adoption",
            },
            {
                "Metric": "Gas Consumption",
                "Description": "Measures the amount of natural gas used by households and businesses in Breda",
                "Elaboration": "Identifies areas for green building practices and energy conservation measures",
            },
            {
                "Metric": "CO2 Emissions",
                "Description": "Refers to the amount of carbon dioxide released into the atmosphere in Breda",
                "Elaboration": "Monitors progress in reducing greenhouse gas emissions and promoting sustainability",
            },
        ]
    with tab3:
        # Display the metrics in a Streamlit app
        st.title("Business Metrics for Greenery Improvement in Breda")

        st.write("Below are the metrics used to measure the success of the greenery improvement project:")

        for metric in metrics:
            st.subheader(metric["Metric"])
            st.write("**Description:**", metric["Description"])
            st.write("**Elaboration:**", metric["Elaboration"])
            st.write("---")
    with tab4:
        # Define the tools and resources
        tools_resources = [
            "Data Visualization Tools: Visualization tools like Tableau, Power BI, or Matplotlib can be used to create interactive and informative visualizations that showcase the impact of green initiatives on various metrics. For example, in case of working with CSV files, we will use python libraries such as pandas and numpy, to preprocess data. Later on, to visualise it, libraries such as plotly, matplotlib or folium can be used for an interactive way of engaging with data. These tools facilitate effective communication of data-driven insights to stakeholders and decision-makers.",
            "Machine Learning and AI Algorithms: Machine learning and AI algorithms can be utilized for tasks such as data analysis. For example, for Machine Learning task, library such as scikit-learn will be crucial for the project, since it enables us to create a model. Regression tasks such as Linear Regression, Random Forest regressor are necessary, because based on their evaluation scores we can choose the best performing model.",
            "Open Data Sources: Leveraging open data sources, such as Breda in Cijfers website, can provide valuable information on factors like population per neighborhood, amount of houses in Breda etc. These sources can aid in understanding the existing environmental conditions and identifying opportunities for improvement.",
            "Collaborative Platforms: Collaborative platforms like GitHub or GitLab can facilitate team collaboration and version control of code and data. They enable data scientists and AI practitioners to work together efficiently and ensure reproducibility of analyses.",
            "CLient Engagement: Engagement with Data Science Team can lead to improvement on understand the case of why this project is done. It helps identifying, what Municipality of Breda really wants, to improve the whole city of Breda."
        ]

        # Display the tools and resources in a Streamlit app
        st.title("Tools and Resources for Meeting Business Case")

        st.write("Below are the tools and resources that can be utilized to meet the business requirements of improving greenery in Breda:")

        for item in tools_resources:
            st.write("- " + item)

    with tab5:
        st.header("AI Canvas")
        image2 = Image.open("app/greenscape/Streamlit/Data/AI_Canvas.png")
        st.image(image2)

    with tab6:
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



if __name__ == "__main__":
    main()
