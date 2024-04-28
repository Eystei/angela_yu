import requests
from datetime import datetime

USERNAME = "yury"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "87s65gh7s786d5f8s48ds7fgsdfh4"
GRAPH_ID = "graph1"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# CREATE USER ON PIXELA

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# CREATE GRAPH ON PIXELA

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


# response_graph_post = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
# print(response_graph_post.text)

# MARK PIXEL ON PIXEL_GRAPH

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
prev_data = datetime(year=2023, month=8, day=26)

pixel_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many kilometres did you cycle today? ")
}

response_pixel_post = requests.post(url=PIXEL_ENDPOINT, json=pixel_data, headers=HEADERS)
print(response_pixel_post.text)

# EDIT EXISTING DATA VIA PUT METHOD

DATA_WILL_BE_UPDATE = "20230927"
PIXEL_ENDPOINT_PUT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{prev_data.strftime('%Y%m%d')}"

pixel_data_put = {
    "quantity": "4.44"
}

# response_pixel_put = requests.put(url=PIXEL_ENDPOINT_PUT, json=pixel_data_put, headers=HEADERS)
# print(response_pixel_put.text)

# DELETE EXISTING PIXEL

PIXEL_ENDPOINT_DELETE = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{prev_data.strftime('%Y%m%d')}"

# response_pixel_deleted = requests.delete(url=PIXEL_ENDPOINT_DELETE, headers=HEADERS)
# print(response_pixel_deleted)
