import requests

from dotenv import load_dotenv # The package needed to load environment variables
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY') # Reading the Open API Key we have created in OpenAI portal

# for key, value in os.environ.items():
#    print(f"{key}: {value}")
    
api_key = os.getenv('OPENAI_API_KEY')
# print('OPENAI_API_KEY', api_key)  # Check if the key is loaded properly

# print(response.json()['output']['content'])
"""
response = requests.get('http://localhost:8000/essay/invoke')
if response.status_code == 200:
    try:
        data = response.json()  # Only attempt to decode if the status code is 200
        print("JSON response:", data)
    except requests.exceptions.JSONDecodeError:
        print("Received empty or invalid JSON response")
else:
    print(f"Error: Received status code {response.status_code}")
"""
url = "http://localhost:8000/essay/invoke"  
headers = {
    "Authorization": f"Bearer {api_key}",  # Replace with your actual API key
    "Content-Type": "application/json"
}
response = requests.post(
    url,
    headers=headers,
    json={'input':{'topic':'my best friend'}} # URL that API is running on
)

if response.status_code == 200:
    if response.headers.get('Content-Type') == 'application/json':
        try:
            data = response.json()['output']['content']
            print(data)
        except requests.exceptions.JSONDecodeError:
            print("Response is not a valid JSON")
else:
    print(f"Error: Status code {response.status_code}, Response: {response.text}")

# print(response.json())