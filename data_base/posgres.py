import psycopg2

def conection_history():
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'jumped8285',
            databaes = 'test'
        )
        return connection
    except Exception as ex:
        print(ex)
        return None

