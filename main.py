#Importação das bibliotecas
import streamlit as st 
import pandas as pd
from utils import MinMaxScalerFeatures, OneHotEncodingFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib
from joblib import load
import time
import plotly.express as px

st.set_page_config(page_title="FIAP Tech Challenge 4 - Dataviz and Production Models")
st.title("FIAP Tech Challenge 4 - Dataviz and Production Models")
st.write("Essa página é dedicada a apresentar uma solução de visualização dos dados encontrando no dataset 'Obesity' e um modelo preditivo em produção." \
"\nTodo o conteúdo presente nessa página foi desenvolvido por Dênis Korin")