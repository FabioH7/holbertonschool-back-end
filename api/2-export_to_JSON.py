#!/usr/bin/python3
""" Getting my first apis """
import json
import requests
import sys


if __name__ == "__main__":
    """Get api bob"""
    todos_api = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')
    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    todo_data = todos_api.text
    user_data = user_api.text
    user = json.loads(user_data)
    todos = json.loads(todo_data)
    all_todos = []
    for todo in todos:
        if todo['userId'] == user['id']:
            all_todos.append(
                {"task": todo['title'], "completed": todo['completed'],
                 "username": user['username']})
    user_tasks = {str(user['id']): all_todos}
    filename = "{}.json".format(user['id'])
    with open(filename, 'w') as file:
        json.dump(user_tasks, file)
