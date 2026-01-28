import os

FILENAME = "appointments.txt"

# Create file if not exists
if not os.path.exists(FILENAME):
    open(FILENAME, "w").close()


# ---------- FILE FUNCTIONS ----------
def load_appointments():
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    return [line.strip().split(",") for line in lines if line.strip()]


def save_appointments(data):
    with open(FILENAME, "w") as file:
        for item in data:
            file.write(",".join(item) + "\n")


# ---------- USER FUNCTIONS (NO LOGIN) ----------
def book_appointment():
    name = input("Enter patient name: ")
    date = input("Enter date (DD-MM-YYYY): ")
    time = input("Enter time (HH:MM): ")

    data = load_appointments()

    for ap in data:
        if ap[1] == date and ap[2] == time:
            print("❌ This slot is already booked!")
            return

    data.append([name, date, time])
    save_appointments(data)
    print("✅ Appointment booked successfully!")


def view_appointments():
    data = load_appointments()

    if not data:
        print("No appointments found.")
        return

    print("\n--- All Appointments ---")
    for i, ap in enumerate(data, 1):
        print(f"{i}. Name: {ap[0]}, Date: {ap[1]}, Time: {ap[2]}")


# ---------- ADMIN FUNCTIONS ----------
def delete_appointment():
    data = load_appointments()

    if not data:
        print("No appointments to delete.")
        return

    view_appointments()
    try:
        choice = int(input("Enter appointment number to delete: "))
        if 1 <= choice <= len(data):
            removed = data.pop(choice - 1)
            save_appointments(data)
            print(f"❌ Appointment for {removed[0]} deleted.")
        else:
            print("Invalid choice.")
    except:
        print("Enter valid number.")


def admin_login():
    username = input("Admin username: ")
    password = input("Admin password: ")

    if username == "admin" and password == "admin123":
        print("✅ Admin login successful!")
        admin_menu()
    else:
        print("❌ Invalid admin login!")


def admin_menu():
    while True:
        print("\n==== ADMIN MENU ====")
        print("1. View all appointments")
        print("2. Delete appointment")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_appointments()
        elif choice == "2":
            delete_appointment()
        elif choice == "3":
            print("Logging out from admin...")
            break
        else:
            print("Invalid choice.")


# ---------- USER MENU ----------
def user_menu():
    while True:
        print("\n==== USER MENU ====")
        print("1. Book appointment")
        print("2. View appointments")
        print("3. Back to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# ---------- MAIN MENU ----------
def main_menu():
    while True:
        print("\n=== Online Appointment Booking System ===")
        print("1. Book Appointment (User)")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            admin_login()
        elif choice == "3":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice.")


# ---------- START PROGRAM ----------
main_menu()