# Simple To-Do List App (Console Based)

FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Enter task number to remove: "))
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except:
        print("Invalid number!")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


main()
