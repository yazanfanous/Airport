"""
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Yazan Fanous
Student ID: 251446630
File created: December  1, 2024
******************************
This file contains the Flight class, which is used to represent flights.
including details like flight number, origin, destination, and duration.
It includes methods that can determine if a flight is domestic, combine flights,
retrieve information about a flight.
"""

# Import airport class
from Airport import *


class Flight:
    # Initialize a Flight object with flight number, origin, destination, and duration
    def __init__(self, flight_no, origin, dest, dur):
        if not isinstance(origin, Airport) or not isinstance(dest, Airport):
            raise TypeError("The origin and destination must be Airport objects")

        # Ensure the duration is a valid float value
        try:
            self._duration = float(dur)
        except ValueError:
            raise ValueError(f"Invalid duration value: {dur}. Duration must be numeric.")

        self._flight_no = flight_no
        self._origin = origin
        self._destination = dest

    # Return a string representation of the Flight object
    def __str__(self):
        try:
            duration = float(self._duration)  # Convert duration to float for rounding
        except ValueError:
            duration = 0

        domestic_status = "domestic" if self.is_domestic() else "international"
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({round(duration)}h) [{domestic_status}]"

    # Check if two Flight objects are equal based on origin and destination
    def __eq__(self, other):
        if not isinstance(other, Flight):
            return False
        return self._origin == other._origin and self._destination == other._destination

    # Combine two flights if they are connectable
    def __add__(self, conn_flight):
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        if self._destination != conn_flight.get_origin():
            raise ValueError("These flights cannot be combined")

        combined_duration = self._duration + conn_flight.get_duration()
        return Flight(self._flight_no, self._origin, conn_flight.get_destination(), combined_duration)

    # Get the flight number
    def get_flight_no(self):
        return self._flight_no

    # Get the origin airport
    def get_origin(self):
        return self._origin

    # Get the destination airport
    def get_destination(self):
        return self._destination

    # Get the flight duration
    def get_duration(self):
        return self._duration

    # Check if the flight is domestic
    def is_domestic(self):
        return self._origin.get_country() == self._destination.get_country()

    # Set the origin airport
    def set_origin(self, origin):
        self._origin = origin

    # Set the destination airport
    def set_destination(self, destination):
        self._destination = destination
