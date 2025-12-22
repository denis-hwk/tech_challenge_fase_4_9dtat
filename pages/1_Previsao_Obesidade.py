#Importação das bibliotecas
import streamlit as st 
import pandas as pd
from utils import MinMaxScalerFeatures, OneHotEncodingFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib
from joblib import load
import time

#carregando os dados 
df_modelo = pd.read_csv('https://raw.githubusercontent.com/denis-hwk/tech_challenge_fase_4_9dtat/refs/heads/main/df_modelo.csv')

############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Formulário para Avaliação de Obesidade</h1>", unsafe_allow_html = True)

st.warning('Preencha o formulário com todos os seus dados pessoais e clique no botão **ENVIAR** no final da página.')

# Gênero (gender)
st.write('### Sexo Biológico')
input_gender_male = st.radio('Qual é o seu sexo biológico?', 
                             ['Masculino','Feminino'], 
                             index=0)
input_gender_male_dict = {'Masculino': 1, 
                          'Feminino':0}
input_gender_male = input_gender_male_dict.get(input_gender_male)

# Idade (age)
st.write('### Idade')
input_age = float(st.slider('Qual é a sua idade?', 18, 100))

# Altura (height)
st.write('### Altura')
input_height = float(st.text_input('Digite a sua altura (em metros) e pressione ENTER para confirmar. Exemplo: 1.89', value='0.00'))

# Peso (weight)
st.write('### Peso')
input_weight = float(st.slider('Qual é o seu peso em kg?', 0, 250))

# Histórico Familiar (family_history)
st.write('### Histórico Familiar')
input_family_history = st.radio('Você possui alguma pessoa com obesidade na sua família?',
                                ['Sim','Não'], 
                                index=0)
input_family_history_dict = {'Sim': 1, 
                             'Não':0}
input_family_history = input_family_history_dict.get(input_family_history)

# Consumo Frequente de Alimentos com alta quantidade de calorias (FAVC)
st.write('### Consumo frequente de alimentos com alta quantidade de calorias')
input_favc = st.radio('Você consome frequentemente alimentos com altas quantidades de calorias?',
                      ['Sim','Não'], 
                      index=0)
input_favc_dict = {'Sim': 1, 
                   'Não':0}
input_favc = input_favc_dict.get(input_favc)

# Consumo de vegetais nas refeições (FCVC)
st.write('### Consumo de vegetais nas refeições')
input_fcvc = st.radio('Você consome vegetais com frequência?', 
                      ['Raramente', 
                       'Às vezes', 
                       'Sempre'], 
                       index=0)
input_fcvc_dict = {'Raramente': 1, 
                   'Às vezes':2, 
                   'Sempre': 3}
input_fcvc = input_fcvc_dict.get(input_fcvc)

# Quantidade de refeições po dia (NCP)
st.write('### Quantidade de refeições diárias')
input_ncp = float(st.slider('Quantas refeições diárias você faz?', 1, 6))

# Consumo de alimentos entre as refeições (CAEC)
st.write('### Consumo de alimentos entre as refeições')
input_caec = st.radio('Você consome alimentos entre as refeições principais?', 
                      ['Não',
                       'Raramente', 
                       'Às vezes', 
                       'Sempre'], 
                       index=0)
input_caec_dict = {'Não': 0,
                   'Raramente': 1, 
                   'Às vezes': 2, 
                   'Sempre': 3}
input_caec = input_caec_dict.get(input_caec)

# Fumante (SMOKE)
st.write('### Fumante')
input_smoke = st.radio('Você fuma?',
                       ['Sim','Não'], 
                       index=0)
input_smoke_dict = {'Sim': 1, 
                    'Não':0}
input_smoke = input_smoke_dict.get(input_smoke)

# Consumo diário de água (H2O)
st.write('### Consumo diário de água')
input_h2o = st.radio('Qual é a quantidade diária de água que você consome?', 
                     ['Até 1L/dia', 
                      'Entre 1L/dia até 2L/dia', 
                      'Mais do que 2L/dia'], 
                      index=0)
input_h2o_dict = {'Até 1L/dia': 1, 
                  'Entre 1L/dia até 2L/dia':2, 
                  'Mais do que 2L/dia': 3}
input_h2o = input_h2o_dict.get(input_h2o)

# Acompanhamento diário de ingestão de calorias (SCC)
st.write('### Acompanhamento diário de ingestão de calorias')
input_scc = st.radio('Você acompanha quantas calorias você ingere por dia?',
                     ['Sim','Não'], 
                     index=0)
input_scc_dict = {'Sim': 1, 
                  'Não':0}
input_scc = input_scc_dict.get(input_scc)

# Frequência semanal de prática de exercícios físicos (FAF)
st.write('### Frequência semanal de prática de exercícios físicos')
input_faf = st.radio('Quantas vezes por semana você pratica exercícios físicos?', 
                     ['Nenhuma', 
                      'De 1 a 2 vezes/semana', 
                      'De 3 a 4 vezes/semana', 
                      '5 vezes/semana ou mais'], 
                      index=0)
input_faf_dict = {'Nenhuma': 0, 
                  'De 1 a 2 vezes/semana':1, 
                  'De 3 a 4 vezes/semana': 2, 
                  '5 vezes/semana ou mais': 3}
input_faf = input_faf_dict.get(input_faf)

# Quantidade de tempo utilizando dispositivos eletrônicos (TUE)
st.write('### Quantidade de tempo utilizando dispositivos eletrônicos')
input_tue = st.radio('Quanto tempo você passa utilizando dispositivos eletrônicos', 
                     ['Até 2 horas/dia', 
                      'Entre 3 horas/dia até 5 horas/dia', 
                      'Mais do que 5 horas/dia'], 
                      index=0)
input_tue_dict = {'Até 2 horas/dia': 1, 
                  'Entre 3 horas/dia até 5 horas/dia':2, 
                  'Mais do que 5 horas/dia': 3}
input_tue = input_tue_dict.get(input_tue)

# Consumo de bebidas alcoólicas (CALC)
st.write('### Consumo de bebidas alcoólicas')
input_calc = st.radio('Você consome bebidas alcoólicas?', 
                      ['Não',
                       'Raramente', 
                       'Às vezes', 
                       'Sempre'], 
                       index=0)
input_calc_dict = {'Não': 0,
                   'Raramente': 1, 
                   'Às vezes':2, 
                   'Sempre': 3}
input_calc = input_calc_dict.get(input_calc)

# Meios de transporte habituais (MTRANS)
st.write('### Meios de transporte habituais')
input_mtrans = st.radio('Qual meio de transporte você mais utiliza?', 
                      ['Carro',
                       'Moto', 
                       'Bicicleta', 
                       'Transporte Público',
                       'Caminhada'], 
                       index=0)
input_mtrans_dict = {'Carro': 'Automobile',
                   'Moto': 'Motorbike', 
                   'Bicicleta': 'Bike', 
                   'Transporte Público': 'Public_Transportation',
                   'Caminhada': 'Walking'
                   }
input_mtrans = input_mtrans_dict.get(input_mtrans)

# Lista de todas as variáveis: 
novo_cliente = [input_gender_male, # Gênero
                input_age, # Idade
                input_height, # Altura
                input_weight, # Peso
                input_family_history,  # Histórico Familiar
                input_favc,  # Consumo Frequente de Alimentos com alta quantidade de calorias (FAVC)
                input_fcvc, # Consumo de vegetais nas refeições (FCVC)
                input_ncp, # Quantidade de refeições po dia (NCP)
                input_caec, # Consumo de alimentos entre as refeições (CAEC)
                input_smoke, # Fumante (SMOKE)
                input_h2o, # Consumo diário de água (H2O)
                input_scc, # Acompanhamento diário de ingestão de calorias (SCC)
                input_faf, # Frequência semanal de prática de exercícios físicos (FAF)                                             
                input_tue, # Quantidade de tempo utilizando dispositivos eletrônicos (TUE)
                input_calc, # Consumo de bebidas alcoólicas (CALC)
                input_mtrans, # Meios de transporte habituais (MTRANS)
                0 # target (Obesity)
                ]

# Separação das amostras de treino e teste
def df_train_test_split(df, test_size):
  seed = 1337
  df_train, df_test = train_test_split(df_modelo, test_size=test_size, random_state=seed)
  return df_train, df_test

df_train, df_test = df_train_test_split(df_modelo, 0.2)

# Consolidando dados do novo cliente
novo_cliente_modelo = pd.DataFrame([novo_cliente], columns=df_test.columns)

# Adicionando novo cliente ao dataframe dos dados de teste
df_novo_cliente  = pd.concat([df_test, novo_cliente_modelo], ignore_index=True)

# Pipeline do modelo
def pipeline_modelo(df):
  pipeline = Pipeline([
      ('MinMaxScaling', MinMaxScalerFeatures()),
      ('OneHotEncoding', OneHotEncodingFeatures())
      ])

  df_pipeline = pipeline.fit_transform(df)
  return df_pipeline

# Separando variáveis para treino do modelo
train = pipeline_modelo(df_train)
X_train, y_train = train.drop(['Obesity'], axis=1), train['Obesity']

# Aplicando a pipeline aos dados de teste
df_novo_cliente = pipeline_modelo(df_novo_cliente)

# Removendo a coluna target do teste
previsao_novo_cliente = df_novo_cliente.drop(['Obesity'], axis=1)

# Gerar previsão do modelo 
if st.button('Enviar'):
    # Criar a barra de progresso
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Etapa 1: Carregando o modelo
    status_text.text('Carregando modelo...')
    progress_bar.progress(25)
    model = joblib.load('modelo/random_forest_classifier.joblib')
    model.fit(X_train, y_train)
    
    # Etapa 2: Preparando dados
    status_text.text('Preparando dados para previsão...')
    progress_bar.progress(50)
    time.sleep(0.3)  # Pequena pausa para visualização
    
    # Etapa 3: Executando previsão
    status_text.text('Executando modelo de previsão...')
    progress_bar.progress(75)
    final_pred = model.predict(previsao_novo_cliente)
    
    # Etapa 4: Finalizando
    status_text.text('Finalizando...')
    progress_bar.progress(100)
    time.sleep(0.3)
    
    # Limpar a barra de progresso e texto de status
    progress_bar.empty()
    status_text.empty()
    
    # Mostrar resultado
    if final_pred[-1] <= 1:
       st.success('### Baixo risco do paciente possuir obesidade')

    elif final_pred[-1] <= 3:
       st.success('### Risco moderado do paciente possuir obesidade')

    else:
       st.error('### Alto risco do paciente possuir obesidade')