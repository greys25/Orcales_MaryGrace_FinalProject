from storage import load_data, save_data
from colorama import Fore, Style, init

init(autoreset=True)

def add_task(title):
    tasks = load_data()
    tasks.append({"title": title, "done": False})
    save_data(tasks)
    print(Fore.GREEN + f"✔ Added: {title}")

def list_tasks():
    tasks = load_data()
    if not tasks:
        print(Fore.YELLOW + "No tasks yet.")
        return

    for i, task in enumerate(tasks, 1):
        if task["done"]:
            print(Fore.GREEN + f"{i}. [✓] {task['title']}")
        else:
            print(Fore.RED + f"{i}. [ ] {task['title']}")

def remove_task(index):
    tasks = load_data()
    try:
        removed = tasks.pop(index - 1)
        save_data(tasks)
        print(Fore.RED + f"✘ Removed: {removed['title']}")
    except IndexError:
        print("Invalid task number.")

def mark_done(index):
    tasks = load_data()
    try:
        tasks[index - 1]["done"] = True
        save_data(tasks)
        print(Fore.GREEN + "✔ Task completed")
    except IndexError:
        print("Invalid task number.")