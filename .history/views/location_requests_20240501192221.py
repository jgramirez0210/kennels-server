import sqlite3
import json
from models import Location, Employee, Animal
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
        l.address
    FROM Location l
    WHERE l.id = ?
    """, (id, ))
    data = db_cursor.fetchone()
    location = Location(data['id'], data['name'], data['address'])
    # Execute the query to get the employees associated with the location
    db_cursor.execute("""
    SELECT
        e.id,
        e.name
    FROM Employee e
    WHERE e.location_id = ?
    """, (id, ))
    employees_data = db_cursor.fetchall()
    # Add each employee to the employees list of the location
    for row in employees_data:
        employee = Employee(row['id'], row['name'])
        location.employees.append(employee.__dict__)
    # Execute the query to get the animals associated with the location
    db_cursor.execute("""
    SELECT
        a.id,
        a.name,
        a.breed,
        a.status
    FROM Animal a
    WHERE a.location_id = ?
    """, (id, ))
    animals_data = db_cursor.fetchall()
    # Add each animal to the animals list of the location
    for row in animals_data:
        animal = Animal(row['id'], row['name'], row['breed'], row['status'])
        location.animals.append(animal.__dict__)
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
