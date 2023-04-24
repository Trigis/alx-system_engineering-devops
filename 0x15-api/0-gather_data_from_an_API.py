#!/usr/bin/python3
"""
Python script that retrieves and displays the TODO list progress of a given employee
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(api_url)
    if response.status_code != 200:
        print("Error: Unable to retrieve TODO list for employee ID {}".format(employee_id))
        sys.exit(1)

    todo_list = response.json()
    total_tasks = len(todo_list)
    done_tasks = [task for task in todo_list if task['completed']]
    num_done_tasks = len(done_tasks)
    employee_name = todo_list[0]['name']

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {} {}".format('\t', task['title']))