import psycopg
from apireq import var_resposta

id = var_resposta["imdbID"]
titulo = var_resposta["Title"]
tipo = var_resposta["Type"]
ano = var_resposta["Year"]
nota = var_resposta["Rated"]
lancamento = var_resposta["Released"]
duracao = var_resposta["Runtime"]
genero = var_resposta["Genre"]
diretor = var_resposta["Director"]
escritores = var_resposta["Writers"]
sinopse = var_resposta["Plot"]
linguagem = var_resposta["Language"]
pais = var_resposta["Country"]
premiacoes = var_resposta["Awards"]
poster = var_resposta["Poster"]
avaliacoes = var_resposta["Ratings"] + var_resposta["Metascore"] + var_resposta["imdbRating"] + var_resposta["imdbVotes"]

with psycopg.connect("dbname=gnx user=postgres host=164.90.152.205 port=80 password=3f@db") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        # cur.execute("""
        #     CREATE TABLE test (
        #         id serial PRIMARY KEY,
        #         num integer,
        #         data text)
        #     """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "negrao"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test")
        print(cur.fetchone())
        # will print (1, 100, "abc'def")

        # You can use `cur.executemany()` to perform an operation in batch
        cur.executemany(
            "INSERT INTO test (num) values (%s)",
            [(33,), (66,), (99,)])

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        cur.execute("SELECT id, num FROM test order by num")
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
