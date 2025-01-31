import requests

response = requests.get("https://bored.api.lewagon.com/api/activity/")
if response.status_code == 200: 
    data = response.json()  
    print(f"Suggested activity: {data['activity']}")
else:
    print("Failed to fetch activity. Please try again later.")

