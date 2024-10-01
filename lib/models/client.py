# lib/models/client.py

from lib.models import get_db_connection

class Client:
    """Represents a freelancer's client."""

    @staticmethod
    def create_table():
        """Creates the clients table if it doesn't already exist."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def reset_table():
        """Drops and recreates the clients table, resetting the client IDs."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS clients")
        conn.commit()
        conn.close()
        Client.create_table()  # Recreate the table to reset IDs

    @staticmethod
    def add(name, email, phone):
        """Adds a new client to the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clients (name, email, phone)
            VALUES (?, ?, ?)
        """, (name, email, phone))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        """Retrieves all clients from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()
        conn.close()
        return clients

    @staticmethod
    def find_by_id(client_id):
        """Finds a client by its ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
        client = cursor.fetchone()
        conn.close()
        return client

    @staticmethod
    def delete(client_id):
        """Deletes a client from the database by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
        conn.commit()
        conn.close()
