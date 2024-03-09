#!/usr/bin/env python3

import requests
import datetime

def upcoming_launch():
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    launches = response.json()

    # Sort launches by date_unix
    launches.sort(key=lambda x: x['date_unix'])

    # Get the soonest upcoming launch
    upcoming_launch = launches[0]

    # Extract launch details
    launch_name = upcoming_launch['name']
    launch_date = datetime.datetime.fromisoformat(upcoming_launch['date_local']).strftime('%Y-%m-%d %H:%M:%S')
    rocket_name = upcoming_launch['rocket']
    launchpad = upcoming_launch['launchpad']

    # Get launchpad details
    launchpad_name = launchpad['name']
    launchpad_locality = launchpad['locality']

    # Format and print the information
    print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

if __name__ == '__main__':
    upcoming_launch()
