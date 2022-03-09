import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('PIYNdxjRzOR-hCaZUDigGA', 'jwzPiTnUXPVMaGx1mojqxSDvMicQGg')
post_data = {"grant_type": "password", "username": "The_G1ver", "password": "********"}
headers = {"User-Agent": "First App by u/The_G1ver"}

response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
response_json = response.json()


url = "https://www.reddit.com/r/PunPatrol/comments/so53d6/weve_got_some_sort_of_financial_crime_here/"

API_method = "/api/vote"
thing_id = url.split("/")[6]

headers = {"Authorization": response_json['token_type'] + " " + response_json["access_token"],
           "User-Agent": headers["User-Agent"]
}

data = {"id": "t3_" + thing_id,
        "dir": "1"
}

response = requests.post("https://oauth.reddit.com" + API_method, headers=headers, data=data)