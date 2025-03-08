import numpy as np 
import pandas as pd 
import streamlit as st
import pickle 
import google.generativeai as genai 
dt=pd.read_csv('processed_dataset.csv')
st.title("Planet Habitability Index Prediction")
selected_name = st.selectbox("Select a planet name:", dt['P_NAME'].unique())
if selected_name:
  filtered_dt = dt[dt['P_NAME'] == selected_name] 
  with open('model.pkl', 'rb') as file:  

    model = pickle.load(file)  
  row=filtered_dt
  feature_names = ['ESI','Atmospheric_Retention','Long_Term_Stability']  # Get only relevant columns used by the model 
  feature_values = row[feature_names].values
  # Extract importance values from the model
  importance_values = model.feature_importances_
  # Map feature importance to the selected features
  feature_importance_dict = dict(zip(model.feature_names_in_, importance_values))

  # Keep only the important features used in the row
  feature_importance_selected = {col: feature_importance_dict[col] for col in feature_names}

  # Compute weighted sum (prediction)
  prediction = np.sum(feature_values * np.array([feature_importance_selected[col] for col in feature_names]))
  # Create a dictionary of feature names, values, and importance
  feature_importances_dict = {
      col: {"value": row[col], "importance": feature_importance_selected[col]}
      for col in feature_names
  } 
  def generate_llm_prompt_from_row(row: pd.Series, prediction: float, feature_importances: dict) -> str:
      """
      Generate a prompt string to be sent to an LLM for explanation.
      
      Parameters:
          row (pd.Series): The original row from a DataFrame.
          prediction (float): The habitability index predicted by the model.
          feature_importances (dict): Dictionary containing feature values and their importance scores.
          
      Returns:
          str: A formatted prompt string.
      """
      prompt_lines = ["Planet Data and Prediction Details:\n"]
      
      # Append each feature with its value and importance
      for feature, details in feature_importances.items():
          prompt_lines.append(f"{feature}: {details['value']} (Importance: {details['importance']:.4f})")
      
      # Add the prediction details and context
      prompt_lines.append(f"\nPrediction (Habitability Index): {prediction:.2f}")
      prompt_lines.append(
          "\nNote: The prediction represents the habitability index of the planet. "
          "A value close to 100 indicates a very high likelihood of habitability, meaning the planet is considered highly favorable for sustaining life. "
          "Similarly, for the provided metrics, values closer to 100 are regarded as very good."
      )
      
      # Ask the LLM for a detailed explanation
      prompt_lines.append(
          "\nBased on the above data, please provide a detailed explanation of why the model might have arrived at this prediction."
      )
      
      return "\n".join(prompt_lines)

  # Generate prompt
  prompt = generate_llm_prompt_from_row(row, prediction, feature_importances_dict)
  genai.configure(api_key="AIzaSyCLt5tuA_m6kaIyxK0KP2NtgM4mbELT-2o")
  model = genai.GenerativeModel("gemini-1.5-flash") 
  response = model.generate_content(prompt)
  response=response.text 
  col1, col2, col3 = st.columns([1, 1, 2])

  with col1:
    st.markdown("**Name**")
    st.write(selected_name)

  with col2:
    st.markdown("**Habitability Index**")
    st.write(prediction)

  with col3:
    st.markdown("**Reason**")
    st.write(response)
