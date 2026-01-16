import json

todo_list = []

def save_todos():
    """Save todo list to JSON file"""
    with open("todos.json", "w") as file:
        json.dump(todo_list,file, indent=2)

def load_todos():
    """Load todo list from JSON file"""
    global todo_list
    try:
        with open("todos.json","r") as file:
            todo_list = json.load(file)
            print(" Loaded todos from file!")
    except FileNotFoundError:
        print("No saved todos found. Starting fresh!")
        todo_list = []
    except json.JSONDecodeError:
        print("File corrupted. Startinf fresh!")
        todo_list = []

def add_todo():
    task =  input('Enter task: ')
    priority = input('Enter priority(high, medium, low): ').lower()
    task_list = {"task":task, "priority":priority}
    todo_list.append(task_list)
    print(f"\nAdded {task} as {priority} priority task.")

   

def show_all_todos():
    print('\n--- Todo List ---')
    if len(todo_list) == 0:
        print("No tasks to show.")
        return    
    for i, task_list in enumerate(todo_list,1):
        print(f"\n{i}. [{task_list['priority'].upper()}] {task_list['task']}")

def show_by_priority():
    required_priority = input("Enter priority (high/medium/low): ").lower()

    print(f"\n--- {required_priority.upper()} Priority Todos ---")

    found=0     
    
    for i, task_list in enumerate(todo_list,1):
        if task_list['priority'] == required_priority:
            print(f'\n{i}. [{task_list['priority']}] {task_list['task']}')
            found += 1

    if found == 0:
        print(f"No {required_priority} priority tasks found.")

def complete_todo():
    if len(todo_list) == 0:
        print("No tasks to complete!")
        return

    show_all_todos()

    try:

       task_completed = int(input("Enter the completed task number: "))
     
       if task_completed < 1 or task_completed > len(todo_list):
         print("Invalid task number.")
         return

       remove = task_completed - 1  
       completed_task = todo_list[remove]
       todo_list.pop(remove)
       print(f"Completed task: {completed_task["task"]}")
    
    except ValueError:
        print("Please enter a valid number.")


load_todos()

while True:
    print("\n--- Todo List Manager ---")
    print("1. Add Todo")
    print("2. Show All Todos")
    print("3. Show by priority")
    print("4. Complete Todo")
    print("5. Exit")

    choice = input("\n Choose (1-5): ")

    if choice == '1':
        add_todo()
        save_todos()
    elif choice == '2':
        show_all_todos()
    elif choice == '3':
        show_by_priority()
    elif choice == '4':
        complete_todo()
        save_todos()
    elif choice == '5':
        save_todos()
        print("Todos saved! Goodbye!")
        break 

    else:
        print("Invalid choice!")                   



