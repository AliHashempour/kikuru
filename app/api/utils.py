import psycopg2


def db_connection():
    host = 'localhost'
    database = 'url-shortener'
    user = 'postgres'
    password = 22442883

    # Establish the connection
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return connection



