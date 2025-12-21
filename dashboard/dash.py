import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

url = 'https://raw.githubusercontent.com/denis-hwk/tech_challenge_fase_4_9dtat/refs/heads/main/Obesity.csv'
df = pd.read_csv(url, delimiter = ',')

def arredondar_colunas(df, colunas):

    # Converte string para lista se necessário
    if isinstance(colunas, str):
        colunas = [colunas]

    # Verifica se todas as colunas existem no DataFrame
    colunas_inexistentes = [col for col in colunas if col not in df.columns]
    if colunas_inexistentes:
        raise ValueError(f"Colunas não encontradas no DataFrame: {colunas_inexistentes}")

    # Arredonda cada coluna
    for coluna in colunas:
        # Arredonda os valores
        df[coluna] = df[coluna].round(0).astype('Int64')

    return df

df_modelo = df.copy()
arredondar_colunas(df_modelo, ['FCVC', 'NCP', 'CH2O', 'FAF', 'TUE'])

dict_obesity = {
    'Insufficient_Weight': 'Abaixo do peso',
    'Normal_Weight': 'Peso normal',
    'Overweight_Level_I': 'Sobrepeso',
    'Overweight_Level_II': 'Sobrepeso',
    'Obesity_Type_I': 'Obesidade',
    'Obesity_Type_II': 'Obesidade',
    'Obesity_Type_III': 'Obesidade'
    }

dict_gender = {
    'Male': 'Masculino',
    'Female': 'Feminino'
    }

dict_family_history = {
    'yes': 'Sim',
    'no': 'Não'
    }

dict_caec = {
    'no': 'Não',
    'Sometimes': 'Às vezes',
    'Frequently': 'Frequentemente',
    'Always': 'Sempre'
    }

dict_smoke = {
    'no': 'Não',
    'yes': 'Sim'
    }

dict_favc = {
    'no': 'Não',
    'yes': 'Sim'
    }

dict_scc = {
    'no': 'Não',
    'yes': 'Sim'
    }

dict_calc = {
    'no': 'Não',
    'Sometimes': 'Às vezes',
    'Frequently': 'Frequentemente',
    'Always': 'Sempre'
    }

dict_mtrans = {
    'Automobile': 'Automóvel',
    'Bike': 'Bicicleta',
    'Motorbike': 'Motocicleta',
    'Public_Transportation': 'Transporte público',
    'Walking': 'Caminhada'
    }

df_modelo['Obesity'] = df_modelo['Obesity'].map(dict_obesity)
df_modelo['Gender'] = df_modelo['Gender'].map(dict_gender)
df_modelo['family_history'] = df_modelo['family_history'].map(dict_family_history)
df_modelo['CAEC'] = df_modelo['CAEC'].map(dict_caec)
df_modelo['SMOKE'] = df_modelo['SMOKE'].map(dict_smoke)
df_modelo['CALC'] = df_modelo['CALC'].map(dict_calc)
df_modelo['MTRANS'] = df_modelo['MTRANS'].map(dict_mtrans)
df_modelo['SCC'] = df_modelo['SCC'].map(dict_scc)
df_modelo['FAVC'] = df_modelo['FAVC'].map(dict_favc)

############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Dashboard para Análise de Dados sobre Obesidade </h1>", unsafe_allow_html = True)

# Gráfico de gênero
st.write('### Sexo Biológico')

fig_gender = px.histogram(
    df_modelo, 
    x='Obesity', 
    color='Gender', 
    barmode='stack',
    title='Distribuição de Pessoas por Gênero e Nível de Obesidade',
    labels={
        'Obesity': 'Nível de Obesidade',
        'Gender': 'Gênero'
        },
    color_discrete_map={
        'Masculino': 'lightseagreen', 
        'Feminino': 'lightcoral'
        },
    category_orders={
        "Obesity": ['Abaixo do peso',
                    'Peso normal',
                    'Sobrepeso',
                    'Obesidade']
        }
    )

fig_gender.update_layout(
    xaxis_tickangle=-45,
    yaxis_title='Quantidade de pessoas',
    legend_title='Sexo biológico'
    )

st.plotly_chart(fig_gender, use_container_width=True)

