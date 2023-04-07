import csv
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
                (user['id'], user['username'], todo['completed'], todo['title']))
    filename = "{}.csv".format(user['id'])
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in all_todos:
            spamwriter.writerow(todo)
