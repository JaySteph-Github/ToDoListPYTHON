tasks = []

def display_tasks(tasks):
  if not tasks:
    print("There are no tasks in the list.")
    return
  print("Your To-Do List:")
  for i, task in enumerate(tasks):
    completed_str = "Completed" if task["completed"] else "Pending"
    print(f"{i+1}. {task['title']} ({completed_str})")

def add_task(tasks):
  title = input("Enter task title: ")
  tasks.append({"title": title, "completed": False})
  print(f"Task '{title}' added successfully!")

def remove_task(tasks):
  display_tasks(tasks)
  if not tasks:
    return
  while True:
    try:
      task_number = int(input("Enter task number to remove (or 0 to cancel): "))
      if task_number <= 0 or task_number > len(tasks):
        raise ValueError
      del tasks[task_number - 1]
      print("Task removed successfully!")
      break
    except ValueError:
      print("Invalid input. Please enter a valid task number.")

def mark_complete(tasks):
  display_tasks(tasks)
  if not tasks:
    return
  while True:
    try:
      task_number = int(input("Enter task number to mark complete (or 0 to cancel): "))
      if task_number <= 0 or task_number > len(tasks):
        raise ValueError
      tasks[task_number - 1]["completed"] = True
      print("Task marked as completed!")
      break
    except ValueError:
      print("Invalid input. Please enter a valid task number.")

def main():
  print("\nWelcome to your To-Do List!")

  while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task Complete")
    print("5. Exit")
    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
      add_task(tasks)
    elif choice == '2':
      remove_task(tasks)
    elif choice == '3':
      display_tasks(tasks)
    elif choice == '4':
      mark_complete(tasks)
    elif choice == '5':
      print("Exiting To-Do List...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()