def apply_migration(connection, migration_function):
    """
    Apply a migration function to the database.

    :param connection: SQLite connection object.
    :param migration_function: A function that takes a connection and applies schema changes.
    """
    try:
        migration_function(connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise Exception(f"An error occurred while applying the migration: {e}")

def rollback_migration(connection, rollback_function):
    """
    Rollback a migration using a rollback function.

    :param connection: SQLite connection object.
    :param rollback_function: A function that takes a connection and reverts schema changes.
    """
    try:
        rollback_function(connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise Exception(f"An error occurred while rolling back the migration: {e}")

# Example migrations (these would typically be in separate files or defined elsewhere)

def create_users_table(connection):
    """
    A migration function to create the users table.
    """
    connection.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

def drop_users_table(connection):
    """
    A rollback function to drop the users table.
    """
    connection.execute('DROP TABLE IF EXISTS users')