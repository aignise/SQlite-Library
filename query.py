def insert_data(connection, table, data):
    """
    Insert data into a table.

    :param connection: SQLite connection object.
    :param table: Table name to insert data into.
    :param data: Dictionary where keys are column names and values are data to insert.
    """
    placeholders = ', '.join(['?'] * len(data))
    columns = ', '.join(data.keys())
    values = list(data.values())
    query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    connection.execute(query, values)

def update_data(connection, table, data, condition):
    """
    Update data in a table based on a condition.

    :param connection: SQLite connection object.
    :param table: Table name to update data in.
    :param data: Dictionary of columns to update.
    :param condition: Dictionary representing the WHERE clause filter.
    """
    set_clause = ', '.join([f'{column} = ?' for column in data])
    where_clause = ' AND '.join([f'{key} = ?' for key in condition])
    values = list(data.values()) + list(condition.values())
    query = f'UPDATE {table} SET {set_clause} WHERE {where_clause}'
    connection.execute(query, values)

def delete_data(connection, table, condition):
    """
    Delete data from a table based on a condition.

    :param connection: SQLite connection object.
    :param table: Table name to delete data from.
    :param condition: Dictionary representing the WHERE clause filter.
    """
    where_clause = ' AND '.join([f'{key} = ?' for key in condition])
    values = list(condition.values())
    query = f'DELETE FROM {table} WHERE {where_clause}'
    connection.execute(query, values)

def fetch_data(connection, table, columns='*', condition=None, order_by=None):
    """
    Fetch data from a table.

    :param connection: SQLite connection object.
    :param table: Table name to fetch data from.
    :param columns: Columns to fetch, defaults to '*'.
    :param condition: Optional dictionary representing the WHERE clause filter.
    :param order_by: Optional string to order the results.
    :return: Query results.
    """
    if condition:
        where_clause = ' AND '.join([f'{key} = ?' for key in condition])
        values = list(condition.values())
        query = f'SELECT {columns} FROM {table} WHERE {where_clause}'
        if order_by:
            query += f' ORDER BY {order_by}'
        return connection.execute(query, values).fetchall()
    else:
        query = f'SELECT {columns} FROM {table}'
        if order_by:
            query += f' ORDER BY {order_by}'
        return connection.execute(query).fetchall()