# lib/models/project.py

from lib.models import get_db_connection

class Project:
    """Represents a project for a specific client."""

    @staticmethod
    def create_table():
        """Creates the projects table if it doesn't already exist."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                deadline TEXT NOT NULL,
                payment_status BOOLEAN DEFAULT 0,
                client_id INTEGER NOT NULL,
                FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE CASCADE
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def reset_table():
        """Drops and recreates the projects table, resetting the project IDs."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS projects")
        conn.commit()
        conn.close()
        Project.create_table()  # Recreate the table to reset IDs

    @staticmethod
    def add(description, deadline, client_id):
        """Adds a new project for a client to the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO projects (description, deadline, client_id)
            VALUES (?, ?, ?)
        """, (description, deadline, client_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        """Retrieves all projects from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()
        conn.close()
        return projects

    @staticmethod
    def find_by_id(project_id):
        """Finds a project by its ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
        project = cursor.fetchone()
        conn.close()
        return project

    @staticmethod
    def get_by_client(client_id):
        """Retrieves all projects associated with a specific client."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects WHERE client_id = ?", (client_id,))
        projects = cursor.fetchall()
        conn.close()
        return projects

    @staticmethod
    def mark_as_paid(project_id):
        """Marks a project as paid."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE projects SET payment_status = 1 WHERE id = ?", (project_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(project_id):
        """Deletes a project from the database by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
        conn.commit()
        conn.close()
