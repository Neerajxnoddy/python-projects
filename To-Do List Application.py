# To-Do List Application

tasks = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task_number=int(input("how many task you want to add:"))
    for i in range(task_number):
        task = input("Enter the task: ")
        tasks.append(task)
    print("task added successfully")

def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        n=1
        for i in tasks:
            print(n,".",i)
            n+=1
    else:
        print("Your to-do list is empty.")

def remove_task():
    view_tasks()
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()