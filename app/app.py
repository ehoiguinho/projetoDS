import streamlit as st
import pandas as pd
import joblib

kmeans = joblib.load('model/kmeans_model.pkl')

scaler = joblib.load('model/scaler.pkl')

st.set_page_config(
    page_title='Clusterização de Clientes',
    layout='centered'
)


# TITULO

st.title('Sistema de Segmentação de Clientes')

st.write(
    'Esta aplicação utiliza K-Means para identificar '
    'o perfil financeiro de um cliente.'
)

# ENTRADA

idade = st.slider(
    'Idade',
    18,
    75,
    30
)

sexo = st.selectbox(
    'Sexo',
    ['male', 'female']
)

job = st.selectbox(
    'Tipo de Trabalho',
    [0, 1, 2, 3]
)

housing = st.selectbox(
    'Moradia',
    ['own', 'rent', 'free']
)

saving = st.selectbox(
    'Conta Poupança',
    ['little', 'moderate', 'quite rich', 'rich']
)

checking = st.selectbox(
    'Conta Corrente',
    ['little', 'moderate', 'rich']
)

credit_amount = st.number_input(
    'Valor do Crédito',
    100,
    100000,
    5000
)

duration = st.slider(
    'Duração do Empréstimo',
    1,
    72,
    12
)

purpose = st.selectbox(
    'Finalidade',
    [
        'car',
        'radio/TV',
        'furniture/equipment',
        'business',
        'education',
        'repairs'
    ]
)


# MAPEAMENTO MANUAL

sexo_map = {
    'male': 1,
    'female': 0
}

housing_map = {
    'own': 0,
    'rent': 1,
    'free': 2
}

saving_map = {
    'little': 0,
    'moderate': 1,
    'quite rich': 2,
    'rich': 3
}

checking_map = {
    'little': 0,
    'moderate': 1,
    'rich': 2
}

purpose_map = {
    'car': 0,
    'radio/TV': 1,
    'furniture/equipment': 2,
    'business': 3,
    'education': 4,
    'repairs': 5
}

# BOTÃO

if st.button('Identificar Cluster'):

    dados = pd.DataFrame({
        'Age': [idade],
        'Sex': [sexo_map[sexo]],
        'Job': [job],
        'Housing': [housing_map[housing]],
        'Saving accounts': [saving_map[saving]],
        'Checking account': [checking_map[checking]],
        'Credit amount': [credit_amount],
        'Duration': [duration],
        'Purpose': [purpose_map[purpose]]
    })

    dados_normalizados = scaler.transform(dados)

    cluster = kmeans.predict(dados_normalizados)

    st.success(
        f'O cliente pertence ao Cluster {cluster[0]}'
    )
    
    #PERFIL

    if cluster[0] == 0:
        st.info(
            'Perfil: Clientes jovens com crédito moderado.'
        )

    elif cluster[0] == 1:
        st.info(
            'Perfil: Clientes com alto volume de crédito.'
        )

    else:
        st.info(
            'Perfil: Clientes com perfil financeiro conservador.'
        )