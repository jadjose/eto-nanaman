import requests
import csv

r = requests.get('https://api.spacexdata.com/v3/launches')


re = r.json()


def data(re):
    mission_name = []
    mission_image = []
    mission_id = []

    for m in re:
        mission_name.append(m['mission_name'])
        mission_image.append(m['links']['mission_patch'])
        mission_id.append(m['flight_number'])
    
    
    with open('etl process.csv', 'w', newline='') as file:
        for a, b, c in zip(mission_id, mission_name, mission_image):
            writer = csv.writer(file)
            writer.writerow([a, b, c])
    
    print(len(mission_id))
    print(len(mission_name))
    print(len(mission_image))


data(re)



