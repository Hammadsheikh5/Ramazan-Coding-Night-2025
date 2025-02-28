import click
import json
import os

TODO_FILE = 'todo.json'

def load_task():
    if not os.path.exists(TODO_FILE):  
        return []
    with open(TODO_FILE, 'r') as file:  
        return json.load(file)

def save_task(tasks):
    with open(TODO_FILE , 'w') as file:
        json.dump(tasks , file , indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument('task', type=str)
def add(task):
    """Add a new task to the list"""
    tasks = load_task()
    tasks.append({"task": task, "done": False})  # FIXED: Corrected key
    save_task(tasks)
    click.echo(f'Task Added : {task}')

@click.command()
def list():
    """List all tasks"""
    tasks = load_task()
    if not tasks:
        click.echo("No task added yet")
        return
    for i, task in enumerate(tasks, 1):
        status = '✅' if task["done"] else '❌'
        click.echo(f"{i}. {task['task']} [{status}]")  # FIXED: Corrected key

@click.command()
@click.argument('task_number', type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_task(tasks)
        click.echo(f"Task {task_number} completed")
    else:
        click.echo("Invalid Task Number")

@click.command()
@click.argument('task_number', type=int)
def remove(task_number):
    """Remove a task"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        remove_task = tasks.pop(task_number - 1)
        save_task(tasks)
        click.echo(f"Task {task_number} removed: {remove_task['task']}")
    else: 
        click.echo("Invalid Task Number")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == '__main__':
    cli()
