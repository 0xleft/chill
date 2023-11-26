import requests
import json
import random
import threading
import os

def download_image(url, filename):
    response = requests.get(url)
    file = open(filename, "wb")
    file.write(response.content)
    file.close()

url = "https://api.openstreetcam.org/2.0/photo/?id="

def get_data(id):
    response = requests.get(url + str(id))
    data = response.json()
    return data

def get_coords(object):
    long = object['matchLng']
    lat = object['matchLat']
    return {
        'long': long,
        'lat': lat
    }

def get_image(object):
    return object['fileurlTh']

def get_info(object):
    coords = get_coords(object)
    image = get_image(object)
    return {
        'coords': coords,
        'image': image
    }

if __name__ == "__main__":
    while True:
        try:
            id = random.randint(400000, 1000000)
            data = get_data(id)
            try:
                data['result']['data']
            except:
                print(data)
                continue
            
            info = get_info(data['result']['data'][0])
            print(info)

            if info['coords']['lat'] == None or info['coords']['long'] == None:
                continue

            # check if image already exists
            if os.path.exists("data/" + str(id) + ".jpg"):
                continue

            threading.Thread(target=download_image, args=(info['image'], "data/" + str(id) + ".jpg")).start()
            # write lat and long to file too
            file = open("data/" + str(id) + ".txt", "w")
            file.write(str(info['coords']['lat']) + "\n")
            file.write(str(info['coords']['long']))
            file.close()
            print("Downloaded image " + str(id))
        except:
            print("Error downloading image " + str(id))
            continue