import requests

TOKEN = 'your_turso_auth_token_here'
URL = 'https://your-database-name.turso.io/v2/pipeline'
headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Content-Type': 'application/json'
}

while True:
    command = input("sql: >")
    payload = {
        "requests": [
            {"type": "execute", "stmt": {"sql": command}},
            {"type": "close"}
        ]
    }
    response = requests.post(URL, json=payload, headers=headers)
    print(response.json())