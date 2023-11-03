import unittest
from .connection import get_connection, execute_query, fetch_results
from .query import insert_data, update_data, delete_data, fetch_data
from .migration import apply_migration, create_users_table, drop_users_table
from .utilities import table_exists

class TestSQLiteLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = 'test.db'
        cls.connection = get_connection(cls.db_path)
        apply_migration(cls.connection, create_users_table)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
        # Optionally, remove the test database file if needed

    def test_insert_data(self):
        user_data = {
            'username': 'testuser',
            'password': 'testpass',
            'email': 'testuser@example.com'
        }
        insert_data(self.connection, 'users', user_data)
        self.assertTrue(table_exists(self.connection, 'users'))

    def test_update_data(self):
        updates = {'password': 'newtestpass'}
        conditions = {'username': 'testuser'}
        update_data(self.connection, 'users', updates, conditions)
        rows = fetch_data(self.connection, 'users', condition=conditions)
        self.assertEqual(rows[0]['password'], 'newtestpass')

    def test_delete_data(self):
        conditions = {'username': 'testuser'}
        delete_data(self.connection, 'users', conditions)
        rows = fetch_data(self.connection, 'users', condition=conditions)
        self.assertEqual(len(rows), 0)

    def test_fetch_data(self):
        rows = fetch_data(self.connection, 'users')
        self.assertIsInstance(rows, list)

# To run the tests from the command line
# if __name__ == '__main__':
#     unittest.main()