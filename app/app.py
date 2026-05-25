import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load('../model/modelo_credito.pkl')

st.title('Sistema de Previsão de Inadimplência')

idade = st.slider('Idade', 18, 75, 30)
valor_credito = st.number_input('Valor do Crédito', 1000, 100000, 5000)
duracao = st.slider('Duração do Empréstimo', 1, 72, 12)

sexo = st.selectbox('Sexo', ['male', 'female'])

sexo = 1 if sexo == 'male' else 0

entrada = pd.DataFrame({
    'Age': [idade],
    'Sex': [sexo],
    'Job': [1],
    'Housing': [1],
    'Saving accounts': [1],
    'Checking account': [1],
    'Credit amount': [valor_credito],
    'Duration': [duracao],
    'Purpose': [1]
})

if st.button('Realizar Previsão'):
    previsao = modelo.predict(entrada)

    if previsao[0] == 1:
        st.error('Cliente com alto risco de inadimplência')
    else:
        st.success('Cliente com baixo risco de inadimplência')