class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        return f"{self.name} - {self.due_date} - {'Completed' if self.completed else 'Not Completed'}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date):
        self.tasks.append(Task(name, due_date))

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Task '{name}' removed.")
                break
        else:
            print(f"Task '{name}' not found.")

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.completed = True
                print(f"Task '{name}' marked as completed.")
                break
        else:
            print(f"Task '{name}' not found.")

    def list_tasks(self):
        for task in self.tasks:
            print(task)


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            due_date = input("Enter due date (dd/mm/yyyy): ")
            todo_list.add_task(name, due_date)
        elif choice == "2":
            name = input("Enter task name: ")
            todo_list.remove_task(name)
        elif choice == "3":
            name = input("Enter task name: ")
            todo_list.complete_task(name)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()