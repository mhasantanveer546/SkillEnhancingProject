my_tasks = []

def add_task(task):
    my_tasks.append(task)
    print(f'Task "{task}" added successfully!')
    
def view_tasks():
    if not my_tasks:
        print("No tasks in your todo list.")
    else:
        print("Todo List:")
        for i, task in enumerate(my_tasks, 1):
            print(f"{i}. {task}")

def remove_task(task_number):
    if 1 <= task_number <= len(my_tasks):
        removed_task = my_tasks.pop(task_number -1)
        print(f'Task "{removed_task}" removed successfully!')
    else:
        print("Invalid task number! Please enter a valid task number.")





add_task("Buy Milk")
add_task("Walk Dog")
view_tasks()
remove_task(1)
view_tasks()
remove_task(10)  # should fail gracefully