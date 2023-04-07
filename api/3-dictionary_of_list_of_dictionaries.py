#!/usr/bin/python3
""" Getting my first apis """
import json
import requests


def get_user_todos(id):
    """Get api bob"""
    todos_api = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')
    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    todo_data = todos_api.text
    user_data = user_api.text
    user = json.loads(user_data)
    todos = json.loads(todo_data)
    all_todos = []
    for todo in todos:
        if todo['userId'] == user['id']:
            all_todos.append(
                {"username": user['username'], "task": todo['title'],
                 "completed": todo['completed']})
    return all_todos


if __name__ == '__main__':
    user_apis = requests.get(
        'https://jsonplaceholder.typicode.com/users/')
    users_data = user_apis.text
    users = json.loads(users_data)
    final_dict = {}
    for user in users:
        final_dict[user['id']] = get_user_todos(str(user['id']))
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(final_dict, file)
