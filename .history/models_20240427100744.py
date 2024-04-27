class Animal:
  def __init__(self, id, name, species, locationId, customerId, status):
    self.id = id
    self.name = name
    self.species = species
    self.locationId = locationId
    self.customerId = customerId
    self.status = status


class Customer:
  def __init__(self, id, name, address, email, password):
    self.id = id
    self.name = name
    self.address = address
    self.email = email
    self.password = password

class Employee:
  def __init__(self, id, name, address, location_id):
    self.id = id
    self.name = name
    self.address = address
    self.location_id = location_id
