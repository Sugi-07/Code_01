import os

FILE_NAME = "students.txt"

# Add student
def add_student():
    with open(FILE_NAME, "a") as file:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        file.write(f"{student_id},{name},{age},{course}\n")
        print("✅ Student added successfully!\n")


# View all students
def view_students():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if not records:
            print("⚠️ No records available.\n")
            return

        print("\n📋 Student Records:")
        for record in records:
            student_id, name, age, course = record.strip().split(",")
            print(f"ID: {student_id} | Name: {name} | Age: {age} | Course: {course}")
        print()


# Search student
def search_student():
    search_id = input("Enter Student ID to search: ")

    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        found = False
        for record in file:
            student_id, name, age, course = record.strip().split(",")
            if student_id == search_id:
                print(f"✅ Found: ID: {student_id}, Name: {name}, Age: {age}, Course: {course}\n")
                found = True
                break

        if not found:
            print("❌ Student not found.\n")


# Delete student
def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    with open(FILE_NAME, "w") as file:
        found = False
        for record in records:
            student_id, name, age, course = record.strip().split(",")
            if student_id != delete_id:
                file.write(record)
            else:
                found = True

    if found:
        print("✅ Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")


# Main menu
def main():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
