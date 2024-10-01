# lib/helpers.py

from models.client import Client
from models.project import Project
from datetime import datetime

def add_client():
    """Adds a new client to the system."""
    name = input("Enter client name: ")
    email = input("Enter client email: ")
    phone = input("Enter client phone: ")

    if not name or not email or not phone:
        print("Error: All fields are required.")
        return

    Client.add(name, email, phone)
    print(f"Client '{name}' added successfully.")

def view_clients():
    """Displays all clients in the system."""
    clients = Client.get_all()
    if not clients:
        print("No clients found.")
    for client in clients:
        print(f"ID: {client[0]} | Name: {client[1]} | Email: {client[2]} | Phone: {client[3]}")

def delete_client():
    """Deletes a client by ID."""
    client_id = input("Enter the client ID to delete: ")
    client = Client.find_by_id(client_id)
    if not client:
        print(f"Client with ID {client_id} not found.")
        return

    Client.delete(client_id)
    print(f"Client with ID {client_id} deleted.")

def reset_clients():
    """Resets the client table, including client IDs."""
    confirm = input("Are you sure you want to reset all client IDs? This will delete all clients. (yes/no): ")
    if confirm.lower() == "yes":
        Client.reset_table()
        print("All clients have been deleted and client IDs have been reset.")
    else:
        print("Client reset canceled.")

def add_project():
    """Adds a new project for a specific client."""
    client_id = input("Enter client ID for the project: ")
    client = Client.find_by_id(client_id)
    if not client:
        print(f"Client with ID {client_id} not found.")
        return

    description = input("Enter project description: ")
    deadline = input("Enter project deadline (MM-DD-YYYY): ")  # Prompt for MM-DD-YYYY format

    # Validate the MM-DD-YYYY format
    try:
        # Parse input to check if it matches MM-DD-YYYY format
        deadline_obj = datetime.strptime(deadline, "%m-%d-%Y")
    except ValueError:
        print("Error: Invalid date format. Use MM-DD-YYYY.")
        return

    # Store the deadline in the format MM-DD-YYYY
    deadline_str = deadline_obj.strftime("%m-%d-%Y")

    Project.add(description, deadline_str, client_id)
    print(f"Project '{description}' added successfully for client ID {client_id}.")

def view_projects():
    """Displays all projects in the system."""
    projects = Project.get_all()
    if not projects:
        print("No projects found.")
    for project in projects:
        # The date is already stored in MM-DD-YYYY format
        print(f"ID: {project[0]} | Description: {project[1]} | Deadline: {project[2]} | Paid: {project[3]}")

def mark_project_as_paid():
    """Marks a project as paid."""
    project_id = input("Enter the project ID to mark as paid: ")
    project = Project.find_by_id(project_id)
    if not project:
        print(f"Project with ID {project_id} not found.")
        return

    Project.mark_as_paid(project_id)
    print(f"Project with ID {project_id} marked as paid.")

def delete_project():
    """Deletes a project by ID."""
    project_id = input("Enter the project ID to delete: ")
    project = Project.find_by_id(project_id)
    if not project:
        print(f"Project with ID {project_id} not found.")
        return

    Project.delete(project_id)
    print(f"Project with ID {project_id} deleted.")

def reset_projects():
    """Resets the project table, including project IDs."""
    confirm = input("Are you sure you want to reset all project IDs? This will delete all projects. (yes/no): ")
    if confirm.lower() == "yes":
        Project.reset_table()
        print("All projects have been deleted and project IDs have been reset.")
    else:
        print("Project reset canceled.")

def view_projects_for_client():
    """Displays all projects for a specific client."""
    client_id = input("Enter client ID to view projects: ")
    client = Client.find_by_id(client_id)
    if not client:
        print(f"Client with ID {client_id} not found.")
        return

    projects = Project.get_by_client(client_id)
    if not projects:
        print(f"No projects found for client ID {client_id}.")
        return

    for project in projects:
        print(f"ID: {project[0]} | Description: {project[1]} | Deadline: {project[2]} | Paid: {project[3]}")
