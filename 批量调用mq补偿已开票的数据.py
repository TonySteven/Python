import requests

import json

# Define the API URL
url = 'https://supply.umugua.net/api-v2/scm-purchase/sale-invoice-bill/send-invoice-status-mq'

# Define the headers for the request
headers = {
    'token': 'lmnchain0524cae7a66d47c6b0c968f81b4e1adc',  # Your token
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Host': 'supply.umugua.net',
    'Connection': 'keep-alive'
}

# List of varying externalNos
external_nos = [
    "9068056055157443971",
    "9068056055157443947",
    "9068056055157443986",
    "9068056055157443869",
    "9068056055157443961",
    "9068056055157444376",
    "9068056055157443884"
]

# Common data fields
common_data = {
    "orderNo": "1829758087792164864",
    "statusDesc": "已开票",
    "status": 2
}

# Loop through the externalNos and make POST requests
for external_no in external_nos:
    # Combine common data with unique externalNo
    data = common_data.copy()
    data['externalNo'] = external_no

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check response status and print the result
    if response.status_code == 200:
        print(f"Success for externalNo {external_no}: {response.json()}")
    else:
        print(f"Error for externalNo {external_no}: {response.status_code} - {response.text}")
