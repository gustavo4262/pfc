import psycopg2

def criaConexao():
    conn = psycopg2.connect(
            host="ec2-3-217-14-181.compute-1.amazonaws.com",
            database="d3135m9jiud9ru",
            user="xcyvurwpchgwco",
            password="a101cf29197042343d25ea45c12388e5a1244cb4bbfa561a582ac385d898a2f7"
            )

    cur = conn.cursor()

    return conn, cur