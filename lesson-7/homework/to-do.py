import csv
import json


class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data):
        return Task(**data)


class FileHandler:
    def __init__(self, file_name, format_type):
        self.file_name = file_name
        self.format_type = format_type

    def save(self, tasks):
        with open(self.file_name, 'w', newline='') as file:
            if self.format_type == "csv":
                writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
                writer.writeheader()
                writer.writerows([task.to_dict() for task in tasks])
            elif self.format_type == "json":
                json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self):
        try:
            with open(self.file_name, 'r') as file:
                if self.format_type == "csv":
                    return [Task.from_dict(row) for row in csv.DictReader(file)]
                elif self.format_type == "json":
                    return [Task.from_dict(task) for task in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


class ToDoManager:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.tasks = self.file_handler.load()

   