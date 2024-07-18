class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")
    main()
