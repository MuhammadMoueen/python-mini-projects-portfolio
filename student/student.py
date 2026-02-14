import json

FILE_NAME = "students.json"


class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data
    except:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def show_students(students):
    if not students:
        print("\nNo students found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")


def add_student(students):
    sid = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    student = Student(sid, name, age, grade)
    students.append(student.to_dict())
    save_students(students)
    print("Student added!")


def edit_student(students):
    sid = input("Enter student ID to edit: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("New name: ")
            s["age"] = input("New age: ")
            s["grade"] = input("New grade: ")
            save_students(students)
            print("Student updated!")
            return

    print("Student not found!")


def delete_student(students):
    sid = input("Enter student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("Student deleted!")
            return

    print("Student not found!")


def main():
    students = load_students()

    while True:
        print("\n--- STUDENT SYSTEM ---")
        print("1. View Students")
        print("2. Add Student")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            edit_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


main()
