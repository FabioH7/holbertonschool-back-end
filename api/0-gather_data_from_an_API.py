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
    completed = []
    all_todos = 0
    for todo in todos:
        if todo['userId'] == user['id']:
            if todo['completed']:
                completed.append(todo)
            all_todos += 1
    print(
        'Employee {} is done with tasks({}/{}):'
        .format(user['name'], len(completed), all_todos), file=sys.stdout)
    for finished_todo in completed:
        print('\t {}'.format(finished_todo['title']), file=sys.stdout)
