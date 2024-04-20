CUSTOMERS = [
    {
        "id": 1,
        "name": "Bob Bobbert"
    },
    {
        "id": 2,
        "name": "Zane Zach"
    }


]
# Function to retrieve all locations
def get_all_customers():
  # Return the global LOCATIONS variable
  return CUSTOMERS

# Function to retrieve a single location based on its ID
def get_single_customer(id):
  # Initialize a variable to store the requested location
  request_customer = None

  # Iterate through the LOCATIONS list
  for customer in CUSTOMERS:
    # Check if the current location's ID matches the requested ID
    if customer["id"] == id:
      # If so, set the request_location variable to the current location
      request_customer = customer

  # Return the requested location
  return request_customer
