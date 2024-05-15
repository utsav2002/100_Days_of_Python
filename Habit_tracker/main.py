import requests
from datetime import datetime

USERNAME = "utsav2002"
TOKEN = "8ebtf768ft8eftew8"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# User created
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(graph_response.text)

date_of_work = datetime.now().strftime("%Y%m%d")

pixel_posting_endpoint = f"{graph_endpoint}/graph1"
pixel_posting_parameter = {
    "date": date_of_work,
    "quantity": input("How long did you code today?: ")
    # "optionalData": {
    #     "Description": "I completed until Day-35 today, hooray!"
    # }
}

pixel_posting_response = requests.post(url=pixel_posting_endpoint, json=pixel_posting_parameter, headers=headers)
print(pixel_posting_response.text)

update_pixel_endpoint = f"{pixel_posting_endpoint}/{date_of_work}"
update_pixel_parameter = {
    "quantity": "5"
}

# update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameter, headers=headers)
# print(update_pixel_response.text)

delete_pixel_endpoint = update_pixel_endpoint

# delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_response.text)
