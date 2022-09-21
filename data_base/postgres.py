import psycopg2
import numpy as np

def get_database_password():
    from pathlib import Path
    path = Path(__file__).parent
    path = path.joinpath('database.txt')
    with path.open() as f:
        key = f.readline()
    f.close()
    return key

def connection_history():
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = get_database_password,
            database = 'otp_analysis'
        )
        return connection
    except Exception as ex:
        print(ex)
        return None

def create_cursor(connection):
    cursor = connection.cursor()
    return cursor

# def consulta(connection):
#     cursor = connection.cursor()
#     cursor.execute('SELECT id, nombre FROM persona;')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# def alta(connection, id, nombre):
#     cursor = connection.cursor()
#     cursor.execute(f"INSERT INTO public.persona (id, nombre) VALUES ({id}, '{nombre}');")
#     connection.commit()

def create_rows(df_data, table, cursor, connection):
    cols = '","'.join([str(title) for title in df_data.columns.tolist()])
    for index, data in df_data.iterrows():
        sql = 'INSERT INTO public.'+table+'("'+cols+'") VALUES ("'+'","'.join(map(str,data.values))+'")'
        cursor.execute(sql)
    connection.commit()