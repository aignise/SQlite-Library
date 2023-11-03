from .connection import get_connection, execute_query, fetch_results
from .query import insert_data, update_data, delete_data, fetch_data
from .migration import apply_migration, create_users_table, drop_users_table
from .utilities import dict_factory, batch_insert, table_exists

# Example of creating a database connection
def example_connection():
    db_path = 'example.db'
    connection = get_connection(db_path)
    print("Database connection created.")

# Example of creating a table
def example_create_table():
    db_path = 'example.db'
    connection = get_connection(db_path)
    apply_migration(connection, create_users_table)
    print("Users table created.")

# Example of inserting data
def example_insert_data():
    db_path = 'example.db'
    connection = get_connection(db_path)
    user_data = {
        'username': 'johndoe',
        'password': 'securepassword',
        'email': 'johndoe@example.com'
    }
    insert_data(connection, 'users', user_data)
    print("Data inserted into users table.")

# Example of updating data
def example_update_data():
    db_path = 'example.db'
    connection = get_connection(db_path)
    updates = {'password': 'newpassword'}
    conditions = {'username': 'johndoe'}
    update_data(connection, 'users', updates, conditions)
    print("User password updated.")

# Example of deleting data
def example_delete_data():
    db_path = 'example.db'
    connection = get_connection(db_path)
    conditions = {'username': 'johndoe'}
    delete_data(connection, 'users', conditions)
    print("User data deleted.")

# Example of fetching data
def example_fetch_data():
    db_path = 'example.db'
    connection = get_connection(db_path)
    rows = fetch_data(connection, 'users')
    for row in rows:
        print(row)

# Example of using utility functions
def example_utility_functions():
    db_path = 'example.db'
    connection = get_connection(db_path)
    
    # Check if table exists
    if table_exists(connection, 'users'):
        print("The 'users' table exists.")
    
    # Use the dict_factory to fetch data as dictionaries
    connection.row_factory = dict_factory
    rows = fetch_data(connection, 'users')
    for row in rows:
        print(row)

    # Batch insert data
    users = [
        ('alice', 'password123', 'alice@example.com'),
        ('bob', 'password456', 'bob@example.com')
    ]
    batch_insert(connection, 'users', ['username', 'password', 'email'], users)
    print("Batch data inserted into users table.")