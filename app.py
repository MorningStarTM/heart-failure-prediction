import streamlit as st

st.title("Heart Attack Prediction")

#Widget for getting Data
age = st.text_input('Your Age', placeholder="40")
cp = st.selectbox('Chest Pain', ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])
rbp = st.text_input('Resting blood pressure', placeholder="in mm Hg")
ch = st.text_input('Cholestoral', placeholder="in mg/dl fetched via BMI sensor")
st.write('Fasting blood sugar > 120 mg/dl')
col1, col2 = st.columns(2)
with col1:
    one = st.checkbox("Yes")
with col2:
    zero = st.checkbox("No")
rer = st.selectbox("Resting electrocardiographic results", ["normal", "having ST-T wave abnormality ", "showing probable or definite left ventricular hypertrophy by Estes' criteria"])
hr = st.text_input("Maximum heart rate achieved")

btn = st.button('Submit',)
