import json
import os

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = {'id': task_id, 'title': title, 'completed': False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        for task in self.tasks:
            status = "Done" if task['completed'] else "Not Done"
            print(f"{task['id']}. {task['title']} - {status}")

    def update_task(self, task_id, new_title=None, completed=None):
        for task in self.tasks:
            if task['id'] == task_id:
                if new_title:
                    task['title'] = new_title
                if completed is not None:
                    task['completed'] = completed
                self.save_tasks()
                print(f"Task '{task_id}' updated.")
                return
        print(f"Task with id '{task_id}' not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print(f"Task '{task_id}' deleted.")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)

def main():
    todo_list = TodoList()
    
    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_title = input("Enter new title (leave blank to keep current): ")
            completed_str = input("Is the task completed? (yes/no/leave blank to keep current): ").strip().lower()
            completed = None
            if completed_str == 'yes':
                completed = True
            elif completed_str == 'no':
                completed = False
            todo_list.update_task(task_id, new_title if new_title else None, completed)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()