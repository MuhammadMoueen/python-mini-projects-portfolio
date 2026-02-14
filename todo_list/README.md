# To-Do List App

A simple console-based to-do list application that helps you manage your daily tasks.

## Features

- ✅ View all tasks
- ➕ Add new tasks
- ❌ Remove completed tasks
- 💾 Persistent storage (saves to file)
- 🎯 Simple and intuitive interface

## Requirements

- Python 3.x

## How to Run

```bash
python todo.py
```

## Usage

1. **View Tasks**: Displays all your current tasks
2. **Add Task**: Enter a new task to add to your list
3. **Remove Task**: Select a task number to remove it
4. **Exit**: Save and exit the application

## File Storage

Tasks are stored in `tasks.txt` in the same directory. The file is automatically created on first run.

## Example

```
--- TO DO LIST ---
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
Choose option: 2
Enter new task: Buy groceries
Task added successfully!
```

## Code Structure

- `load_tasks()`: Loads tasks from file
- `save_tasks()`: Saves tasks to file
- `show_tasks()`: Displays all tasks
- `add_task()`: Adds a new task
- `remove_task()`: Removes a task by number
- `main()`: Main program loop

## Future Enhancements

- Mark tasks as complete without removing
- Priority levels for tasks
- Due dates for tasks
- Categories/tags for organization
