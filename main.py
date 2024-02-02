import requests
from datetime import datetime
import os

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPH_ID = os.environ["GRAPH_ID"]


# Username creation via POST
# Token is chosen by user when first creating account - add token to environmental variables
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Graph creation via POST
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Change "name" to the name you would like the graph to be
# Change "color" to one of the following:
# shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro(black)
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Time Graph",
    "unit": "minute",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixel addition to graph via POST
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

# When I forget to add a time for a previous date I can comment out the current "date"
# and use the hardcoded date I am looking to POST to pixela
# Feel free to customize the input("quantity") message to further remember what you are tracking
pixel_config = {
    # "date": "20231229",
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?(floating number): "),
}

response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
print(response.text)

# Updating a pixel via PUT
date_to_change = "20230907"
pixel_put_endpoint = f"{pixel_post_endpoint}/{date_to_change}"

# "quantity" is the value adjusted when calling the PUT
pixel_put_config = {
    "quantity": "85",
}

# response = requests.put(url=pixel_put_endpoint, json=pixel_put_config, headers=headers)
# print(response.text)

# Updating graph units via PUT

graph_put_config = {
    "unit": "minutes",
}

# response = requests.put(url=pixel_post_endpoint, json=graph_put_config, headers=headers)
# print(response.text)

# Delete a pixel via DELETE
date_to_delete = "20230825"
pixel_delete_endpoint = f"{pixel_post_endpoint}/{date_to_delete}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
