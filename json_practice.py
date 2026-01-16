import json

#Your data
my_list = ["apple", "banana", "cherry"]

#Save to JSON file
with open("fruits.json","w") as file:
    json.dump(my_list, file)

print("List saved to fruits.json!")

import json

#Load from JSON file
with open("fruits.json", "r") as file:
    loaded_list = json.load(file)

print("Loaded from file: ")
print(loaded_list)
print(type(loaded_list)) #It's a list!   

import json

todos = [
    {"task": "Buy groceries", "priority": "high"},
    {"task": "Call mom", "priority": "medium"},
    {"task": "Read book", "priority": "low"}
]

#Save to JSON
with open("todos.json","w") as file:
    json.dump(todos,file,indent=2) #indent=2 makes  it readable

print("Todos saved!")

#Load from JSON
with open ("todos.json", "r") as file:
    loaded_todos = json.load(file)

print("\nLoaded todos:")
for todo in loaded_todos:
    print(f"- {todo['task']} ({todo['priority']})")

import json

try:
    with open("todos.json", "r") as file:
        todos = json.load(file)
    print("Loaded todos from file!")
except FileNotFoundError:
    print("No saved file found. Starting with empty list.")
    todos = []

print(f"Total todos: {len(todos)}")


import json

names = [
    input("First Name: "),
    input("Second Name: "),
    input("Third Name: ")
]

with open("names.json", "w") as file:
    json.dump(names,file, indent=2)

print("Names saved!")

with open("names.json", "r") as file:
    loaded_names = json.load(file)
print("\nLoaded_names: ")

for name in loaded_names:
    print(f"- Name:{name}")

