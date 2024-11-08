 
import requests
from bs4 import BeautifulSoup

def scrape_forum(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('div', class_='post')  # Adjust selector based on forum structure
    for post in posts:
        print(post.text)

if __name__ == "__main__":
    forum_url = "https://exampleforum.com/threats"  # Replace with actual forum URL
    scrape_forum(forum_url)