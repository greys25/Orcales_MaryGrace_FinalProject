from storage import load_data, save_data

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def to_dict(self):
        return {
            "title": self.title,
            "done": self.done
        }

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        data = load_data()
        self.tasks = [Task(t["title"], t["done"]) for t in data]

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        save_data(data)

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task.done else "✘"
            print(f"{i}. [{status}] {task.title}")

    def mark_done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].done = True
            self.save_tasks()
            print("Task marked as done!")
        else:
            print("Invalid number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Deleted: {removed.title}")
        else:
            print("Invalid number.")