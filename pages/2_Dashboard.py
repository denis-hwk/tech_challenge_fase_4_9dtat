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

col11, col21 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
############################ Gráfico de Sexo Biológico ############################
with col11:
    st.write('### Distribuição de Sexo Biológico')
    fig_gender = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='Gender', 
        barmode='stack',
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

############################## Gráfico de Idade ##############################
with col21:
    st.write('### Distribuição da Idade por Nível de Obesidade')

    fig_age = px.box(
        df_modelo, 
        y='Age',
        color='Obesity',
        labels={
            'Age': 'Idade',
            'Obesity': 'Nível de Obesidade'
            },
        color_discrete_map={
            'Abaixo do peso': 'royalblue', 
            'Peso normal': 'forestgreen',
            'Sobrepeso': 'orange',
            'Obesidade': 'orangered'
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )

    fig_age.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Nível Obesidade'
        )

    st.plotly_chart(fig_age, use_container_width=True)

col21, col22 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
############################## Gráfico de Peso ##############################
with col21:
    st.write('### Distribuição do Peso por Nível de Obesidade')

    fig_weight = px.box(
        df_modelo, 
        y='Weight',
        color='Obesity',
        labels={
            'Weight': 'Peso',
            'Obesity': 'Nível de Obesidade'
            },
        color_discrete_map={
            'Abaixo do peso': 'royalblue', 
            'Peso normal': 'forestgreen',
            'Sobrepeso': 'orange',
            'Obesidade': 'orangered'
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )

    fig_weight.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Nível Obesidade'
        )

    st.plotly_chart(fig_weight, use_container_width=True)

############################## Gráfico de Altura ##############################
with col22:
    st.write('### Distribuição da Altura por Nível de Obesidade')

    fig_height = px.box(
        df_modelo, 
        y='Height',
        color='Obesity',
        labels={
            'Height': 'Altura',
            'Obesity': 'Nível de Obesidade'
            },
        color_discrete_map={
            'Abaixo do peso': 'royalblue', 
            'Peso normal': 'forestgreen',
            'Sobrepeso': 'orange',
            'Obesidade': 'orangered'
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )

    fig_height.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Nível Obesidade'
        )

    st.plotly_chart(fig_height, use_container_width=True)

col31, col32 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
############################## Gráfico de Dispersão Altura X Peso ##############################
with col31:
    st.write('### Relação entre Altura e Peso por Nível de Obesidade')

    fig_scatter_height_weight = px.scatter(
        df_modelo, 
        x='Height', 
        y='Weight',
        color='Obesity',
        labels={
            'Height': 'Altura',
            'Weight': 'Peso',
            'Obesity': 'Nível de Obesidade'
            },
        color_discrete_map={
            'Abaixo do peso': 'royalblue', 
            'Peso normal': 'forestgreen',
            'Sobrepeso': 'orange',
            'Obesidade': 'orangered'
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )

    fig_scatter_height_weight.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Nível Obesidade'
        )

    st.plotly_chart(fig_scatter_height_weight, use_container_width=True)

with col32: 
############################## Gráfico de Histórico Familiar ##############################

    st.write('### Distribuição da Histórico Familiar por Nível de Obesidade')

    fig_family_history = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='family_history', 
        barmode='stack',
        histnorm='percent',
        title='Distribuição de Pessoas por Histórico Familiar e Nível de Obesidade',
        labels={
            'Obesity': 'Nível de Obesidade',
            'family_history': 'Histórico Familiar'
        },
        color_discrete_map={
            'Sim': 'indianred', 
            'Não': 'slateblue',
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )

    fig_family_history.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Histórico Familiar'
        )

    st.plotly_chart(fig_family_history, use_container_width=True)

col41, col42 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
################### Gráfico do Consumo Frequente de Alimentos Muito Calóricos ###################
with col41:
    st.write('### Distribuição do Consumo Frequente de Alimentos Muito Calóricos por Nível de Obesidade')
    
    fig_favc = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='FAVC', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'FAVC': 'Consumo frequente de alimentos muito calóricos'
        },
        color_discrete_map={
            'Sim': 'indianred', 
            'Não': 'slateblue',
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )
    
    fig_favc.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Consumo frequente'
        )
    
    st.plotly_chart(fig_favc, use_container_width=True)

############################## Gráfico da Frequência de Consumo de Vegetais ##############################
with col42:
    st.write('### Distribuição da Frequência de Consumo de Vegetais por Nível de Obesidade')

    fig_fcvc = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='FCVC', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'FCVC': 'Frequência de Consumo de Vegetais'
        },
        color_discrete_map={
            'Sim': 'indianred', 
            'Não': 'slateblue',
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade'],
            "FCVC": [1,
                     2,
                     3]
            }
        )

    fig_fcvc.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Consumo frequente'
        )

    st.plotly_chart(fig_fcvc, use_container_width=True)

col51, col52 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
############################## Gráfico da Quantidade de Refeições Principais ##############################
with col51:
    st.write('### Distribuição da Quantidade de Refeições Principais por Nível de Obesidade')

    fig_ncp = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='NCP', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'NCP': 'Frequência de Consumo de Vegetais'
        },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade'],
            "NCP": [1,
                    2,
                    3,
                    4]
            }
        )

    fig_ncp.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Quantidade de Refeições Principais'
        )

    st.plotly_chart(fig_ncp, use_container_width=True)

############################## Gráfico do Consumo de Alimentos entre Refeições ##############################
with col52:
    st.write('### Distribuição do Consumo de Alimentos entre Refeições por Nível de Obesidade')

    fig_caec = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='CAEC', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'CAEC': 'Consumo de Alimento entre Refeições'
        },
        color_discrete_map={
            'Não': 'yellowgreen', 
            'Às vezes': 'darkcyan',
            'Frequentemente': 'darkorange',
            'Sempre': 'crimson'
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade'],
            "CAEC": ['Não',
                     'Às vezes',
                     'Frequentemente',
                     'Sempre']
            }
        )

    fig_caec.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Consumo de Alimento entre Refeições'
        )

    st.plotly_chart(fig_caec, use_container_width=True)

col61, col62 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
############################## Gráfico do Hábito de Fumar ##############################
with col61:
    st.write('### Distribuição do Hábito de Fumar por Nível de Obesidade')

    fig_smoke = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='SMOKE', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'SMOKE': 'Hábito de Fumar'
        },
        color_discrete_map={
            'Sim': 'indianred', 
            'Não': 'slateblue',
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )

    fig_smoke.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Hábito de Fumar'
        )

    st.plotly_chart(fig_smoke, use_container_width=True)

############################## Gráfico do Consumo Diário de Água ##############################
with col62:
    st.write('### Distribuição do Consumo Diário de Água (em l) por Nível de Obesidade')

    fig_ch2o = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='CH2O', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'CH2O': 'Consumo Diário de Água (em l)'
        },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade'],
            "CH2O": [1,
                     2,
                     3]
            }
        )

    fig_ch2o.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Consumo Diário de Água (em l)'
        )

    st.plotly_chart(fig_ch2o, use_container_width=True)

col71, col72 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
############################## Gráfico do Acompanhamento de Ingestão de Calorias ##############################
with col71:
    st.write('### Distribuição do Acompanhamento de Ingestão de Calorias por Nível de Obesidade')

    fig_scc = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='SCC', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'SCC': 'Acompanhamento de Ingestão de Calorias'
            },
        color_discrete_map={
            'Sim': 'indianred', 
            'Não': 'slateblue',
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade']
            }
        )

    fig_scc.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Acompanhamento de Ingestão de Calorias'
        )

    st.plotly_chart(fig_scc, use_container_width=True)

############################## Gráfico do Acompanhamento de Frequência de Atividades Físicas ##############################
with col72:
    st.write('### Distribuição de Frequência de Atividades Físicas por Nível de Obesidade')

    fig_faf = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='FAF', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'FAF': 'Frequência de Atividades Físicas (Semanal)'
        },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade'],
            "FAF": [0,
                    1,
                    2,
                    3]
            }
        )

    fig_faf.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Frequência de Atividades Físicas (Semanal)'
        )

    st.plotly_chart(fig_faf, use_container_width=True)

col81, col82 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")
############################## Gráfico do Acompanhamento de Tempo Utilizando Dispositivos Eletrônicos ##############################
with col81:
    st.write('### Distribuição de Tempo Utilizando Dispositivos Eletrônicos por Nível de Obesidade')

    fig_tue = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='TUE', 
        barmode='stack',
        title='Distribuição de Pessoas por Tempo Utilizando Dispositivos Eletrônicos e Nível de Obesidade',
        labels={
            'Obesity': 'Nível de Obesidade',
            'TUE': 'Tempo Utilizando Dispositivos Eletrônicos (Diário)'
        },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade'],
            "FAF": [0,
                    1,
                    2,
                    3]
            }
        )

    fig_tue.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Frequência de Atividades Físicas (Semanal)'
        )

    st.plotly_chart(fig_tue, use_container_width=True)

############################## Gráfico do Acompanhamento de Consumo de Álcool ##############################
with col82:
    st.write('### Distribuição de Consumo de Álcool por Nível de Obesidade')

    fig_calc = px.histogram(
        df_modelo, 
        x='Obesity', 
        color='CALC', 
        barmode='stack',
        labels={
            'Obesity': 'Nível de Obesidade',
            'CAEC': 'Consumo de Álcool'
        },
        color_discrete_map={
            'Não': 'yellowgreen', 
            'Às vezes': 'darkcyan',
            'Frequentemente': 'darkorange',
            'Sempre': 'crimson'
            },
        category_orders={
            "Obesity": ['Abaixo do peso',
                        'Peso normal',
                        'Sobrepeso',
                        'Obesidade'],
            "CALC": ['Não',
                     'Às vezes',
                     'Frequentemente',
                     'Sempre']
            }
        )

    fig_calc.update_layout(
        xaxis_tickangle=-45,
        yaxis_title='Quantidade de pessoas',
        legend_title='Consumo de Álcool'
        )

    st.plotly_chart(fig_calc, use_container_width=True)

############################## Gráfico dos Meios de Transporte Utilizados ##############################
st.write('### Distribuição de Meios de Transporte Utilizados por Nível de Obesidade')

fig_mtrans = px.histogram(
    df_modelo, 
    x='Obesity', 
    color='MTRANS', 
    barmode='stack',
    labels={
        'Obesity': 'Nível de Obesidade',
        'MTRANS': 'Transporte Público'
    },
    category_orders={
        "Obesity": ['Abaixo do peso',
                    'Peso normal',
                    'Sobrepeso',
                    'Obesidade'],
        "MTRANS": ['Caminhando',
                    'Bicicleta',
                    'Carro',
                    'Transporte Público']
        }
    )

fig_mtrans.update_layout(
    xaxis_tickangle=-45,
    yaxis_title='Quantidade de pessoas',
    legend_title='Transporte Público'
    )

st.plotly_chart(fig_mtrans, use_container_width=True)