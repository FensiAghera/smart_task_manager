from storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks, 1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. [{status}] {task['title']}")

    def add_task(self, title):
        self.tasks.append({"title": title, "completed": False})
        save_tasks(self.tasks)
        print("Task added successfully!")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            save_tasks(self.tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            deleted = self.tasks.pop(index - 1)
            save_tasks(self.tasks)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
