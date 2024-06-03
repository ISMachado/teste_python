# Projeto de ETL e API com FastAPI e PostgreSQL

Este projeto consiste em uma aplicação ETL (Extração, Transformação e Carga) e uma API construída com FastAPI que interage com um banco de dados PostgreSQL.

## Estrutura do Projeto

.
├── database.py # Configuração do banco de dados e definição do modelo
├── etl.py # Script de ETL
├── main.py # Aplicação FastAPI
├── schemas.py # Definições de schemas para a API
└── .env # Arquivo de variáveis de ambiente

## Configuração do Ambiente

### Pré-requisitos

1. Python 3.7+
2. PostgreSQL
3. pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:

```sh
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
pip install -r requirements.txt


Configuração do Banco de Dados

1. Crie um banco de dados PostgreSQL:
CREATE DATABASE nome_do_banco;

2. Configure as variáveis de ambiente no arquivo .env:
root_pw=your_postgres_password
postgres_user=your_postgres_user
postgres_db=your_postgres_db


Inicializando o Banco de Dados
Execute o script para criar a tabela no banco de dados:

python database.py

Executando o Script ETL
Para rodar o script ETL que extrai, transforma e carrega os dados no banco de dados, execute:
python etl.py

Executando a API
Para iniciar o servidor FastAPI, execute:
uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.

Endpoints da API
GET /data/ - Retorna os dados entre duas datas especificadas.

Exemplo de Uso
Para obter os dados entre duas datas:
GET /data/?start=2023-06-01T00:00:00&end=2023-06-01T23:59:59

Automatizando o Script ETL
Usando Cron Job (Linux)
1. Abra o crontab:
crontab -e

2. Adicione a linha abaixo para executar o script todos os dias à meia-noite:
0 0 * * * /usr/bin/python3 /path/to/your/project/etl.py

Usando Agendador de Tarefas (Windows)
1. Abra o Agendador de Tarefas e crie uma nova tarefa.
2. Configure a tarefa para ser executada diariamente.
3. No campo "Ação", escolha "Iniciar um programa" e aponte para o interpretador Python e o caminho para etl.py.