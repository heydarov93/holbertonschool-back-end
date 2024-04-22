#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

from sys import argv
from urllib import request
import json


employee_id = argv[1]

todos_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                             f'todos?userId={employee_id}')

user_json = request.urlopen('https://jsonplaceholder.typicode.com/' +
                            f'users/{employee_id}')

todos = json.loads(todos_json.read())
employee = json.loads(user_json.read())
employee_name = employee['name']

with open('USER_ID.csv', 'a') as afile:
    for task in todos:
        user_id = task['userId']
        status = task['completed']
        title = task['title']

        value_for_line = (
            f'\"{user_id}\",'
            f'\"{employee_name}\",'
            f'\"{status}\",'
            f'\"{title}\"\n'
        )

        afile.write(value_for_line)
