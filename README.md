# Tech Challenge - Fase 3

Projeto desenvolvido para a pós-graduação em Machine Learning Engineering da FIAP. Neste projeto desenvolvemos uma API rest utilizando Fast API para obter dados do IPCA (índice Nacional de Preços ao Consumidor Amplo) do IBGE. A API conta com uma autenticação de usuários por JWT. Os são são usados para treinar um modelo de Machine Learning com o objetivo de prever a inflação futura. Para serem utilizados no modelo, os dados obtidos através da API passam por uma transformação através de um script python contido na pasta Transformacao-base-IPCA.

Desenvolvido por: Bianca Gobe, Emerson Quirino e Mayara Reghin (Grupo 37)

##  📁 Estrutura do projeto

techchallenge-3-dados-ipca/

├── API_DADOS_IPCA/

├── Transformacao-base-IPCA/

│ ├──Transformacao_base_IPCA.py

├── prevendo_a_inflacao.ipnyb

├── README.md

**API_DADOS_IPCA/:** diretório com os arquivos da API. Será detalhado abaixo.

**Transformacao-base-IPCA/:** Script com as transformações da base de dados. 

**prevendo_a_inflacao.ipnyb:** notebook onde foi desenvolvido o modelo de machine learning.

**README.ms:** contém as informações do projeto. 

## 🚀 Funcionalidades da API

**Download de arquivos:** Download de arquivo contendo dados do IPCA em formato csv.

**Autenticação:** As rotas da API são protegidas por autenticação JWT (JSON Web Token), garantindo maior segurança e controle de acesso. Os usuários podem criar suas contas, alterar seus dados, consultar e deletar sua conta. O token é válido por 30 minutos a partir do momento do login e pode ser reiniciado.

**Documentação:** Documentação automática com Swagger

## 📁 Estrutura da API

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
poetry run alembic upgrade head
```

6. Inicie o servidor FastAPI com Uvicorn:
```bash
poetry uvicorn api.app:app --reload
```
## Utilizando a API

Para ter acesso aos arquivos da API é necessário ter um usuário criado. Após o usuário ser criado, fazer login com e-mail e senha. O botão Authorize na parte superior da API irá automaticamente gerar um Token quando o login for feito por lá. O Token expira automaticamente após 30 minutos, mas é possível atualizar antes do tempo expirar.

## 📖 Documentação da API
A documentação da API é gerada automaticamente com Swagger e está disponível em  http://127.0.0.1:8000/docs/. A rota raiz ( http://127.0.0.1:8000) também direciona automaticamente para a documentação.

## Transformando os dados

Os dados obtidos através da API devem passar pelo processo de transformação antes de serem usados no modelo de machine learning. Para isso, basta salvar o arquivo "Transformacao_base_IPCA.py" no mesmo diretório em que estiver a base de dados e executar. Será gerado um novo arquivo com o nome "dados_ipca_transformados.csv'.

## Sobre o modelo de machine learning

Este modelo tem como propósito prever o índice geral do IPCA, e fazer uma comparação entre o dado real e previsto. O Índice Nacional de Preços ao Consumidor Amplo - IPCA é produzido pelo IBGE desde dezembro de 1979. A partir de novembro de 1985, de acordo com o Decreto n. 91.990, o IPCA passou a ser utilizado como indexador oficial do País, corrigindo salários, aluguéis, taxa de câmbio, poupança, além dos demais ativos monetários. 

OBS: A TABELA UTILIZADA CONTÉM DADOS DE 2020 A 2025.

O modelo utilizado é a regressão linear múltipla, pelas seguintes razões:
1.	Capacidade de lidar com múltiplos preditores: Diferente da regressão linear simples, que usa apenas uma variável independente, a regressão linear múltipla permite incluir várias variáveis preditoras. Isso é crucial para prever o IPCA, pois a inflação é composta pelos grupos da cesta.
2.	Melhor ajuste e precisão: Ao considerar múltiplas variáveis, o modelo pode capturar mais nuances e interações entre os fatores que afetam a inflação. Isso geralmente resulta em um ajuste melhor e previsões mais precisas
3.	Análise de impacto individual: A regressão linear múltipla permite analisar o impacto individual de cada variável preditora sobre o IPCA. Isso ajuda a entender quais fatores têm maior influência na inflação e pode orientar políticas econômicas mais eficazes.
4.	Flexibilidade: Este modelo pode ser ajustado para incluir variáveis sazonais e defasadas, o que é útil para capturar padrões recorrentes e atrasos nos efeitos das variáveis econômicas.
5.	Facilidade de interpretação: Os coeficientes estimados na regressão linear múltipla são relativamente fáceis de interpretar, permitindo que analistas e economistas compreendam como cada variável contribui para a previsão do IPCA

O modelo foi escrito em um arquivo do jupyter notebook para facilitar a execução e visualização de gráficos.

## 🤝 Contribuindo
Fork este repositório.
Crie sua branch (git checkout -b feature/nova-funcionalidade).
Faça commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
Faça push para sua branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request. instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.
