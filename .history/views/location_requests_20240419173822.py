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
    # Get the id value of the last animal in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location
