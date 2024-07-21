import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example-blog.com"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all article titles
    titles = soup.find_all('h2', class_='post-title')

    # Print each title
    for title in titles:
        print(title.get_text())
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
