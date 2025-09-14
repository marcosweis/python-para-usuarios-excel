import streamlit as st
import pandas as pd
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Análise de Vendas",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Análise de Vendas")

# Carregar dados
pasta_datasets = Path(__file__).parent / 'datasets'

# Verificar se os arquivos existem
try:
    df_vendas = pd.read_csv(pasta_datasets / 'vendas_sample.csv', decimal=',', sep=';', index_col=0)
    df_filiais = pd.read_csv(pasta_datasets / 'filiais.csv', decimal=',', sep=';')
    df_produtos = pd.read_csv(pasta_datasets / 'produtos.csv', decimal=',', sep=';')
    
    st.success("✅ Dados carregados com sucesso!")
    
    # Mostrar informações básicas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total de Vendas", len(df_vendas))
    
    with col2:
        st.metric("Total de Filiais", len(df_filiais))
    
    with col3:
        st.metric("Total de Produtos", len(df_produtos))
    
    # Mostrar tabelas
    st.subheader("📋 Dados de Vendas")
    st.dataframe(df_vendas, use_container_width=True)
    
    st.subheader("🏢 Filiais")
    st.dataframe(df_filiais, use_container_width=True)
    
    st.subheader("🛍️ Produtos")
    st.dataframe(df_produtos, use_container_width=True)
    
except FileNotFoundError as e:
    st.error(f"❌ Erro ao carregar dados: {e}")
    st.info("💡 Execute o script 'gerador_de_vendas.py' para gerar os dados de exemplo.")

except Exception as e:
    st.error(f"❌ Erro inesperado: {e}")