import json
import csv

def load_tasks(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("ID | Task Name | Completed | Priority")
    print("-" * 40)
    for task in tasks:
        print(f"{task['id']} | {task['task']} | {task['completed']} | {task['priority']}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")


