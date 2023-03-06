import requests

# This is an API to get activity ideas
activity_url = "https://www.boredapi.com/api/activity"

response = requests.get(activity_url)

print(response.text)