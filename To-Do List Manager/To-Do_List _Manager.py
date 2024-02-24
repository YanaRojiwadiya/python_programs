"""Assignment 2: To-Do List Manager

Create a Python script that implements a simple to-do list manager.
Allow users to add tasks, mark tasks as completed, and remove tasks.
Store the tasks in a list of dictionaries where each dictionary represents a task with keys like 'task_name', 'priority', 'completed', etc.
Provide a menu-driven interface for users to interact with the to-do list."""


def add_task(todo_list):
    task_name = input("enter task name: ")
    priority = int(input("enter priority: "))
    todo_list.append({'task_name': task_name, 'priority': priority, 'completed': False})
    print("task added")

def display_tasks(todo_list):
    print("To-Do List:")
    for i in range(len(todo_list)):
        task = todo_list[i]
        if task['completed']==True:
            status = "completed" 
        else:
            status = "not completed"
        print(f"{i}. {task['task_name']}, Priority:{task['priority']} [{status}]")
        
def mark_completed(todo_list):
    task_index = int(input("enter index number: "))
    if 0 <= task_index <= len(todo_list):
        todo_list[task_index]['completed'] = True
        print("marked as completed!")
    else:
        print("index is not valid")

def remove_task(todo_list):
    task_index = int(input("enter index number: "))
    if 0 <= task_index <= len(todo_list):
        todo_list.pop(task_index)
        print("task removed ")
    else:
        print("index is not valid")


def main():
    todo_list = []

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            display_tasks(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("exit")
            break
        else:
            print("choose number between 1 to 4")

if __name__ == "__main__":
    main()
