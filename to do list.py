Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def main():
    todo_list = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
...             remove_task(todo_list)
...         elif choice == "3":
...             display_tasks(todo_list)
...         elif choice == "4":
...             print("Exiting to-do list...")
...             break
...         else:
...             print("Invalid choice. Please try again.")
... 
... def print_menu():
...     print("\nTo-Do List Menu:")
...     print("1. Add a task")
...     print("2. Remove a task")
...     print("3. Display tasks")
...     print("4. Exit")
... 
... def add_task(todo_list):
...     task = input("Enter the task: ")
...     todo_list.append(task)
...     print(f"Task '{task}' added to the list.")
... 
... def remove_task(todo_list):
...     if not todo_list:
...         print("The to-do list is empty.")
...         return
... 
...     display_tasks(todo_list)
...     task_index = int(input("Enter the task number to remove: "))
... 
...     if task_index < 1 or task_index > len(todo_list):
...         print("Invalid task number.")
...         return
... 
...     removed_task = todo_list.pop(task_index - 1)
...     print(f"Task '{removed_task}' removed from the list.")
... 
... def display_tasks(todo_list):
...     if not todo_list:
...         print("The to-do list is empty.")
...         return
... 
...     print("\nCurrent Tasks:")
...     for i, task in enumerate(todo_list, start=1):
...         print(f"{i}. {task}")
... 
... if __name__ == "__main__":
