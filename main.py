import requests
from datetime import datetime


TOKEN= "s65dg4s654g6sdbs658dgf"
USERNAME= "mertneo"
GRAPH_ID = "graph1"  # Replace with your graph ID

# ---------------------------- CREATING PIXELA ACCOUNT WITH POST() ------------------------------- #

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment the lines below to create a Pixela account
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# ---------------------------- CREATING PIXELA GRAPH WITH POST() ------------------------------- #

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",  # You can change color (shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple), and kuro (black) are supported as color kinds.)
}

headers = {
    "X-USER-TOKEN": TOKEN  # We hide the API key with this method; Pixela documentation contains information
}

# Uncomment the lines below to create a Pixela graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ---------------------------- CREATING PIXEL IN PIXELA GRAPH WITH POST() ------------------------------- #

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)

# ---------------------------- UPDATING PIXEL IN PIXELA GRAPH WITH PUT() ------------------------------- #

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5",  # example
}

# Uncomment the lines below to update a pixel square with put() method
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# ---------------------------- DELETING PIXEL DATA IN PIXELA GRAPH WITH DELETE() ------------------------------- #

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Uncomment the lines below to delete data with delete method; Pixela has documentation about it
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
