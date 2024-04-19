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
  # Return the global EMPLOYEES variable
  return EMPLOYEES

# Function to retrieve a single employee based on its ID
def get_single_employee(id):
  # Initialize a variable to store the requested employee
  request_employee = None

  # Iterate through the EMPLOYEES list
  for employee in EMPLOYEES:
    # Check if the current employee's ID matches the requested ID
    if employee["id"] == id:
      # If so, set the request_employee variable to the current employee
      request_employee = employee

  # Return the requested employee
  return request_employee
