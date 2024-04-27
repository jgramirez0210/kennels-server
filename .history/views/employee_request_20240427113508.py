import sqlite3
import json
from models import Employee
EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Jesse Ramirez"
    }
]

# Function to retrieve all employees
def get_all_employees():
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.name,
      e.address,
      e.location_id
    FROM employee e
    """)

    employees = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      employee = Employee(row['id'], 
                row['name'], 
                row['address'],
                row['location_id'])

      employees.append(employee.__dict__)

  return employees

def get_single_employee(id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.name,
      e.address,
      e.location_id
    FROM employee e
    WHERE e.id = ?
    """, ( id, ))

    data = db_cursor.fetchone()

    employee = Employee(data['id'], 
              data['name'], 
              data['address'],
              data['location_id'])

    return employee.__dict__
#CREATE EMPLOYEE
def create_employee(employee):
  # Check if EMPLOYEES is empty
  if EMPLOYEES:
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]
  else:
    # If EMPLOYEES is empty, start IDs from 1
    max_id = 0

  # Add 1 to whatever that number is
  new_id = max_id + 1

  # Add an `id` property to the employee dictionary
  employee["id"] = new_id

  # Add the employee dictionary to the list
  EMPLOYEES.append(employee)

  # Return the dictionary with `id` property added
  return employee
# DELETE EMPLOYEE
def delete_employee(id):
  # Initial -1 value for employee index, in case one isn't found
  employee_index = -1

  # Iterate the EMPLOYEES list, but use enumerate() so that you
  # can access the index value of each item
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      # Found the employee. Store the current index.
      employee_index = index

  # If the employee was found, use pop(int) to remove it from list
  if employee_index >= 0:
    EMPLOYEES.pop(employee_index)
    
# UPDATE EMPLOYEE
def update_employee(id, new_employee):
  # Iterate the EMPLOYEES list, but use enumerate() so that
  # you can access the index value of each item.
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      # Found the employee. Update the value.
      EMPLOYEES[index] = new_employee
      break
    
def get_employees_by_location(location_id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.name,
      e.address,
      e.location_id
    FROM employee e
    WHERE e.location_id = ?
    """, (location_id, ))

    employees = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
      employees.append(employee.__dict__)

  return employees
