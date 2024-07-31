#!/usr/bin/python3
"""
Fetches and displays to-do list information for a given employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])
    
    user_response = requests.get(f"{url}users/{employee_id}")
    user = user_response.json()
    
    todos_response = requests.get(f"{url}todos", params={"userId": employee_id})
    todos = todos_response.json()
    
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)
    
    print(f"Employee {user.get('name')} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
