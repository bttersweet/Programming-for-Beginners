import requests

url = "https://www.boredapi.com/api/activity"

# Get response from the API.
response = requests.get(url)

# Print the response text to console
print(response.text)