# Python Expense Tracker (CLI)

A command-line expense tracker built in Python as part of my summer skill-building projects. This project focuses on the "accumulator pattern," defensive input handling, and using a real database (SQLite) as the single source of truth for persistent data.

## Features

- **Add expenses** — enter a description and amount for each expense
- **Running total** — automatically calculates the total of all expenses
- **Input validation** — rejects non-numeric input and negative amounts without crashing, re-prompting until valid input is given
- **Persistent storage with SQLite** — all expenses are stored in a real database (`expenses.db`), so data survives across program runs
- **Expense breakdown** — view all recorded expenses individually alongside the grand total

## How It Works

Each expense is stored as a row in a SQLite table:
```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL
)
```

Rather than keeping expenses in an in-memory list, every expense is inserted directly into the database. When the program displays the final breakdown and total, it queries the database fresh — meaning the database is the single source of truth, not a separate in-memory variable that could drift out of sync.

All database writes use **parameterized queries** (`?` placeholders) rather than string-formatted SQL, to avoid SQL injection risks — a practice that carries over to any real-world database work.

## Tech Used

- Python 3
- Built-in `sqlite3` module (no external dependencies or server setup required)

## How to Run

```bash
python expense_tracker.py
```

You'll be prompted to enter expenses one at a time:
```
Enter an expense description (or type 'Exit' to quit):
Enter an expense amount:
```
Type `Exit` as the description when you're done. The program will then display a full breakdown of all expenses (including ones from previous runs) and the grand total.

## Project Structure

```
Python-expense-tracker/
  ├── expense_tracker.py   # main application logic
  └── expenses.db           # auto-generated SQLite database storing expenses
```

## What I Practiced

- The accumulator pattern (running totals)
- Sentinel-controlled loops (looping until a specific input like "Exit")
- Defensive coding with `try`/`except` and custom validation (rejecting negative numbers)
- Writing and executing real SQL from Python (`CREATE TABLE`, `INSERT`, `SELECT`)
- Using parameterized queries to prevent SQL injection
- Designing a program around a single source of truth instead of duplicating state
- Git/GitHub workflow with small, incremental commits

## Possible Future Improvements

- Add categories (e.g., Food, Transport, Bills) per expense
- Add date tracking for each expense
- Add the ability to delete or edit individual expenses
- Rebuild persistence using SQL Server + `pyodbc` as a follow-up exercise