# 🥇 Instalação
GNX é uma ferramenta responsável por adquirir informações sobre um filme em cartaz. Com a GNX você pode pesquisar por um nome e encontrar tudo a respeito de um título das telas quentes do cinema. Algumas das informações que você pode encontrar aqui são:
- Id na IMDB
- Data de lançamento
- Duração
- Gênero
- Notas
- E muito mais!

## 🚀 Instalação

1. Clone o repositório:
   ```bash
    git clone https://github.com/vichsort/GNX.git
    cd GNX
    ```

2. Certifique-se de ativar o seu ambiente virtual:
    ```bash
    python -m venv .venv

    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

4. Sirva o servidor:
    ```bash
    Flask --app apireq.py run
    ```

## 🎮 Como Utilizar
### 👨‍💻 Método 1 (Website):
Para usar da forma preferível, usando a aplicação Web desenvolvida pela dupla, siga os seguintes passos:
1. Sirva o servidor do Webapp:
    ```bash
    Flask --app app.py run
    ```

2. Acesse o site e insira o tipo da requisição (título ou id)
3. Insira a informação respectiva ao tipo selecionado
4. Clique no botão "Enviar"

### 💻 Método 2 (Cliente REST):
Se preferir apenas realizar a requisição inserindo um JSON por meio de algum REST Client (como Postman, Insomnia, etc.), siga os seguintes passos:
1. Selecione o tipo de dado que você enviará (title ou id)
2. Envie para o seguinte servidor local sua requisição: http://127.0.0.1:5000/`(tipo do dado)`
3. Coloque no corpo da requisição um metadado JSON contendo o argumento "info" e sua equivalente resposta.


## 📂 Estrutura do Projeto `GNX`

```text
📁 GNX
├── 📁 __pycache__/
├── 📁 .venv/
├── 📁 templates/
│   └── 📄 index.html
├── 📄 .gitignore
├── 📄 apireq.py     // faz as requisições da API
├── 📄 app.py        // realiza o serve do website
├── 📄 config.py     // guarda as variáveis frágeis
├── 📄 db.py         // realiza a conexão com o banco de dados
└── 📄 README.md
└── 📄 requirements.txt
```

## 🌶️ Como foi desenvolvido
Além de amor, o projeto GNX foi desenvolvido por Vitor Marcelo Mignoni e Pietro Matheus Pellizzaro usando Flask e Postgres, como atividade prática para a disciplina Desenvolvimento Web III. <br>
As tecnologias foram assim escolhidas para melhor situar a didática de ensino que o professor tem utilizado em aula. <br>
Usando alguns dos princípios da nomenclatura SOLID, os arquivos foram separados para situarem condições e realizarem funções diferentes entre si, efetuando então serviços autônomos e de fácil leitura, que possibilite futura abstração ou escalabilidade. <br>
A princípio, a atividade consiste em realizar positivamente uma requisição usufruindo a API gratuita da OMDB (você pode ver sobre ela [aqui](http://www.omdbapi.com/)). Realizando corretamente a requisição, guardamos os resultados separadamente em colunas dentro de um banco de dados relacional Postgres. <Br>
Contudo, a dupla decidiu aprimorar o projeto e desenvolver um sistema num website que realize a requisição com inserção apartir de um formulário HTML disposto em um servidor Flask local. <br>
Tendo isso em vista, ainda se é possível realizar a requisição apenas com os métodos HTTP (como usando Postman, Insomnia etc) apenas enviando a http://127.0.0.1:5000/{title ou id} um metadado JSON contendo o parâmetro "info" - Como explicado no método 2.

## 💡 Planos
O Projeto GNX será melhorado constantemente para adequar-se aos padrões de segurança e escalabilidade. Futuramente, este projeto será publicado como plataforma de pesquisas por muitas outras qualificações dentro da API OMDB, tornando-se uma aplicação viável que também tornará-se uma forma de realizar _reviews_ e avaliações sobre os filmes e séries encontrados dentro da mesma.
