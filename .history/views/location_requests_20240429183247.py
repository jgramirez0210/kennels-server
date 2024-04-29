import sqlite3
import json
from models import Location
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

    db_cursor.execute("""
    SELECT
      l.id,
      l.name,
      l.address
    FROM location l
    WHERE l.id = ?
    """, ( id, ))

    data = db_cursor.fetchone()

    location = Location(data['id'], 
              data['name'], 
              data['address'])

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
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))
#UPDATE LOCATION
def update_location(id, new_location):
  # Iterate the LOCATIONS list, but use enumerate() so that
  # you can access the index value of each item.
  for index, location in enumerate(LOCATIONS):
    if location["id"] == id:
      # Found the location. Update the value.
      LOCATIONS[index] = new_location
      break
