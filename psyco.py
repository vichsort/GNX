import psycopg
from config import db_name, db_host, db_password, db_port, db_user

def db_info():
    return psycopg.connect(f'dbname={db_name} user={db_user} host={db_host} port={db_port} password={db_password}')

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
    avaliacoes = param["Ratings"]
    metascore = param["Metascore"]
    imdbrating = param["imdbRating"]
    imdbvotes = param["imdbVotes"]

    with db_info() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                        INSERT INTO filmes_series (
                        id, 
                        tipo, 
                        ano, 
                        nota, 
                        lancamento, 
                        duracao, 
                        genero, 
                        diretor, 
                        escritores, 
                        sinopse, 
                        linguagem, 
                        pais, 
                        premiacoes, 
                        poster, 
                        avaliacoes,
                        metascore,
                        imdbrating,
                        imdbvotes
                        )
                            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                        """, (
                            id, 
                            tipo, 
                            ano, 
                            nota, 
                            lancamento, 
                            duracao, 
                            genero, 
                            diretor, 
                            escritores, 
                            sinopse, 
                            linguagem, 
                            pais, 
                            premiacoes, 
                            poster, 
                            avaliacoes,
                            metascore,
                            imdbrating,
                            imdbvotes
                            ))




def generator():
    with db_info() as conn:
        with conn.cursor() as cur: 
            cur.execute("""
                CREATE TABLE IF NOT EXISTS requisitados (
                    id PRIMARY KEY, 
                    titulo TEXT,
                    tipo TEXT,
                    ano TEXT,
                    nota: TEXT,
                    lancamento TEXT,
                    duracao TEXT,
                    genero TEXT,
                    diretor TEXT,
                    escritores TEXT,
                    sinopse TEXT,
                    linguagem TEXT,
                    pais TEXT,
                    premiacoes TEXT,
                    poster TEXT,
                    avaliacoes TEXT,
                    metascore TEXT,
                    imdbrating TEXT,
                    imdbvotes TEXT
                );
            """) 
        conn.commit()
