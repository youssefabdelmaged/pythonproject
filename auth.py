import json
import os
from utils import validate_email, validate_egyptian_phone_number, validate_date

USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def register():
    print("Register New Account")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email format. Please try again.")
        email = input("Enter your email: ")

    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

    phone_number = input("Enter your phone number: ")
    while not validate_egyptian_phone_number(phone_number):
        print("Invalid Egyptian phone number format. Please try again.")
        phone_number = input("Enter your phone number: ")

    users = load_users()
    for user in users:
        if user["email"] == email:
            print("Email already exists. Please try again.")
            return

    user = {
        "user_id": len(users) + 1,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone_number": phone_number,
    }

    users.append(user)
    save_users(users)
    print("Registration successful!")


def login():
    print("Login")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    users = load_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome, {user['first_name']} {user['last_name']}!")
            return user
    print("Invalid email or password. Please try again.")
    return None
