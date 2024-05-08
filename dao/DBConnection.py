import mysql.connector


def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user=r'root',
            password=r'Riyaiscute',
            database=r'project1'
        )
        print("Connected to MySQL")
        return connection

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


connect_to_mysql()