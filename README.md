📰 Web Scraper for News Headlines

This Python script is a simple web scraper that fetches top news headlines from a news website using requests and BeautifulSoup. It demonstrates how to collect data from the web and save it in a .txt file for further use.


# Step 1: Send a GET request to the news site
url = 'https://example.com/news'
response = requests.get(url)
html = response.text

# Step 2: Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Find all headline tags (e.g., h2)
headlines = soup.find_all('h2')

# Step 4: Extract text and save to a file
with open("headlines.txt", "w") as f:
    for h in headlines:
        f.write(h.get_text(strip=True) + "\n")
🔄 Customization Tips
To scrape a different site, just change the url and adjust the tag in soup.find_all('h2') accordingly.

Use soup.find_all('a'), soup.select(), or soup.find_all(class_="...") for more targeted scraping.











Ask ChatGPT
