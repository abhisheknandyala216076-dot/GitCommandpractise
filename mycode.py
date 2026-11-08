
students = []

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("--------------------")
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])

def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")

def calculate_average():
    if not students:
        print("No marks available.")
        return

    total = sum(s["marks"] for s in students)
    average = total / len(students)

    print("Average marks:", average)

def show_topper():
    if not students:
        print("No student records.")
        return

    topper = max(students, key=lambda s: s["marks"])

    print("Topper:", topper["name"])
    print("Marks:", topper["marks"])

def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def show_menu():
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Show Topper")
    print("6. Delete Student")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            show_topper()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
