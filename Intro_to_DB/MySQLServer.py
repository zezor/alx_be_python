import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Connect to MySQL server (no database specified)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # <-- replace with your MySQL username
            password='Rasnaana12@'  # <-- replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
