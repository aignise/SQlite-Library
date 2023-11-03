import sqlite3

def get_connection(db_path):
    """
    Get a SQLite database connection.
    
    :param db_path: Path to the SQLite database file.
    :return: SQLite connection object.
    """
    try:
        return sqlite3.connect(db_path)
    except sqlite3.Error as e:
        raise Exception(f"An error occurred while connecting to the database: {e}")

def execute_query(connection, query, params=None):
    """
    Execute a SQL query directly, for queries that don't return results.
    
    :param connection: SQLite connection object.
    :param query: SQL query to execute.
    :param params: Optional parameters for the SQL query.
    """
    if params is None:
        params = ()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"An error occurred while executing the query: {e}")
    finally:
        cursor.close()

def fetch_results(connection, query, params=None):
    """
    Execute a SQL query and return fetched results.
    
    :param connection: SQLite connection object.
    :param query: SQL query to execute.
    :param params: Optional parameters for the SQL query.
    :return: Fetched query results.
    """
    if params is None:
        params = ()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        raise Exception(f"An error occurred while fetching the results: {e}")
    finally:
        cursor.close()