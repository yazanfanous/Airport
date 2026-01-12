"""
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Yazan Fanous
Student ID: 251446630
File created: December 1, 2024
******************************
This is the main program file, loading the data from files.
creates the Airport and Flight objects, with all functions
needed to analyze flights and get answers about travel.
"""

# Import the flight and airport classes
from Flight import *
from Airport import *

# Store airports and flights
all_airports = []
all_flights = {}

# Load data from airport and flight files
def load_data(airport_file, flight_file):
    # Try loading both airport and flight data
    try:
        # Read the airport file and create Airport objects
        with open(airport_file, 'r') as airport_data:
            for line in airport_data:
                parts = line.split('-')
                code = parts[0].strip()
                city = parts[2].strip()
                country = parts[1].strip()
                all_airports.append(Airport(code, city, country))

        # Read the flight file and create Flight objects
        with open(flight_file, 'r') as flight_data:
            for line in flight_data:
                parts = line.strip().split('-')
                flight_number = f"{parts[0].strip()}-{parts[1].strip()}"
                origin_code = parts[2].strip()
                destination_code = parts[3].strip()
                duration = parts[4].strip()

                # Find origin and destination airports
                origin_airport = next((a for a in all_airports if a.get_code() == origin_code), None)
                destination_airport = next((a for a in all_airports if a.get_code() == destination_code), None)

                if origin_airport and destination_airport:
                    flight = Flight(flight_number, origin_airport, destination_airport, duration)
                    if origin_code not in all_flights:
                        all_flights[origin_code] = []
                    all_flights[origin_code].append(flight)
        return True
    except Exception:
        return False

# Get an airport object by its code
def get_airport_by_code(code):
    for airport in all_airports:
        if airport.get_code().strip() == code.strip():
            return airport
    raise ValueError(f"No airport with the given code: {code}")

# Find all flights for a given city
def find_all_city_flights(city):
    flights = []
    for flight_list in all_flights.values():
        for flight in flight_list:
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                flights.append(flight)
    return flights

# Find all flights for a given country
def find_all_country_flights(country):
    flights = []
    for flight_list in all_flights.values():
        for flight in flight_list:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                flights.append(flight)
    return flights

# Find direct or connecting flights between two airports
def find_flight_between(orig_airport, dest_airport):
    orig_code = orig_airport.get_code()
    if orig_code in all_flights:
        for flight in all_flights[orig_code]:
            if flight.get_destination() == dest_airport:
                return f"Direct Flight: {orig_code} to {dest_airport.get_code()}"

    connecting_airports = set()
    if orig_code in all_flights:
        for first_flight in all_flights[orig_code]:
            connecting_code = first_flight.get_destination().get_code()
            if connecting_code in all_flights:
                for second_flight in all_flights[connecting_code]:
                    if second_flight.get_destination() == dest_airport:
                        connecting_airports.add(connecting_code)

    if connecting_airports:
        return connecting_airports
    raise ValueError(f"There are no direct or single-hop connecting flights from {orig_code} to {dest_airport.get_code()}")

# Find the shortest flight from an airport
def shortest_flight_from(orig_airport):
    orig_code = orig_airport.get_code()
    if orig_code not in all_flights or not all_flights[orig_code]:
        return None
    return min(all_flights[orig_code], key=lambda x: float(x.get_duration()))

# Find the return flight for a given flight
def find_return_flight(first_flight):
    dest_code = first_flight.get_destination().get_code()
    if dest_code in all_flights:
        for flight in all_flights[dest_code]:
            if flight.get_destination() == first_flight.get_origin():
                return flight
    raise ValueError(f"There is no flight from {dest_code} to {first_flight.get_origin().get_code()}")

if __name__ == "__main__":
    pass
