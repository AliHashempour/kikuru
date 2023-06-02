import psycopg2
from app.helpers.config_helper import ConfigHelper

CFG_HELPER = ConfigHelper()


def db_connection():
    host = CFG_HELPER.get("POSTGRES", "host")
    database = CFG_HELPER.get("POSTGRES", "database_name")
    user = CFG_HELPER.get("POSTGRES", "username")
    password = CFG_HELPER.get("POSTGRES", "password")

    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return connection


def db_insert(request_url):
    url_id = abs(hash(request_url)) % (10 ** 8)

    con = db_connection()
    cursor = con.cursor()
    val = (url_id, request_url)
    insert_query = """
        INSERT INTO urls_table (ID, URL_ADDRESS)
        VALUES (%s, %s)
    """
    cursor.execute(insert_query, val)
    con.commit()
    return url_id


def db_select(url_id):
    con = db_connection()
    cursor = con.cursor()

    select_query = f"SELECT URL_ADDRESS FROM urls_table WHERE ID ={url_id}"
    cursor.execute(select_query)
    result = cursor.fetchall()
    result_url = result[0][0]
    return result_url
