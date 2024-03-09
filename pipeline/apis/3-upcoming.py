#!/usr/bin/env python3

"""
This script retrieves information about the upcoming SpaceX launch
and prints details including launch name, date, rocket name, and launchpad.
"""

import requests

def upcomingLaunch():
    """
    Retrieves information about the upcoming SpaceX launch
    and prints details including launch name, date, rocket name, and launchpad.
    """
    # API endpoint for upcoming launches
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    
    # Send a GET request to the SpaceX API
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()

    # Sort launches by date
    sorted_launches = sorted(data, key=lambda x: x['date_local'])

    # Get details of the soonest upcoming launch
    upcoming_launch = sorted_launches[0]

    # Retrieve rocket and launchpad details
    rocket_response = requests.get(upcoming_launch['rocket'])
    launchpad_response = requests.get(upcoming_launch['launchpad'])
    rocket_data = rocket_response.json()
    launchpad_data = launchpad_response.json()

    # Extract relevant information
    launch_name = upcoming_launch['name']
    launch_date = upcoming_launch['date_local']
    rocket_name = rocket_data['name']
    launchpad_name = launchpad_data['name']
    launchpad_locality = launchpad_data['locality']

    # Print the details of the upcoming launch
    print("{} ({}) {} - {} ({})".format(
        launch_name,
        launch_date,
        rocket_name,
        launchpad_name,
        launchpad_locality
    ))

if __name__ == "__main__":
    upcomingLaunch()
