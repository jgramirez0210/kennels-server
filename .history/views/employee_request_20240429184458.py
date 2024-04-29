import sqlite3

# Function to retrieve all employees
def get_all_employees():
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.name
    FROM employee e
    """)

    employees = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      employee = {"id": row['id'], "name": row['name']}
      employees.append(employee)

  return employees

# Function to retrieve a single employee based on its ID
def get_single_employee(id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.name
    FROM employee e
    WHERE e.id = ?
    """, (id, ))

    data = db_cursor.fetchone()

    employee = {"id": data['id'], "name": data['name']}

  return employee

#CREATE EMPLOYEE
def create_employee(employee):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    INSERT INTO Employee
      ( name )
    VALUES
      ( ? );
    """, (employee['name'], ))

    employee['id'] = db_cursor.lastrowid

  return employee

# DELETE EMPLOYEE
def delete_employee(id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    DELETE FROM employee
    WHERE id = ?
    """, (id, ))

# UPDATE EMPLOYEE
def update_employee(id, new_employee):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    UPDATE Employee
    SET
      name = ?
    WHERE id = ?
    """, (new_employee['name'], id))

  return new_employee

def get_employees_by_location(location_id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      e.id,
      e.name
    FROM employee e
    WHERE e.location_id = ?
    """, (location_id, ))

    employees = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      employee = {"id": row['id'], "name": row['name']}
      employees.append(employee)

  return employees
