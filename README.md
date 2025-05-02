# GNX
GNX é uma ferramenta responsável por adquirir informações sobre um filme em cartaz. Com a GNX você pode pesquisar por um nome e encontrar tudo a respeito de um título das telas quentes do cinema.<br>

## Instalação

```bash
py -3 -m venv .venv
.venv\Scripts\activate
pip install Flask
pip install psycopg[binary]
```

## Esquema
- main.py vai gerir todas as requisições e chamar as funções
- psyco.py vai gerir tudo sobre o banco de dados
- apireq.py vai gerir tudo sobre a omdapi
- app.py faz a renderização do site
- pasta templates tem as paginas html
- pasta static tem as estilizações em css
- pasta assets tem as imagens

## O que precisamos fazer
- Tem que implementar um negocio nessa api aqui: https://omdapi.com
- o usuário faz uma requisição que diz à nossa API que ela tem que requisitar nessa omd se tem o filme pedido lá
- caso não tiver, o sistema retorna 404 
- no banco de dados armazenamos as informações retornadas do JSON da API.

