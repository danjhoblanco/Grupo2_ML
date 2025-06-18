import streamlit as st
import pandas as pd
import pickle

# -------------------------
# Cargar modelo entrenado
# -------------------------
with open('heart_disease_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("💓 Predicción de Enfermedad Cardíaca")
st.write("Completa los datos del paciente (o usa los valores por defecto) para obtener una predicción.")

# -------------------------
# Entradas del usuario con valores por defecto que generan predicción = 1
# -------------------------
age = st.number_input("Edad", min_value=0, max_value=120, value=70)
sex = st.selectbox("Sexo", options={0: 'Femenino', 1: 'Masculino'}, index=1)
cp = st.selectbox("Tipo de dolor de pecho (cp)", options={0: 'Típico anginoso', 1: 'Angina atípica', 2: 'No anginoso', 3: 'Asintomático'}, index=3)
trestbps = st.number_input("Presión arterial en reposo (trestbps)", value=160)
chol = st.number_input("Colesterol sérico (chol)", value=320)
fbs = st.selectbox("¿Azúcar en sangre en ayunas > 120 mg/dl? (fbs)", options={0: 'No', 1: 'Sí'}, index=1)
restecg = st.selectbox("Resultados del electrocardiograma en reposo (restecg)", options={0: 'Normal', 1: 'Anormalidad ST-T', 2: 'Hipertrofia ventricular izquierda'}, index=2)
thalach = st.number_input("Frecuencia cardíaca máxima alcanzada (thalach)", value=100)
exang = st.selectbox("¿Angina inducida por ejercicio? (exang)", options={0: 'No', 1: 'Sí'}, index=1)
oldpeak = st.number_input("Depresión del ST inducida por ejercicio (oldpeak)", value=3.5)
slope = st.selectbox("Pendiente del segmento ST (slope)", options={0: 'Ascendente', 1: 'Plano', 2: 'Descendente'}, index=2)
ca = st.selectbox("Número de vasos principales (ca)", options=[0, 1, 2, 3], index=2)
thal = st.selectbox("Tipo de talasemia (thal)", options={0: 'Normal', 1: 'Fijo defecto', 2: 'Reversible defecto', 3: 'No especificado'}, index=2)

# -------------------------
# Botón para predecir
# -------------------------
if st.button("🔍 Predecir"):
    # Convertir entradas en DataFrame
    input_data = pd.DataFrame([{
        'age': age,
        'sex': 1 if sex == 'Masculino' else 0,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': 1 if fbs == 'Sí' else 0,
        'restecg': restecg,
        'thalach': thalach,
        'exang': 1 if exang == 'Sí' else 0,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }])

    # Predicción
    prediction = model.predict(input_data)[0]

    # Resultado directo
    st.subheader("🩺 Resultado:")
    st.write(f"**{int(prediction)}** → {'Presenta' if prediction == 1 else 'No presenta'} enfermedad cardíaca")
