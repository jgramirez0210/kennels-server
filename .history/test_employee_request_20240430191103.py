import unittest
from views import update_animal, get_single_animal

class TestUpdateAnimal(unittest.TestCase):
  def test_update_animal(self):
    # Update the animal with id 1
    update_animal(1, {"name": "New Name"})

    # Retrieve the updated animal
    animal = get_animal_by_id(1)

    # Check that the animal's name was updated
    self.assertEqual(animal.name, "New Name")

if __name__ == '__main__':
  unittest.main()
