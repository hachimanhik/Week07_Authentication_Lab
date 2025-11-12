import bcrypt
import os

USER_DATA_FILE = "users.txt"


def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")                          # convert bytes to string



def verify_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(
        plain_text_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )



def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            stored_user = line.strip().split(",")[0]
            if stored_user == username:
                return True
    return False


def register_user(username, password):
    # check duplicate user
    if user_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return False

    # hash the password
    hashed = hash_password(password)

    # append new user to file
    with open(USER_DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed}\n")

    print(f"Success: User '{username}' registered successfully.")
    return True


def login_user(username, password):
    if not os.path.exists(USER_DATA_FILE):
        print("Error: No users registered yet.")
        return False

    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            stored_user, stored_hash = line.strip().split(",")
            if stored_user == username:
                if verify_password(password, stored_hash):
                    print(f"Login Successful — Welcome, {username}!")
                    return True
                else:
                    print("Error: Invalid password.")
                    return False

    print("Error: Username not found.")
    return False



def display_menu():
    """Displays the main menu."""
    print("\n" + "="*50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def validate_username(username):
    if not username:
        print("Error: Username cannot be empty.")
        return False
    if " " in username or "," in username in username:
        print("Error: Username cannot contain spaces or , .")
        return False
    if len(username) < 3:
        print("Error: Username must be at least 3 characters long.")
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return False
    if password.isdigit() or password.isalpha():
        print("Error: Password must contain at least one number.")
        return False
    if " " in password:
        print("Error: Password cannot contain spaces.")
        return False
    return True

def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == "1":
            # Registration flow
            print("\n---USER REGISTRATION---")
            username = input("Enter a username: ").strip()

            # Validate username
            if not validate_username(username):
                continue

            password = input("Enter a password: ").strip()

            #Validate Password
            if not validate_password(password):
                continue
            # Confirm Password
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # Register the user
            register_user(username, password)

        elif choice == "2":
            # Login flow
            print("\n---USER LOGIN---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt login
            if login_user(username, password):
                print("\nYou are now logged in.")
                print("In a real application, you would now access the dashboard.")

                # Optional: Ask if they want to logout or exit
                input("\nPress Enter to return main menu...")
        elif choice == "3":
                # Exit
                print("\nThank you for using Authentication System.")
                print("Exiting...")
                break
        else:
            print("Error: Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

