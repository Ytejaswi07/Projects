def display_menu():
    print("Simple To-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

def get_user_choice():
    return input("Choose an option: ")
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['task']} [{status}]")
def mark_task_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")
def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['task']}' deleted.")
    else:
        print("Invalid task number.")
import json

def save_tasks_to_file(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print(f"Tasks saved to {filename}.")
def load_tasks_from_file(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print(f"Tasks loaded from {filename}.")
        return tasks
    except FileNotFoundError:
        print(f"No existing task file found. Starting with an empty list.")
        return []
def main():
    tasks = load_tasks_from_file()
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks_to_file(tasks)
        elif choice == "6":
            tasks = load_tasks_from_file()
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
