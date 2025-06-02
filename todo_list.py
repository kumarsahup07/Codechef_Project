from datetime import datetime

def userChoice(choice, tasks):
    if choice == 1:
        task_name = input("Enter task name: ")
        deadline = input("Enter deadline (DD-MM-YYYY): ")
        add_task(tasks, task_name, deadline)
    elif choice == 2:
        if not tasks:
            print("No tasks to delete.\n")
        else:
            task_number = int(input("Enter task number to delete: "))
            delete_task(tasks, task_number)
    elif choice == 3:
        display_tasks(tasks)
    elif choice == 4: 
        return "Exiting application. Goodbye!"
    else:
        print("Invalid choice!\n")
    return None


def validate_date(deadline):
    try:
        # Convert the string deadline into a datetime object
        deadline_date = datetime.strptime(deadline, "%d-%m-%Y").date()
        return deadline_date
    except ValueError:
        print("Invalid date format! Please use DD-MM-YYYY.\n")
        return None


def add_task(tasks, task_name, deadline):
    deadline_date = validate_date(deadline)
    if deadline_date:
        tasks.append({"task": task_name, "deadline": deadline_date})
        print(f"Task '{task_name}' added with deadline {deadline_date}\n")


def delete_task(tasks, task_number):
    """Deletes a task from the task list based on user input."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed['task']}' deleted successfully!\n")
    else:
        print("Invalid task number!\n")


def display_tasks(tasks):
    """Displays all tasks along with their deadlines."""
    if not tasks:
        print("No tasks to display.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} (Deadline: {task['deadline']})")
        print()


if __name__ == "__main__":
    tasks = []
    print("\nWelcome to the To-Do List Application!\n")
    
    while True:
        print("Choose one operation:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            value = userChoice(choice, tasks)
            if value == "Exiting application. Goodbye!":
                print(value)
                break
        except ValueError:
            print("Please enter a valid number (1–4).\n")
