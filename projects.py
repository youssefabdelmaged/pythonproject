import json
import os
from datetime import datetime
from utils import validate_date

PROJECTS_FILE = "data/projects.json"


def load_projects():
    if not os.path.exists(PROJECTS_FILE):
        return []
    with open(PROJECTS_FILE, "r") as f:
        return json.load(f)


def save_projects(projects):
    with open(PROJECTS_FILE, "w") as f:
        json.dump(projects, f, indent=4)


def create_project(user_id):
    print("Create New Project")
    project_title = input("Enter project name: ")
    details = input("Enter project details: ")
    target_amount = input("Target Amount (EGP): ")
    start = input("Enter target date (YYYY-MM-DD): ")

    while not validate_date(start):
        print("Invalid date format. Please use YYYY-MM-DD.")
        start = input("Enter target date (YYYY-MM-DD): ")

    end = input("End Date (YYYY-MM-DD): ")
    while not validate_date(end):
        end = input("Invalid. Try again: ")

    project = {
        "project_id": datetime.now().timestamp(),
        "owner_id": user_id,
        "title": project_title,
        "details": details,
        "total_target": target_amount,
        "start_date": start,
        "end_date": end
    }

    projects = load_projects()
    projects.append(project)
    save_projects(projects)
    print("Project created successfully!")


def view_projects():
    print("All Projects")
    projects = load_projects()
    for p in projects:
        print(
            f"{p['title']} | Target: {p['total_target']} EGP | From {p['start_date']} to {p['end_date']}")


def edit_project(user_id):
    projects = load_projects()
    pid = input("Enter project title to edit: ")
    for p in projects:
        if p["title"] == pid and p["owner_id"] == user_id:
            p["title"] = input("New Title: ")
            p["details"] = input("New Details: ")
            save_projects(projects)
            print("Project updated.")
            return
    print("Not found or unauthorized.")


def delete_project(user_id):
    projects = load_projects()
    pid = input("Enter project title to delete: ")
    new_projects = [p for p in projects if not (
        p["title"] == pid and p["owner_id"] == user_id)]
    if len(new_projects) != len(projects):
        save_projects(new_projects)
        print("Project deleted.")
    else:
        print("Project not found or unauthorized.")
