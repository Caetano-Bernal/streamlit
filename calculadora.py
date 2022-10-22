from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
from millify import millify
from millify import prettify

def calcula(salario_minimo, qtd_mes, valor_entrada,montante,percentual):

    valor_salario = salario_minimo * qtd_mes
    comissao = montante * percentual
    total = valor_entrada + valor_salario + comissao
    return total, comissao, valor_salario




st.set_page_config(page_title='SIMULÇÃO DE PROPOSTA',layout='wide')


tabs_font_css = """
<style>
div[class*="stMultiSelect"] label {
  font-size: 20px;
  color: black;
}

div[class*="stSelectbox"] label {
  font-size: 20px;
  color: black;
}

div[class*="stSlider"] label {
  font-size: 20px;
  color: black;
}

</style>
"""







def run():
    st.write(tabs_font_css, unsafe_allow_html=True)

    st.title("SIMULAÇÃO DE PROPOSTA")
    st.text_area('PROPOSTA DR JOÃO', '''Apresentamos a seguinte proposta de prestação de serviços
            a. R$ 100.000,00 a título de pro labore na forma de pagamento a ser combinada
            b. Após 1 ano da propositura dos processos  : 
            2 salários mínimos mensais a serem compensados nos honorários de  êxito
            c. Honorários de êxito correspondente a:
            c.1  10% do proveito econômico até R$ 1.000.000,00.
            c.2  8% do proveito econômico de R$ 1.000.000,00 até R$ 3.000.000,00;
            c.3  5% acima de R$ 5.000.000,00.''', height =200)

    

    #formatacao = '<p style="font-family:sans serif; color:Black; font-size: 30px;">Original image</p>'
    formatacao = '<p style="color:Black; font-size: 35px;">{}</p>'

    valor_entrada = st.sidebar.number_input('valor de entrada',value = 100000, step=5000)
    salario_minimo = st.sidebar.number_input('Salario minimo', value = 1200, step=100)
    qtd_mes = st.sidebar.number_input('tempo de pagamento do salario minino',value = 60, step=5)
    percentual = st.sidebar.number_input('percentual do montante',value = 0.05, step=0.01)
    montante = st.sidebar.number_input('montante', value = 1000000,step=500000)

    total, comissao, valor_salario = calcula(salario_minimo, qtd_mes, valor_entrada,montante,percentual) 

    col1, col2, col3 , col4= st.columns(4)
    col1.metric("Total", prettify(total))
    col2.metric("Comissão", prettify(comissao))
    col3.metric("Total Salario", prettify(valor_salario))
    col4.metric("Total Salario", prettify(valor_entrada))
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()