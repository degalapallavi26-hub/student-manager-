import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter Student ID: ")

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    try:
        age = int(age)
        marks = float(marks)

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks!")
            return

    except ValueError:
        print("Age must be an integer and marks must be a number.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print("-" * 30)
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])


def search_student(students):
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print("Leave a field blank to keep its current value.")

            name = input(f"Name ({student['name']}): ")
            age = input(f"Age ({student['age']}): ")
            course = input(f"Course ({student['course']}): ")
            marks = input(f"Marks ({student['marks']}): ")

            try:
                new_age = int(age) if age else student["age"]
                new_marks = float(marks) if marks else student["marks"]

                if new_age <= 0 or not 0 <= new_marks <= 100:
                    print("Invalid age or marks!")
                    return

            except ValueError:
                print("Invalid age or marks!")
                return

            student["name"] = name if name else student["name"]
            student["age"] = new_age
            student["course"] = course if course else student["course"]
            student["marks"] = new_marks

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()

