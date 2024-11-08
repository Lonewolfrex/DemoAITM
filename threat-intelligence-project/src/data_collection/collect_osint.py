import requests
import os
from dotenv import load_dotenv

def get_vt_data(url):
    api_key = os.getenv('API_KEY')
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {
        'apikey': api_key,
        'resource': 'example.com'  # Replace with the URL you want to analyze
    }
    response = requests.get(url, params=params)
    print(response.json())

if __name__ == "__main__":
    url = "https://www.virustotal.com/vtapi/v2/url/report"  # Replace with actual OSINT API
    data = get_vt_data(url)
    if data:
        print(data)  # Process and save data as needed