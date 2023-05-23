import streamlit as st
st.title("Heart Attack Prediction")



#Widget for getting Data
st.text_input('Your Age', placeholder="40")
st.selectbox('Chest Pain', ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])
st.text_input('Resting blood pressure', placeholder="in mm Hg")
st.text_input('Cholestoral', placeholder="in mg/dl fetched via BMI sensor")
st.write('Fasting blood sugar > 120 mg/dl')
col1, col2 = st.columns(2)
with col1:
    st.checkbox("Yes")
with col2:
    st.checkbox("No")
st.selectbox("Resting electrocardiographic results", ["normal", "having ST-T wave abnormality ", "showing probable or definite left ventricular hypertrophy by Estes' criteria"])
st.text_input("Maximum heart rate achieved")

st.button('Submit',)
