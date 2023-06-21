import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def main():
    tab1, tab2, tab3 = st.tabs(["ML Lifecycle", "ML App Demo", "Conclusion"])

    with tab1:
        # Problem Definition
        st.header("1. Problem Definition")
        st.write(
            "The project aims to analyze the factors impacting the Green Index score in Breda to help the client allocate resources effectively for addressing environmental challenges. The goal is to predict the Green Index score for each neighborhood using regression models based on factors such as Quality of life, Public Safety, Segregation, and Environmental statistics. The objective is to enable Breda to set realistic sustainability goals and monitor progress in a data-driven manner."
        )

        # Data Collection and Preprocessing
        st.header("2. Data Collection and Preprocessing")
        st.write(
            "The project starts with identifying the data requirements, including variables such as Quality of life, Public Safety, Segregation, Environmental statistics, and the Green Index score. Relevant data sources are identified and accessed, ensuring data quality and consistency. Data preprocessing techniques are applied to handle missing values, normalize variables, and address outliers."
        )

        # Exploratory Data Analysis (EDA)
        st.header("3. Exploratory Data Analysis (EDA)")
        st.write(
            "EDA is performed to gain insights into the data and understand the relationships between variables. Statistical summaries, data visualizations, and correlation analysis are used to identify patterns and determine the potential impact of each factor on the Green Index score. This analysis helps in feature selection and feature engineering."
        )

        # Feature Selection and Engineering
        st.header("4. Feature Selection and Engineering")
        st.write(
            "Feature selection techniques are applied to identify the most relevant variables that significantly impact the Green Index score. This step reduces dimensionality and focuses on the factors that contribute the most to sustainability. Feature engineering techniques, such as label encoding for categorical variables and feature scaling for numerical variables, are employed to prepare the data for model training."
        )

        # Model Selection and Training
        st.header("5. Model Selection and Training")
        st.write(
            "Different regression models, such as linear regression, decision tree regression, and random forest regression, are explored. Evaluation metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared are used to assess the performance of each model. Based on the evaluation, the Random Forest regressor is selected as the final model due to its superior prediction accuracy."
        )

        # Model Tuning and Validation
        st.header("6. Model Tuning and Validation")
        st.write(
            "The selected model is further refined through iterative processes. Hyperparameter tuning techniques, such as grid search or random search, are applied to optimize the model's parameters. Cross-validation techniques, like k-fold cross-validation, are utilized to obtain reliable performance estimates. The model is validated using separate test data to assess its generalization ability and confirm its accuracy."
        )

        # Interpretation and Insights
        st.header("7. Interpretation and Insights")
        st.write(
            "The final model, Random Forest regressor, provides feature importances, allowing for insights into the relative importance of factors influencing the Green Index score. This information helps in understanding the relationships and making informed decisions to improve sustainability efforts. Results are visualized and communicated effectively, potentially using techniques like partial dependence plots or permutation importance."
        )

        # Future Improvements
        st.header("8. Future Improvements")
        st.write(
            "To enhance the model's performance, future improvements can be considered. This includes conducting hyperparameter tuning, exploring additional features, employing ensemble learning methods, and using advanced interpretability techniques. Regular updates to the dataset and collaboration with domain experts ensure the model's accuracy and relevance over time. Error analysis helps identify areas for improvement, leading to enhanced performance and applicability of the model in improving the Green Index score in Breda."
        )

    with tab2:

        @st.cache_data
        def load_data():
            """
            Load the dataframe from a CSV file.

            Returns:
                pd.DataFrame: The loaded dataframe.
            """
            df = pd.read_csv("app/greenscape/Streamlit/Data/final_ML.csv")
            return df

        @st.cache_data
        def train_model(X_train, y_train):
            """
            Train the Random Forest model using the provided training data.

            Args:
                X_train (pd.DataFrame): The features of the training data.
                y_train (pd.Series): The target variable of the training data.

            Returns:
                RandomForestRegressor: The trained Random Forest model.
            """
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            return model

        def predict_score(model, new_data):
            """
            Predict the green score using the trained model and new data.

            Args:
                model (RandomForestRegressor): The trained Random Forest model.
                new_data (pd.DataFrame): The new data for prediction.

            Returns:
                float: The predicted green score.
            """
            return model.predict(new_data)[0]

        def create_app():
            """
            Create a Streamlit app for green score prediction.
            """
            st.title("Green Score Prediction")

            # Load the dataframe
            df = load_data()

            # Select the features and target variable
            features = [
                "reg_nuisance",
                "year",
                "livability_score",
                "houses_amount",
                "population",
                "income",
                "total_job_growth",
                "electricity_cons",
                "gas_cons",
                "co2_emi",
                "neighborhood_encoded",
            ]
            target = "green_score"

            # Split the dataset into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(
                df[features], df[target], test_size=0.2, random_state=42
            )

            # Train the model
            model = train_model(X_train, y_train)

            # Create a selectbox for neighborhood_encoded
            neighborhood_mapping = df[
                ["neighborhood_encoded", "neighborhood_name"]
            ].drop_duplicates()
            neighborhood_values = neighborhood_mapping["neighborhood_encoded"].unique()
            selected_neighborhood_encoded = st.selectbox(
                "Select neighborhood",
                neighborhood_values,
                format_func=lambda value: neighborhood_mapping.loc[
                    neighborhood_mapping["neighborhood_encoded"] == value,
                    "neighborhood_name",
                ].iloc[0],
            )

            # Get the corresponding neighborhood_name for the selected neighborhood_encoded
            selected_neighborhood_name = neighborhood_mapping.loc[
                neighborhood_mapping["neighborhood_encoded"]
                == selected_neighborhood_encoded,
                "neighborhood_name",
            ].iloc[0]

            # Create sliders for the features
            reg_nuisance = st.slider(
                "Registered nuisance (number)",
                min_value=0.0,
                max_value=1000.0,
                value=0.0,
            )
            year = st.slider("Year", min_value=2000.0, max_value=2050.0, value=0.0)
            livability_score = st.slider(
                "Livability Score", min_value=0.0, max_value=10.0, value=0.0
            )
            houses_amount = st.slider(
                "Amount of houses (In whole Breda)",
                min_value=0.0,
                max_value=200000.0,
                value=0.0,
            )
            population = st.slider(
                "Number of Population (per neighborhood)",
                min_value=0.0,
                max_value=50000.0,
                value=0.0,
            )
            income = st.slider(
                "Income (in Euros)", min_value=0.0, max_value=10000.0, value=0.0
            )
            total_job_growth = st.slider(
                "Job Growth (in percentage)",
                min_value=-100.0,
                max_value=100.0,
                value=0.0,
            )
            electricity_cons = st.slider(
                "Total Electricity Consuption (all homes, kWh)",
                min_value=0.0,
                max_value=5000.0,
                value=0.0,
            )
            gas_cons = st.slider(
                "Gas consuption (all homes, cubic meters)",
                min_value=0.0,
                max_value=5000.0,
                value=0.0,
            )
            co2_emi = st.slider(
                "CO2 emissions (from homes, in tonnes)",
                min_value=0.0,
                max_value=500000.0,
                value=0.0,
            )

            # Create a dataframe with the new values
            new_data = pd.DataFrame(
                {
                    "reg_nuisance": [reg_nuisance],
                    "year": [year],
                    "livability_score": [livability_score],
                    "houses_amount": [houses_amount],
                    "population": [population],
                    "income": [income],
                    "total_job_growth": [total_job_growth],
                    "electricity_cons": [electricity_cons],
                    "gas_cons": [gas_cons],
                    "co2_emi": [co2_emi],
                    "neighborhood_encoded": [selected_neighborhood_encoded],
                }
            )

            # Predict the green score
            predicted_score = predict_score(model, new_data)
            formatted_score = f"{round(predicted_score, 2)}%"
            styled_score = f'<span style="color: LightGreen; font-size:35px;">{formatted_score}</span>'
            st.subheader(f"Predicted green score for {selected_neighborhood_name}:")
            st.markdown(styled_score, unsafe_allow_html=True)

            # Make predictions on the test set
            y_pred = model.predict(X_test)

            # Calculate evaluation metrics
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            st.subheader("Evaluation Metrics:")
            st.markdown(f"Mean Squared Error (MSE): {mse}")
            st.markdown(f"Mean Absolute Error (MAE): {mae}")
            st.markdown(f"R-squared Score: {r2}")

        with tab3:
            st.header("Conclusion")
            st.divider()
            st.write(
                "The model is able to predict a change in green score according to a change of value in one of the selected criteria. However, we would like to highlight the central pain-point with any project of this nature."
            )
            st.divider()
            st.subheader("Correlation does not equal Causation.")
            st.divider()
            st.write(
                "Even though the algorithm predicts a change in value if average income value increases, it does not mean that the change in green score is a direct consequence of a higher average salary."
            )
            st.write(
                "We realize this is due to the fact that the green score is calculated based on the total amount of green area visible in a geographic region."
            )
            st.write(
                "Despite this, we believe that the factors presented in the algorithm go a long way in enabling more green areas being added to certain neighborhoods."
            )

    if __name__ == "__main__":
        create_app()
