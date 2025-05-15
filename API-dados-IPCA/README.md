# Tech Challenge - Fase 2 

Projeto desenvolvido para a pós-graduação em Machine Learning Engineering da FIAP. Neste projeto desenvolvemos uma API rest utilizando Fast API para obter dados do IPCA (índice Nacional de Preços ao Consumidor Amplo) do IBGE. A API conta com uma autenticação de usuários por JWT. Os dados são usados para treinar um modelo de Machine Learning com o objetivo de prever a inflação futura.

Desenvolvido por: Bianca Gobe, Emerson Quirino e Mayara Reghin (Grupo 37)


## 🚀 Funcionalidades

**Download de arquivos:** Download de arquivo contendo dados do IPCA em formato JSON.

**Autenticação:** As rotas da API são protegidas por autenticação JWT (JSON Web Token), garantindo maior segurança e controle de acesso. Os usuários podem criar suas contas, alterar seus dados, consultar e deletar sua conta. O token é válido por 30 minutos a partir do momento do login e pode ser reiniciado.

**Documentação:** Documentação automática com Swagger

## 📁 Estrutura do Projeto

API_DADOS_IPCA/

├── api/

│ ├── init.py

│ ├── app.py

│ ├── models.py

│ ├── schemas.py

│ ├── security.py

│ ├── setting.py

│ └── routes/

│ ├── init.py

│ ├── auth.py

│ ├── ipca.py

│ └── users.py

├── migrations/

│ └── versions/

│ └── 681fa444bf23_create_users_table

├── alembic.ini

├── poetry.lock

├── pyproject.toml

└── README.md


**api/:** Diretório principal do aplicativo, onde ficam armazenadas as rotas, modelos, esquemas e configurações.

**routes/:** Contém as rotas organizadas por funcionalidades.

**app.py:** Ponto de entrada para iniciar o aplicativo.

**migrations/:** Pasta usada pelo Alembic para gerenciar rveisões e configurações de mudanças no banco de dados.

**alembic.ini:** Arquivo de configuração Alembic

**poetry.lock:** lista as dependências do projeto para garantir a reprodução em um ambiente consistente.

**pyproject.toml:** arquivo de configurações do projeto
README.md: Documentação do projeto.

## 🛠️ Como Executar o Projeto

0. Pré-requisitos

Instalação do Python 3.11+ e Poetry

1. Clone o Repositório
```bash
git clone https://github.com/mayarareghin/tech-challenge-3-dados-ipca.git
```

2. Instale as dependências com o Poetry
```bash
poetry install
```

3. Ative o ambiente virtual do Poetry
```bash
    poetry shell
```

4. Configure as variáveis de ambiente (crie um arquivo .env com essas variáveis)
```bash
DATABASE_URL="sqlite+aiosqlite:///database.db"
SECRET_KEY="secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Inicialize o banco de dados com o Alembic:
```bash
alembic upgrade head
```

6. Inicie o servidor FastAPI com Uvicorn:
```bash
uvicorn api.app:app --reload
```
## Utilizando a API

Para ter acesso aos arquivos da API é necessário ter um usuário criado. Após o usuário ser criado, fazer login com e-mail e senha. O botão Authorize na parte superior da API irá automaticamente gerar um Token quando o login for feito por lá. O Token expira automaticamente após 30 minutos, mas é possível atualizar antes do tempoe expirar.

## 📖 Documentação da API
A documentação da API é gerada automaticamente com Swagger e está disponível em  http://127.0.0.1:8000/docs/. A rota raiz ( http://127.0.0.1:8000) também direciona automaticamente para a documentação.



## 🤝 Contribuindo
Fork este repositório.
Crie sua branch (git checkout -b feature/nova-funcionalidade).
Faça commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
Faça push para sua branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request. instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.