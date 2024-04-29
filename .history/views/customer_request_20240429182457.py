import sqlite3
import json
from models import Customer
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
def get_all_customers():
  # Open a connection to the database
  with sqlite3.connect("./kennel.sqlite3") as conn:

    # Just use these. It's a Black Box.
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    # Write the SQL query to get the information you want
    db_cursor.execute("""
    SELECT
      a.id,
      a.name,
      a.address,
      a.email,
      a.password
    FROM customer a
    """)

    # Initialize an empty list to hold all animal representations
    customers = []

    # Convert rows of data into a Python list
    dataset = db_cursor.fetchall()

    # Iterate list of data returned from database
    for row in dataset:

      # Create an animal instance from the current row.
      # Note that the database fields are specified in
      # exact order of the parameters defined in the
      # Animal class above.
      customer = Customer(row['id'], 
                row['name'], 
                row['address'],
                row['email'], 
                row['password'])

      customers.append(customer.__dict__)

  return customers


# Function to retrieve a single location based on its ID
def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'], 
                          data['name'], 
                          data['address'],
                          data['email'], data['password'])

        return customer.__dict__
  # Iterate through the LOCATIONS list
  # for customer in CUSTOMERS:
  #   # Check if the current location's ID matches the requested ID
  #   if customer["id"] == id:
  #     # If so, set the request_location variable to the current location
  #     request_customer = customer

  # # Return the requested location
  # return request_customer

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
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))

# UPDATE CUSTOMER
def update_customer(id, new_customer):
  # Iterate the CUSTOMERS list, but use enumerate() so that
  # you can access the index value of each item.
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      # Found the customer. Update the value.
      CUSTOMERS[index] = new_customer
      break
    
def get_customer_by_email(email):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
      c.id,
      c.name,
      c.address,
      c.email,
      c.password
    FROM Customer c
    WHERE c.email = ?
    """, (email, ))

    customers = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])
      customers.append(customer.__dict__)

  return customers
