# 🔗 Server Sent Event - SSE
Um serviço para se utilizar em aplicações em tempo real. Para esse projeto utilizei o REDIS como um receptor das mensagens, uma espécie de fila, e o backend "escutando" as mensagens que chegam e redirecionando para o meu HTML.

**[Clique Aqui](https://www.youtube.com/watch?v=uiT4oK19hu4&list=PLNHxHgB-_LTusKqdWaZJtRbcqEMXPZXtw)** para saber mais sobre Server Sent Event (SSE) e sua utilização.

## 🚀 Tecnologias Utilizadas

- **[Python 3.11+](https://www.python.org/)**
- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno e de alta performance.
- **[Redis](https://redis.io/docs/latest/develop/clients/redis-py/)**: Redis como uma especie de mensageria.
- **[Docker & Docker Compose](https://www.docker.com/)**: Containerização do Redis

## 🛠️ Arquitetura e Lógica
1. O client (index.html) fecha uma conexão do tipo "event-stream" com a nossa rota "/stream_data"
2. A nossa API do backend responde a essa request e fecha um listener para o Redis
3. O Redis assim que receber uma notification informa o backend que por sua vez retorna a mensagem para o cliente (index.html)
4. O cliente por sua vez exibe a mensagem em tela.

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
- [Git](https://git-scm.com)
- [Docker](https://www.docker.com/get-started) e **Docker Compose**


## 🔧 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
- [Git](https://git-scm.com)
- [Docker](https://www.docker.com/) e **Docker Compose**
- [Python 3.11+](https://www.python.org/) *(caso vá rodar a API fora do container)*

### 2. Clonar o Repositório
Use o git clone com o link do repositorio

### 3. Subir o Redis
 - docker compose up -d

### 4. Rodando Localmente com Ambiente Virtual
- Criar e ativar a venv
    - python -m venv .venv
    - source .venv/bin/activate  # Linux/Mac
    - .venv\Scripts\activate   # Windows

 - Instalar as dependências
    - pip install -r requirements.txt

 - Subir a aplicação com Uvicorn (verifique se esta na raiz do projeto)
    - uvicorn src.api.main:app --reload

 - Abrir o index.html no navegador de sua preferencia
 
 - Acessar o Redis via terminal, se for necessario instalar no vscode o plugin de acesso ao redis e digitar o comando: PUBLISH notification 'MENSAGEM'