# Python para Usuários de Excel

Este repositório contém materiais e projetos educativos para aprender Python com foco em análise de dados para usuários familiarizados com Excel.

## 📚 Conteúdo do Projeto

### Material Educativo
- **Apostilas**: PDF com conteúdo teórico
- **Notebooks Jupyter**: Lições práticas cobrindo:
  - Criação e importação de tabelas
  - Visualização de dados
  - Seleção e filtragem
  - Adição de colunas e linhas
  - Mesclagem de tabelas
  - Realização de cálculos
  - Criação de tabelas dinâmicas
  - Criação de gráficos

### Aplicações Streamlit
- **SalesApp**: Aplicação web completa para análise de vendas
  - Visão geral das vendas
  - Visualização dinâmica
  - Gerenciamento de tabelas
  - Adição e remoção de vendas

### Datasets
- **vendas.csv/xlsx**: Dados de vendas
- **filiais.csv/xlsx**: Informações das filiais
- **produtos.csv/xlsx**: Catálogo de produtos
- **gerador_de_vendas.py**: Script para gerar dados de exemplo

### Scripts de Projeto
- Visualização de tabelas
- Seleção de colunas
- Adição de linhas
- Criação de tabelas dinâmicas
- Geração de gráficos

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7+
- pip

### Instalação
1. Clone este repositório:
```bash
git clone https://github.com/marcosweis/python-para-usuarios-excel.git
cd python-para-usuarios-excel
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando as Aplicações

#### Aplicação Streamlit Principal
```bash
streamlit run _visualizando_tabela.py
```

#### SalesApp (Aplicação Completa)
```bash
streamlit run "Material Aula/salesapp/Home.py"
```

#### Notebooks Jupyter
```bash
jupyter notebook
```

## 📦 Dependências

- **pandas**: Manipulação de dados
- **openpyxl**: Leitura/escrita de arquivos Excel
- **matplotlib**: Visualização de dados
- **plotly**: Gráficos interativos
- **streamlit**: Aplicações web
- **ipykernel**: Suporte a Jupyter

## 🎯 Objetivos de Aprendizado

- Migrar de Excel para Python
- Automatizar análises de dados
- Criar visualizações interativas
- Desenvolver aplicações web para análise de dados
- Dominar pandas para manipulação de dados

## 📁 Estrutura do Projeto

```
├── datasets/                 # Dados de exemplo
├── Material Aula/           # Notebooks e aplicações
│   ├── projeto/            # Scripts de exemplo
│   └── salesapp/           # Aplicação Streamlit completa
├── Apostilas/              # Material teórico
├── requirements.txt        # Dependências Python
└── README.md              # Este arquivo
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novos exemplos
- Melhorar a documentação

## 📄 Licença

Este projeto é destinado a fins educativos. Sinta-se livre para usar e modificar conforme necessário.

## 👨‍💻 Autor

Projeto desenvolvido como parte do curso "Python para Usuários de Excel" da Asimov Academy.