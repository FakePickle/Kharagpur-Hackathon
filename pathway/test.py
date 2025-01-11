import requests

# Define the endpoint and payload
url = "http://127.0.0.1:8000/rag"
payload = {"query": "What is clustering?"}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
