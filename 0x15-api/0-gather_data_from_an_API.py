#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(f"{url}users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    user = user_response.json()

    # Fetch TODO list data
    todos_response = requests.get(f"{url}todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print("Todos not found")
        sys.exit(1)
    todos = todos_response.json()

    # Extract and count tasks
    employee_name = user.get('name')
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
