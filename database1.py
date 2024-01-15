import csv
import mysql.connector
from mysql.connector import Error

def read_csv(file_path):
    """
    Read data from a CSV file.
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            data.append(row)
    return headers, data

def connect_to_database(host, user, password, database):
    """
    Establish a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def create_table_if_not_exists(connection, headers):
    """
    Create 'geoevents' table if it does not exist.
    """
    try:
        cursor = connection.cursor()
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS geoevents (
            {', '.join([f'{header} VARCHAR(255)' for header in headers])}
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
    except Error as e:
        print(f"Error creating table: {e}")

def insert_data_into_table(connection, headers, data):
    """
    Insert data into the 'geoevents' table.
    """
    try:
        cursor = connection.cursor()
        insert_query = f"""
        INSERT INTO geoevents ({', '.join(headers)}) VALUES ({', '.join(['%s' for _ in headers])});
        """
        for row in data:
            cursor.execute(insert_query, tuple(row))
        connection.commit()
    except Error as e:
        print(f"Error inserting data into table: {e}")

def main(file_path, db_credentials):
    """
    Main function to execute the script.
    """
    # Read data from CSV
    headers, data = read_csv(file_path)

    # Connect to database
    db_connection = connect_to_database(**db_credentials)
    if db_connection is None:
        return

    # Create table if not exists
    create_table_if_not_exists(db_connection, headers)

    # Insert data into table
    insert_data_into_table(db_connection, headers, data)

    # Close database connection
    db_connection.close()


# Define database credentials and CSV file path
db_credentials = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'admin1',
    'database': 'Seysmo'
}
csv_file_path = r'C:\Users\Oleksandr\Downloads\NADD.xlsx - Sheet1.csv'


# Execute the script
main(csv_file_path, db_credentials)

