import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 

df_complet = pd.read_csv('data/df_complet.csv')
df_complet_log = pd.read_csv('data/df_complet_log.csv')
df_complet_copy_0 = pd.read_csv('data/df_complet_copy_0.csv')


st.title('a. Selecione os plots relevantes da fase de análise exploratória.')

fig1 = plt.figure()
sns.countplot(data=df_complet, x='IsHoliday')
plt.title('Volume de Semanas com feriados vs Semanas Sem Feriados')
st.pyplot(fig1)


fig2 = plt.figure()
sns.barplot(data=df_complet,x='IsHoliday', y='Sales' )
plt.title('Volume de Venda no Feriados vs Sem Feriado')
st.pyplot(fig2)
#Esta visualização comprova que as vendas nos feriados performam ligeiramente melhor. 


fig3 = plt.figure(figsize=(15,7))
sns.barplot(data=df_complet,x='Store', y='Sales' )
plt.title('Volume de Vendas por Loja',fontsize=20)
st.pyplot(fig3)
#Através dessa visualização é possível constatar que existe um desequilíbrio de vendas entre as unidades o que é natural.  

fig4,(ax1, ax2) = plt.subplots(nrows=1,ncols=2, figsize=(10,5))
sns.kdeplot(data=df_complet, x="Temperature", ax=ax1)
sns.kdeplot(data=df_complet, x="Fuel_Price", ax=ax2)
fig4.suptitle('KDE das Variáveis - Parte 1', fontsize=20)
st.pyplot(fig4)


fig5, (ax3,ax4,ax5) = plt.subplots(nrows=1,ncols=3, figsize=(10,5))
sns.kdeplot(data=df_complet, x="Unemployment", ax=ax3)
sns.kdeplot(data=df_complet, x="CPI", ax=ax4)
sns.kdeplot(data=df_complet, x="Sales", ax=ax5)
fig5.suptitle('KDE das Variáveis - Parte 2', fontsize=20)
st.pyplot(fig5)

st.title('b. Mostre os dados antes e depois da análise de qualidade dos dados, destacando as melhorias')

st.write('A varíavel normalizada foi a Sales, então será exibido o KDE após a normalização.')

fig6 = plt.figure()
sns.kdeplot(data=df_complet_log, x="Sales")
plt.title('Exibindo melhora na variável Sales')
st.pyplot(fig6)

st.title('c. Mostre o resultado do modelo de regressão linear(Série temporal no meu caso).')

st.image('predicao_modelo.png')

st.image('predicao_e_original.png')

st.title('d.Mostre as métricas calculadas de forma clara.')
st.image('qualidade_modelo.png')
