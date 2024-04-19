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