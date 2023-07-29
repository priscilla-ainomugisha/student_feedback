import requests
from pprint import pprint

form_id = "nuZNe3g5"
token = "tfp_ZCpXR3kyiC3UNxtWkVx8f4NNjMsrXDo893ySs25Tx4S_3peHSKMXjB9XV4"
headers = {"authorization": f"bearer {token}"}
response = requests.get(
    f"https://api.typeform.com/forms/{form_id}/responses", headers=headers
)

pprint(response.json())
