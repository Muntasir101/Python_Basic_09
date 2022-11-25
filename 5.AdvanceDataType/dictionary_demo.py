car_dictionary = {'make': 'bmw',
                  'model': '2000b',
                  'year': 2022,
                  'weight': 100.3}

print(car_dictionary['make'])
print(car_dictionary['model'])
year = car_dictionary['year']
print(year)

# Nested dictionary
user_details = {
    "username": "Mr.Superman",
    "password": "1234567",
    "address": "dhaka",
    "permanent_address": {
        "house": "123 New York"
    },
    "present_address": {
        "house": "123 California",
        "road": {
            "street_number": 123
        }
    }
}

print(user_details["present_address"]["road"]["street_number"])

print(user_details.keys())
print(user_details.values())
print(user_details.items())
print(user_details)

