import psycopg2
import numpy as np
import files.get_config as get_config

def connection_history():
    db_data = get_config.db_data()
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = db_data['user'],
            password = db_data['password'],
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