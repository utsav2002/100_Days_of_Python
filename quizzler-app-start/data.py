import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

questions = (requests.get(url="https://opentdb.com/api.php", params=parameters)).json()

question_data = questions["results"]