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
  # Return the global LOCATIONS variable
  return LOCATIONS

# Function to retrieve a single location based on its ID
def get_single_location(id):
  # Initialize a variable to store the requested location
  request_location = None

  # Iterate through the LOCATIONS list
  for location in LOCATIONS:
    # Check if the current location's ID matches the requested ID
    if location["id"] == id:
      # If so, set the request_location variable to the current location
      request_location = location

  # Return the requested location
  return request_location

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
        
#UPDATE LOCATION
def update_location(id, new_location):
  # Iterate the LOCATIONS list, but use enumerate() so that
  # you can access the index value of each item.
  for index, location in enumerate(LOCATIONS):
    if location["id"] == id:
      # Found the location. Update the value.
      LOCATIONS[index] = new_location
      break
