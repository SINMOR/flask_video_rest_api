# Import the requests library to handle HTTP requests
import requests

# Define the base URL of the API
BASE = "http://127.0.0.1:5000/"

# Create a list of dictionaries, each representing a video with likes, name, views, and dislikes
data = [
    {"likes": 130, "name": "Tim", "views": 1044552, "dislikes": 235},
    {"likes": 16750, "name": "Morris ", "views": 134200, "dislikes": 25435},
    {"likes": 180, "name": "Sindet", "views": 1240, "dislikes": 9235},
    {"likes": 90, "name": "Albert", "views": 1000000, "dislikes": 67235},
]

# Loop through the list of data
for i in range(len(data)):
    # Send a PUT request to the API to update the video information
    # BASE + "video/"+str(i) constructs the URL like "http://example.com/api/video/0", "http://example.com/api/video/1", etc.
    # data[i] is the payload containing the current video's data
    response = requests.put(BASE + "video/" + str(i), data[i])
    # Print the server's response in JSON format
    print(response.json())

input()  # to pause when executing
response = requests.get(BASE + "video/2")
print(response.json())
