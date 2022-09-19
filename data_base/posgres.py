import psycopg2
import numpy as np

def connection_history():
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'jumped8285',
            database = 'prueba'
        )
        return connection
    except Exception as ex:
        print(ex)
        return None

def consulta(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT id, nombre FROM persona;')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def alta(connection, id, nombre):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO public.persona (id, nombre) VALUES ({id}, '{nombre}');")
    connection.commit()

def main():
    connection = connection_history()
    consulta(connection)
    for i in range(5):
        alta(connection, np.random.randint(0, 10000), 'jose')
    consulta(connection)


if __name__ == '__main__':
    main()
