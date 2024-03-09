#!/usr/bin/env python3

"""
This module contains a function that
uses Star Wars API to get the list of names of
all sentinent species in the Star Wars universe"""

import requests
import time


def sentientPlanets():
    """Return list of names of home planets of all sentient species"""
    url = "https://swapi-api.alx-tools.com/api/species/"
    species = []

    while url:
        response = requests.get(url)
        data = response.json()

        for result in data['results']:
            if result['designation'] == "sentient":
                species.append((result['name'], result['homeworld']))

        url = data['next']

        # Introduce a delay to avoid hitting API rate limits
        time.sleep(0.5)  # You may adjust the delay as needed

    planets = []
    for species_name, homeworld_url in species:
        response = requests.get(homeworld_url)
        homeworld_data = response.json()
        planets.append(homeworld_data['name'])

        # Introduce a delay to avoid hitting API rate limits
        time.sleep(0.5)  # You may adjust the delay as needed

    return planets
