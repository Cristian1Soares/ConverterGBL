import streamlit as st
from forex_python.converter import CurrencyRates


#Nome da página
st.set_page_config(page_title="ConverterGBL")

#Título ao site
st.title('Bem vindo ao ConverterGBL!')
st.write('Converta o valor das moedas em segundos!')

c = CurrencyRates()

moedas = ['BRL', 'USD', 'EUR', 'GBP', 'JPY', 'CAD']

#Sistema de seleção das moedas
moeda_origem = st.selectbox('Selecione uma moeda para converter:', moedas)
moeda_destino = st.selectbox('Resultado:', moedas)

#Seleção
valor = st.number_input('Digite o valor:', min_value=0.0)

#Resultados
if st.button('Converter'):
    taxa = c.get_rate(moeda_origem, moeda_destino)
    resultado = valor * taxa

    st.success(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")

#Extras
st.sidebar.title('Menu')
st.sidebar.write('Em breve mais opções...')







