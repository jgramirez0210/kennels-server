import sqlite3
import json
from models import Location, employee, Animal, Customer, Employee
LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]
# Function to retrieve all locations
def get_all_locations():
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      l.id,
      l.name,
      l.address
    FROM location l
    """)

    locations = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      location = Location(row['id'], 
                row['name'], 
                row['address'])

      locations.append(location.__dict__)
      
  return locations

def get_single_location(id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    # Execute the query to get the location details
    db_cursor.execute("""
    SELECT
      l.id,
      l.name,
      l.address,
      e.id as employee_id,
      e.name as employee_name,
      e.address as employee_address,
      a.id as animal_id,
      a.name as animal_name,
      a.breed as animal_breed,
      a.status as animal_status,
      a.customer_id as animal_customer_id
    FROM Location l
    LEFT JOIN Employee e
      ON e.location_id = l.id
    LEFT JOIN Animal a
      ON a.location_id = l.id
    WHERE l.id = ?
    """, (id, ))

    employees = []
    animals = []
    location = None
    dataset = db_cursor.fetchall()

    for row in dataset:
      if location is None:
        location = Location(row['id'], row['name'], row['address'])

      employee = Employee(row['employee_id'], row['employee_name'], row['employee_address'])
      employees.append(employee.__dict__)

      animal = Animal(row['animal_id'], row['animal_name'], row['animal_breed'], row['animal_status'], row['animal_customer_id'])
      animals.append(animal.__dict__)

    location.employees = employees
    location.animals = animals

    return location.__dict__
#CREATE LOCATION
def create_location(location):
  # Check if LOCATIONS is empty
  if LOCATIONS:
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]
  else:
    # If LOCATIONS is empty, start IDs from 1
    max_id = 0

  # Add 1 to whatever that number is
  new_id = max_id + 1

  # Add an `id` property to the location dictionary
  location["id"] = new_id

  # Add the location dictionary to the list
  LOCATIONS.append(location)

  # Return the dictionary with `id` property added
  return location

#DELETE LOCATION
def delete_location(id):
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)
        
# UPDATE LOCATION
def update_location(id, new_location):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
