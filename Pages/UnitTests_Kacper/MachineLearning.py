import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

@st.cache_data
def load_data():
    """
    Load the dataframe from a CSV file.
    
    Returns:
        pd.DataFrame: The loaded dataframe.
    """
    st.set_option('deprecation.showfileUploaderEncoding', False)
    df = pd.read_csv('C:/Users/kacpe/Documents/2022-23d-1fcmgt-reg-ai-01-KacperJanczyk220646/Deployment/MLtask.csv')
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
    st.set_option('deprecation.showfileUploaderEncoding', False)
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
    st.set_option('deprecation.showfileUploaderEncoding', False)
    return model.predict(new_data)[0]

def create_app():
    """
    Create a Streamlit app for green score prediction.
    """
    st.title("Green Score Prediction")
    
    # Load the dataframe
    df = load_data()

    # Select the features and target variable
    features = ['year_x', 'livability_score_x', 'TotalHouses', 'Population', 'income', 'working_population', 'total_job_growth']
    target = 'green_score'

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Create input fields for the desired values
    year_x = st.slider("Year", min_value=2000, max_value=2025, step=1, value=2022)
    livability_score_x = st.slider("Livability Score", min_value=0.0, max_value=10.0, step=0.01, value=2.5)
    total_houses = st.slider("Total Houses", min_value=0, step=1, value=90000)
    population = st.slider("Population", min_value=0, step=1, value=3500)
    income = st.slider("Income", min_value=0, step=1, value=2800)
    working_population = st.slider("Working Population", min_value=0, step=1, value=2600)
    total_job_growth = st.slider("Total Job Growth", min_value=-1.0, max_value=1.0, step=0.001, value=-0.02)

    # Create a dataframe with the new values
    new_data = pd.DataFrame({
        'year_x': [year_x],
        'livability_score_x': [livability_score_x],
        'TotalHouses': [total_houses],
        'Population': [population],
        'income': [income],
        'working_population': [working_population],
        'total_job_growth': [total_job_growth]
    })

    # Predict the green score
    predicted_score = predict_score(model, new_data)
    formatted_score = f"{round(predicted_score, 2)}%"
    styled_score = f'<span style="color: LightGreen; font-size:35px;">{formatted_score}</span>'
    st.subheader("Predicted green score:")
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

if __name__ == '__main__':
    create_app()
