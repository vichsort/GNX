import psycopg
from config import db_name, db_host, db_password, db_port, db_user


def db_info():
    return psycopg.connect(
        dbname=db_name,
        user=db_user,
        host=db_host,
        port=db_port,
        password=db_password
    )


def generator():
    with db_info() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS filmes_series (
                    imdb_id    TEXT PRIMARY KEY,
                    titulo     TEXT,
                    tipo       TEXT,
                    ano        TEXT,
                    nota       TEXT,
                    lancamento TEXT,
                    duracao    TEXT,
                    genero     TEXT,
                    diretor    TEXT,
                    escritores TEXT,
                    sinopse    TEXT,
                    linguagem  TEXT,
                    pais       TEXT,
                    premiacoes TEXT,
                    poster     TEXT,
                    metascore  TEXT,
                    imdbrating TEXT,
                    imdbvotes  TEXT
                );
            """)
        conn.commit()


def catcher(param):
    imdb_id    = param.get("imdbID")
    titulo     = param.get("Title")
    tipo       = param.get("Type")
    ano        = param.get("Year")
    nota       = param.get("Rated")
    lancamento = param.get("Released")
    duracao    = param.get("Runtime")
    genero     = param.get("Genre")
    diretor    = param.get("Director")
    escritores = param.get("Writer")
    sinopse    = param.get("Plot")
    linguagem  = param.get("Language")
    pais       = param.get("Country")
    premiacoes = param.get("Awards")
    poster     = param.get("Poster")
    metascore  = param.get("Metascore")
    imdbrating = param.get("imdbRating")
    imdbvotes  = param.get("imdbVotes")

    with db_info() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO filmes_series (
                    imdb_id, titulo, tipo, ano,
                    nota, lancamento, duracao, genero,
                    diretor, escritores, sinopse, linguagem,
                    pais, premiacoes, poster, metascore,
                    imdbrating, imdbvotes
                ) VALUES (
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s
                )
                ON CONFLICT (imdb_id) DO NOTHING
                """,
                (
                    imdb_id, titulo, tipo, ano,
                    nota, lancamento, duracao, genero,
                    diretor, escritores, sinopse, linguagem,
                    pais, premiacoes, poster, metascore,
                    imdbrating, imdbvotes
                )
            )
        conn.commit()
