# lib/models/__init__.py

import sqlite3

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect('freelancer_management.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Ensures foreign key constraints
    return conn

def initialize_db():
    """Initializes the database by creating tables for clients and projects."""
    from lib.models.client import Client
    from lib.models.project import Project
    Client.create_table()
    Project.create_table()
