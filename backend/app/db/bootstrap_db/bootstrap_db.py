import sqlite3
from pathlib import Path

from app.config import settings


class BootstrapDb:
    """
    This class is responsible for initializing the database and managing the db_settings table.
    It provides methods to initialize the database, save settings, and load settings.
    The database is stored in a file named 'db_settings.db' in the current directory.

    The db_settings table contains the following columns:
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - host: TEXT NOT NULL
    - port: INTEGER NOT NULL
    - username: TEXT NOT NULL
    - password: TEXT NOT NULL
    - db_name: TEXT NOT NULL

    @author IFD
    @since 2025-05-05
    """

    dbpath = Path("db_settings.db")

    @classmethod
    def init_db(cls):
        """
        Initialize the database and create the db_settings table if it doesn't exist.
        If the table is empty, insert default settings from the config.
        This method should be called at the start of the application.

        If an error occurs while connecting to the database or executing SQL commands,
        an exception will be raised. The error message will be printed to the console
        and the system will set bootstrap_db_healthy to False.

        :return: None
        :raises sqlite3.Error: If there is an error connecting to the database or executing SQL commands.

        @author IFD
        @since 2025-05-05
        """
        try:
            with sqlite3.connect(cls.dbpath) as conn:
                cursor = conn.cursor()
                # Create table if it doesn't exist
                cursor.execute('''
                               CREATE TABLE IF NOT EXISTS db_settings
                               (
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   host TEXT NOT NULL,
                                   port INTEGER NOT NULL,
                                   username TEXT NOT NULL,
                                   password TEXT NOT NULL,
                                   db_name TEXT NOT NULL
                               )
                               ''')

                # Check if table is empty
                cursor.execute('SELECT COUNT(*) FROM db_settings')
                count = cursor.fetchone()[0]
                if count == 0:
                    cursor.execute('''
                                   INSERT INTO db_settings (host, port, username, password, db_name)
                                   VALUES (?, ?, ?, ?, ?)
                                   ''', (settings.DB_HOST, settings.DB_PORT, settings.DB_USER, settings.DB_PASSWORD, settings.DB_NAME))

                conn.commit()

                print("Bootstrap Database initialized successfully.")

        except Exception as e:
            print(f"An error occurred while initializing the bootstrap database: {e}")
            raise

    @classmethod
    def save_settings(cls, host, port, username, password, db_name):
        """
        Save the database settings to the db_settings table.
        This method deletes any existing records in the table and inserts a new record
        with the provided settings. This ensures that only one record exists in the table.
        This method should be called when the user updates the database settings.

        If an error occurs while connecting to the database or executing SQL commands,
        an exception will be raised. The error message will be printed to the console
        and the system will set bootstrap_db_healthy to False.

        :param host:
        :param port:
        :param username:
        :param password:
        :param db_name:
        :return:

        @author IFD
        @since 2025-05-05
        """
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM db_settings')  # ensure only one record
            cursor.execute('''
                           INSERT INTO db_settings (host, port, username, password, db_name)
                           VALUES (?, ?, ?, ?, ?)
                           ''', (host, port, username, password, db_name))
            conn.commit()

    @classmethod
    def load_db_settings(cls):
        """
        Load the database settings from the db_settings table.
        This method retrieves the first record from the table and returns it as a dictionary.
        If the table is empty or an error occurs while connecting to the database or executing SQL commands,
        an exception will be raised. The error message will be printed to the console and the system will
        set bootstrap_db_healthy to False.

        :return:

        @author IFD
        @since 2025-05-05
        """
        try:
           with sqlite3.connect(cls.dbpath) as conn:
               cursor = conn.cursor()
               cursor.execute('SELECT host, port, username, password, db_name FROM db_settings LIMIT 1')
               row = cursor.fetchone()
               if row:
                   return {
                       'host': row[0],
                       'port': row[1],
                       'username': row[2],
                       'password': row[3],
                       'db_name': row[4],
                   }
               raise Exception("Bootstrap Database settings not found.")
        except Exception as e:
              print(f"An error occurred while loading the database settings: {e}")
              raise
