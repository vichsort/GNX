import psycopg

def catcher(param): 
    id = param["imdbID"]
    titulo = param["Title"]
    tipo = param["Type"]
    ano = param["Year"]
    nota = param["Rated"]
    lancamento = param["Released"]
    duracao = param["Runtime"]
    genero = param["Genre"]
    diretor = param["Director"]
    escritores = param["Writers"]
    sinopse = param["Plot"]
    linguagem = param["Language"]
    pais = param["Country"]
    premiacoes = param["Awards"]
    poster = param["Poster"]
    avaliacoes = param["Ratings"] + param["Metascore"] + param["imdbRating"] + param["imdbVotes"]

with psycopg.connect("dbname=gnx user=postgres host=164.90.152.205 port=80 password=3f@db") as conn:

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO test (id, titulo, tipo, ano, nota, lancamento, duracao, genero, diretor, escritores, sinopse, linguagem, pais, premiacoes, poster, avaliacoes) VALUES (%s, %s)",
            (id, titulo, tipo, ano, nota, lancamento, duracao, genero, diretor, escritores, sinopse, linguagem, pais, premiacoes, poster, avaliacoes))

        cur.execute("SELECT * FROM test")
        print(cur.fetchone())
        cur.executemany(
            "INSERT INTO test (num) values (%s)",
            [(33,), (66,), (99,)])
        cur.execute("SELECT id, num FROM test order by num")
        for record in cur:
            print(record)

        conn.commit()
