# Python To-Do List (CLI)

A simple command-line to-do list application built in Python as part of my summer skill-building projects. This was designed to practice core programming fundamentals: data structures, functions, input validation, and file persistence.

## Features

- **Add tasks** — add new tasks to your list
- **View tasks** — see all tasks with their status (Pending/Completed)
- **Remove tasks** — delete a task by its number
- **Mark tasks as completed** — update a task's status without deleting it
- **Persistent storage** — tasks are saved to a `tasks.json` file, so your list is still there the next time you run the program
- **Input validation** — handles invalid menu choices and non-numeric input gracefully, without crashing

## How It Works

Tasks are stored as a list of dictionaries in memory:
```python
{"Task": "Buy Milk", "Status": "Pending"}
```

On every change (add, remove, mark completed), the list is saved to `tasks.json` using Python's built-in `json` module. When the program starts, it loads any existing tasks from that file — solving the problem of data being lost when the program closes (since RAM is volatile, but files on disk are not).

## Tech Used

- Python 3
- Built-in `json` module for file-based persistence

## How to Run

```bash
python todo.py
```

You'll see a menu like this:
```
===== Todo List Application =====
1. Add Task
2. View Tasks
3. Remove Task
4. Mark Task as Completed
5. Exit
```
Enter a number to choose an option, and follow the prompts.

## Project Structure

```
Python-todo-app/
  ├── todo.py        # main application logic
  └── tasks.json      # auto-generated file storing your tasks
```

## What I Practiced

- Working with lists and dictionaries
- Writing clean, decoupled functions (separating data logic from the menu/UI logic)
- Using `enumerate()` for readable iteration
- Handling invalid user input with `try`/`except`
- File handling and the `json` module for persistence
- Git/GitHub workflow with small, incremental commits

## Possible Future Improvements

- Rebuild persistence using SQLite instead of JSON (in progress as a follow-up project)
- Add due dates and priority levels to tasks
- Add task editing (not just remove/mark completed)