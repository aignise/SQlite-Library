def dict_factory(cursor, row):
    """
    Convert query results to a dictionary.
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def batch_insert(connection, table, columns, data):
    """
    Insert multiple records at once into the given table.

    :param connection: SQLite connection object.
    :param table: Table name to insert data into.
    :param columns: List of column names for the insert.
    :param data: List of tuples representing the data to insert.
    """
    placeholders = ', '.join(['?'] * len(columns))
    query = f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({placeholders})'
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()

def table_exists(connection, table_name):
    """
    Check if a table exists in the database.

    :param connection: SQLite connection object.
    :param table_name: Name of the table to check.
    :return: True if the table exists, False otherwise.
    """
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return cursor.fetchone()[0] == 1
    finally:
        cursor.close()