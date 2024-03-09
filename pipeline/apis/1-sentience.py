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

        print("Received data:", data)  # Print received data for debugging

        for result in data.get('results', []):
            if result.get('designation') == "sentient":
                species.append((result.get('name'), result.get('homeworld')))

        url = data.get('next')

        # Introduce a delay to avoid hitting API rate limits
        time.sleep(0.5)

    planets = []
    for species_name, homeworld_url in species:
        response = requests.get(homeworld_url)
        homeworld_data = response.json()
        planets.append(homeworld_data.get('name'))

        # Introduce a delay to avoid hitting API rate limits
        time.sleep(0.5)

    return planets
