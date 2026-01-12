"""
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Yazan Fanous
Student ID: 251446630
File created: December  1, 2024
******************************
This file contains the Airport class, which is used to represent
airports by their code, city, and country. It has basic methods
to retrieve or update these values and to check whether two airports are the same.
"""

class Airport:
    # Initialize an Airport object with a code, city, and country
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    # Return a string representation of the Airport object
    def __str__(self):
        return f'{self._code} ({self._city}, {self._country})'

    # Compare two Airport objects based on their airport code
    def __eq__(self, other):
        if not isinstance(other, Airport):  # Ensure the other object is an Airport
            return False
        return self._code == other._code

    # Get the airport code
    def get_code(self):
        return self._code

    # Get the city of the airport
    def get_city(self):
        return self._city

    # Get the country of the airport
    def get_country(self):
        return self._country

    # Update the city of the airport
    def set_city(self, city):
        self._city = city

    # Update the country of the airport
    def set_country(self, country):
        self._country = country
