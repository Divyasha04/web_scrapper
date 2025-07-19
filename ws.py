import requests
from bs4 import BeautifulSoup

# URL of the news website 
URL = 'https://www.ndtv.com/latest'

# FetchIing the HTML content
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve the web page.")
    exit()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all h2 tags (commonly used for headlines)
headlines = soup.find_all('h2')

# Extract and clean the text
headline_list = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

# Save to a text file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for idx, headline in enumerate(headline_list, start=1):
        file.write(f"{idx}. {headline}\n")

print(f"✅ {len(headline_list)} headlines saved to 'headlines.txt'")

