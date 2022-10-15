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
            database = db_data['name']
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

def exception_handler(function):
    def try_except_decorator(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            print(e)
    return try_except_decorator

@exception_handler
def execute_sql(connection, cursor, sql):
    cursor.execute(sql)
    print(sql)
    connection.commit()

def create_rows(df_data, table):
    query = list()
    cols = '","'.join([str(title) for title in df_data.columns.tolist()])
    for index, data in df_data.iterrows():
        sql = 'INSERT INTO public.'+table+'("'+cols+'") VALUES ('+"'"+"','".join(map(str,data.values))+"')"
        query.append(sql)
    return query