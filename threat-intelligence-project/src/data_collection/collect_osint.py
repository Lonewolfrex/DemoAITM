import requests

def get_osint_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data")
        return None

if __name__ == "__main__":
    url = "https://api.example.com/osint"  # Replace with actual OSINT API
    data = get_osint_data(url)
    if data:
        print(data)  # Process and save data as needed