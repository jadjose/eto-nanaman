import requests

def get_launch_data(url):
    launch_data = requests.get(url)
    return launch_data.json()


def transform_data(launch_data):
    for launch in launch_data:
        print(launch['mission_name'])


        
        



result = get_launch_data('https://api.spacexdata.com/v3/launches')

transform_data(result)