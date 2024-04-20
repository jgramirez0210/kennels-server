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

#CREATE CUSTOMER
def create_customer(customer):
  # Check if CUSTOMERS is empty
  if CUSTOMERS:
    # Get the id value of the last employee in the list
    max_id = CUSTOMERS[-1]["id"]
  else:
    # If CUSTOMERS is empty, start IDs from 1
    max_id = 0

  # Add 1 to whatever that number is
  new_id = max_id + 1

  # Add an `id` property to the employee dictionary
  customer["id"] = new_id

  # Add the employee dictionary to the list
  CUSTOMERS.append(customer)

  # Return the dictionary with `id` property added
  return customer
#DELETE CUSTOMER
def delete_customer(id):
    # Initial -1 value for location index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the location. Store the current index.
            customer_index = index

    # If the location was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
