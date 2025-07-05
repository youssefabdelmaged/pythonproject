from auth import register, login
from projects import create_project, view_projects, edit_project, delete_project

def main_menu():
    print("\n=== CrowdFunding App ===")
    print("1. Register")
    print("2. Login")
    print("0. Exit")
    return input("Choose: ")

def project_menu(user):
    while True:
        print(f"\nHello {user['first_name']}, choose an option:")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("0. Logout")
        choice = input("Choose: ")

        if choice == "1":
            create_project(user["user_id"])
        elif choice == "2":
            view_projects()
        elif choice == "3":
            edit_project(user["user_id"])
        elif choice == "4":
            delete_project(user["user_id"])
        elif choice == "0":
            break
        
        

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                project_menu(user)
        elif choice == "0":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")