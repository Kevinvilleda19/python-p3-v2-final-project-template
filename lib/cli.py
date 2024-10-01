# lib/cli.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers import (
    add_client, view_clients, delete_client, reset_clients,  # Add reset_clients
    add_project, view_projects, delete_project, reset_projects,  # Add reset_projects
    view_projects_for_client, mark_project_as_paid
)
from lib.models import initialize_db

def main():
    """Main entry point for the Freelancer Job Management System CLI."""
    initialize_db()  # Ensure tables are created

    while True:
        print("\nFreelancer Job Management System")
        print("1. Manage Clients")
        print("2. Manage Projects")
        print("3. Reset Client IDs")  # Option to reset client IDs
        print("4. Reset Project IDs")  # Option to reset project IDs
        print("5. Exit")
        choice = input("> ")

        if choice == "1":
            client_menu()
        elif choice == "2":
            project_menu()
        elif choice == "3":
            reset_clients()  # Call the reset_clients function
        elif choice == "4":
            reset_projects()  # Call the reset_projects function
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def client_menu():
    """Displays the client management menu."""
    while True:
        print("\nClient Menu")
        print("1. Add Client")
        print("2. View Clients")
        print("3. Delete Client")
        print("4. Back to Main Menu")
        choice = input("> ")

        if choice == "1":
            add_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            delete_client()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

def project_menu():
    """Displays the project management menu."""
    while True:
        print("\nProject Menu")
        print("1. Add Project")
        print("2. View Projects")
        print("3. Mark Project as Paid")
        print("4. Delete Project")
        print("5. View Projects for a Client")
        print("6. Back to Main Menu")
        choice = input("> ")

        if choice == "1":
            add_project()
        elif choice == "2":
            view_projects()
        elif choice == "3":
            mark_project_as_paid()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            view_projects_for_client()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
