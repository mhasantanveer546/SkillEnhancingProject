my_tasks = []

def add_task(task):
    my_tasks.append({"Task": task, "Status": "Pending"})
    print(f'Task "{task}" added successfully!')
    
def view_tasks():
    if not my_tasks:
        print("No tasks in your todo list.")
    else:
        print("Todo List:")
        for i, task in enumerate(my_tasks, 1):
            print(f"{i}. {task['Task']} - {task['Status']}")

def remove_task(task_number):
    if 1 <= task_number <= len(my_tasks):
        removed_task = my_tasks.pop(task_number -1)
        print(f'Task "{removed_task["Task"]}" removed successfully!')
    else:
        print("Invalid task number! Please enter a valid task number.")

def mark_task_completed(task_number):
    if 1 <= task_number <= len(my_tasks):
        my_tasks[task_number -1]["Status"] = "Completed"
        print(f'Task "{my_tasks[task_number -1]["Task"]}" marked as completed!')
    else:
        print("Invalid task number! Please enter a valid task number.")


while True:
    print("===== Todo List Application =====")
    print("1. Add Task")
    print("2. View Tasks") 
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        try:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        except ValueError:
            print("That's not a valid number. Please try again.")
    elif choice == "4":
        view_tasks()
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(task_number)
        except ValueError:
            print("That's not a valid number. Please try again.")
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid Choice! Please enter a valid option (1-5).")
    

