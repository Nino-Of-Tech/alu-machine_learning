#!/usr/bin/env python3

"""
This module contains a function that
uses the unofficial SpaceX API to display
the number of launches per rocket.
"""

import requests

def get_all_launches():
    """
    Retrieve all launches from the SpaceX API.
    """
    url = "https://api.spacexdata.com/v4/launches"
    all_launches = []

    # Retrieve all launches by handling pagination
    while url:
        response = requests.get(url)
        data = response.json()
        all_launches.extend(data)
        url = response.links.get('next', {}).get('url')

    return all_launches

def launches_per_rocket():
    """
    Print the number of launches per rocket.
    """
    all_launches = get_all_launches()
    rockets = {}

    for launch in all_launches:
        rocket_id = launch['rocket']
        rocket_name = launch['rocket']['name']
        if rocket_name in rockets:
            rockets[rocket_name] += 1
        else:
            rockets[rocket_name] = 1

    # Sort and print the results
    for rocket, count in sorted(rockets.items(), key=lambda x: (-x[1], x[0])):
        print(f"{rocket}: {count}")

if __name__ == "__main__":
    launches_per_rocket()
