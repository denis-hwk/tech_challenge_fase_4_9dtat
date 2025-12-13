#Importação das bibliotecas
import streamlit as st 
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib
from joblib import load


############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Formulário para Avaliação de Obesidade</h1>", unsafe_allow_html = True)

st.warning('Preencha o formulário com todos os seus dados pessoais e clique no botão **ENVIAR** no final da página.')

# Gênero
st.write('### Sexo Biológico')
input_gender_male = st.radio('Qual é o seu sexo biológico?', ['Masculino','Feminino'], index=0)
input_gender_male_dict = {'Masculino': 1, 'Feminino':0}
input_gender_male = input_gender_male_dict.get(input_gender_male)

# Idade
st.write('### Idade')
input_age = float(st.slider('Qual é a sua idade', 18, 100))

# Altura
st.write('### Altura')
input_height = float(st.text_input('Digite a sua altura (em metros) e pressione ENTER para confirmar. Exemplo: 1.89', 0))

# Peso
st.write('### Peso')
input_height = float(st.text_input('Digite o seu peso (em kg) e pressione ENTER para confirmar. Exemplo: 90', 0))

# Histórico Familiar
st.write('### Histórico Familiar')
input_family_history = st.radio('Você possui alguma pessoa com obesidade na sua família?',['Sim','Não'], index=0)
input_family_history_dict = {'Sim': 1, 'Não':0}
input_family_history = input_family_history_dict.get(input_family_history)

# Consumo Frequente de Alimentos com alta quantidade de calorias
st.write('### Consumo frequente de alimentos com alta quantidade de calorias')
input_favc = st.radio('Você consome frequentemente alimentos com altas quantidades de calorias?',['Sim','Não'], index=0)
input_favc_dict = {'Sim': 1, 'Não':0}
input_favc = input_favc_dict.get(input_favc)

# Consumo de vegetais nas refeições
st.write('### Consumo de vegetais nas refeições')
input_favc = st.selectbox('Você consome vegetais com frequência?', ['Raramente', 'Às vezes', 'Sempre'])
input_favc_dict = {'Raramente': 1, 'Às vezes':2, 'Sempre': 3}
input_favc = input_favc_dict.get(input_favc)