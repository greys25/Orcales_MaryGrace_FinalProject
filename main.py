from todo import ToDoList

def menu():
    print("\n=== Grace's To-Do List ===")
    print("1. ➕  Add Tasks")
    print("2. 👀  View Tasks")
    print("3. ✔  Mark as Done")
    print("4. ❌ Delete Task")
    print("5. 💨  Exit")


def main():
    todo = ToDoList()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter your new task: ")
            todo.add_task(title)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            num = int(input("Task number to mark done: "))
            todo.mark_done(num)

        elif choice == "4":
            todo.view_tasks()
            num = int(input("Task number to delete: "))
            todo.delete_task(num)

        elif choice == "5":
            print("Byebye💙!")
            break

        else:
            print("Hindi right ang iyong na pick😂!")

if __name__ == "__main__":
    main()
