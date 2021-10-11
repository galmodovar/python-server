CUSTOMERS = [
     {
      "id": 1,
      "name": "Emma Beaton",
      "email": "emma@beaton.com",
      "employee": False
    },
    {
      "id": 2,
      "name": "Dani Adkins",
      "email": "dani.adkins.com",
      "employee": False
    },
    {
      "id": 3,
      "name": "Adam Oswalt",
      "email": "adam@oswalt.com",
      "employee": False
    },
    {
      "id": 4,
      "name": "Fletcher Bangs",
      "email": "flangs@bangs.com",
      "employee": False
    }
]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer