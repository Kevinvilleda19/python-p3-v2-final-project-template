Freelancer Job Management System
Introduction
The Freelancer Job Management System is a Command Line Interface (CLI) application that helps freelancers manage their clients, projects, and payment statuses. This system allows you to add, view, and delete clients and projects, track project statuses (paid or unpaid), and reset the project and client IDs by resetting their respective tables.

The application uses SQLite as the database engine and is built using Python's sqlite3 module to interact with the database.

Features
Client Management:

Add a new client with their name, email, and phone number.
View all clients in the system.
Delete clients by their ID.
Reset client IDs by dropping and recreating the clients table.
Project Management:

Add a project for a specific client, including description, deadline, and payment status.
View all projects in the system.
Mark projects as paid.
Delete projects by their ID.
View projects associated with a specific client.
Reset project IDs by dropping and recreating the projects table.
Prerequisites
To run this project, you need the following installed:

Python 3.x
Pipenv (if using pipenv for dependency management)
Installation and Setup
Clone the repository:

bash
Copy code
git clone <repository-url>
Navigate to the project directory:

bash
Copy code
cd <project-directory>
Install dependencies using Pipenv (if you're using it):

bash
Copy code
pipenv install
Activate the virtual environment:

bash
Copy code
pipenv shell
Run the application:

bash
Copy code
python lib/cli.py
Usage
Once the application is running, you'll be presented with the main menu that offers various options for managing clients and projects.

Main Menu Options
1. Manage Clients: Enter the Client Management menu where you can add, view, and delete clients.
2. Manage Projects: Enter the Project Management menu where you can add, view, delete, mark projects as paid, and view projects for a specific client.
3. Reset Client IDs: Drop and recreate the clients table, resetting the client IDs.
4. Reset Project IDs: Drop and recreate the projects table, resetting the project IDs.
5. Exit: Exit the application.
Client Management Menu
1. Add Client: Add a new client by entering the client's name, email, and phone number.
2. View Clients: View all clients currently stored in the system.
3. Delete Client: Delete a client by providing their ID.
4. Back to Main Menu: Return to the main menu.
Project Management Menu
1. Add Project: Add a project for a specific client by entering the client ID, project description, deadline (MM-DD-YYYY), and payment status.
2. View Projects: View all projects currently stored in the system.
3. Mark Project as Paid: Mark a project as paid by providing the project ID.
4. Delete Project: Delete a project by providing its ID.
5. View Projects for a Client: View all projects associated with a specific client by providing the client ID.
6. Back to Main Menu: Return to the main menu.
Resetting Client and Project IDs
You can reset the clients or projects tables by choosing the respective options in the main menu:

Reset Client IDs: This option drops the clients table and recreates it, which resets the AUTOINCREMENT ID for clients.
Reset Project IDs: This option drops the projects table and recreates it, resetting the AUTOINCREMENT ID for projects.
Note: Resetting the tables will delete all existing clients or projects and reset the IDs to start from 1 again.

Directory Structure
The project follows a modular structure for easy organization and maintainability:

graphql
Copy code
.
├── Pipfile             # Pipenv dependency manager configuration file
├── Pipfile.lock        # Pipenv lock file
├── README.md           # Documentation file
└── lib
    ├── models          # Contains the ORM models for Clients and Projects
    │   ├── __init__.py  # Database connection setup
    │   ├── client.py    # Client model with methods for CRUD operations and resetting client table
    │   └── project.py   # Project model with methods for CRUD operations and resetting project table
    ├── cli.py           # Main CLI logic and user interface
    └── helpers.py       # Helper functions for managing clients and projects
Example Workflow
Here’s a sample workflow for managing clients and projects:

Add a Client:

Select option 1 (Manage Clients).
Select 1 (Add Client), then input the name, email, and phone of the client.
The client is added to the system with a unique ID.
Add a Project:

Select option 2 (Manage Projects).
Select 1 (Add Project), then input the project description, deadline (in MM-DD-YYYY format), and client ID.
The project is linked to the client and can be tracked.
Mark Project as Paid:

Select option 2 (Manage Projects).
Select 3 (Mark Project as Paid), then input the project ID to mark it as paid.
Reset Client or Project IDs:

From the main menu, select option 3 or 4 to reset client or project IDs. This will drop and recreate the respective tables, resetting their IDs.
License
This project is licensed under the MIT License.