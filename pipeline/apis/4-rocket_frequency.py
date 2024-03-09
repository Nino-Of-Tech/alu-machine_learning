#!/usr/bin/env python3

"""
This module contains a function that
uses the unofficial SpaceX API to display
the number of launches per rocket.
"""

import requests

def launches_per_rocket():
    """Print the number of launches per rocket"""
    url = "https://api.spacexdata.com/v4/launches"
    rockets = {}

    # Retrieve all launches by handling pagination
    while url:
        response = requests.get(url)
        data = response.json()

        for launch in data:
            rocket_id = launch['rocket']
            rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
            rocket_response = requests.get(rocket_url)
            rocket_data = rocket_response.json()
            rocket_name = rocket_data['name']
            if rocket_name in rockets:
                rockets[rocket_name] += 1
            else:
                rockets[rocket_name] = 1

        # Check if there are more pages
        url = response.links.get('next', {}).get('url')

    # Sort and print the results
    for rocket in sorted(rockets.items(), key=lambda x: (-x[1], x[0])):
        print(f"{rocket[0]}: {rocket[1]}")

if __name__ == "__main__":
    launches_per_rocket()
