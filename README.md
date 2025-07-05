# CrowdFunding App

## Project Description
This is a simple command-line CrowdFunding application that allows users to register, log in, and manage crowdfunding projects. Users can create, view, edit, and delete their own projects. The application validates user inputs such as email, Egyptian phone numbers, and dates to ensure data integrity.

## Features
- User registration with validation for email and Egyptian phone numbers.
- User login with email and password authentication.
- Create new crowdfunding projects with details, target amount, and date range.
- View all existing projects.
- Edit and delete projects owned by the logged-in user.
- Data persistence using JSON files for users and projects.

## Installation
1. Ensure you have Python 3 installed on your system.
2. Clone or download this repository.
3. Navigate to the project directory in your terminal.

## Usage
Run the application by executing the main script:

```bash
python3 main.py
```

Follow the on-screen menu to register a new account or log in. After logging in, you can manage your projects through the project menu.

## File Descriptions
- `main.py`: Entry point of the application. Handles the main menu and project menu interactions.
- `auth.py`: Contains functions for user registration and login, including input validation and data storage.
- `projects.py`: Contains functions to create, view, edit, and delete projects. Manages project data storage.
- `utils.py`: Utility functions for validating email addresses, Egyptian phone numbers, and date formats.
- `data/users.json`: JSON file storing registered user information.
- `data/projects.json`: JSON file storing project information.

## Data Storage
User and project data are stored locally in JSON files within the `data` directory:
- `users.json` stores user details such as name, email, password, and phone number.
- `projects.json` stores project details including title, description, target amount, dates, and owner ID.

## Input Validation
- Email addresses are validated using a regex pattern to ensure proper format.
- Egyptian phone numbers are validated to match common Egyptian number formats.
- Dates are validated to ensure they follow the `YYYY-MM-DD` format.

## License
This project is provided as-is without any warranty. Feel free to use and modify it as needed.
