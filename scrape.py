from requests import get
from bs4 import BeautifulSoup
import os
os.system('cls' if os.name == 'nt' else 'clear')    #clear the screen

url = "http://quotes.toscrape.com"
response = get(url)

# Check if request was successful
if response.status_code == 200:
    print("Successfully connected!")
else:
    print("Failed to retrieve webpage.")

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify()) # print the content of the webpage
print("-" * 100)

for quote_div in soup.find_all("div", class_="quote"):
    quote_text = quote_div.find("span", class_="text").text
    author = quote_div.find("small", class_="author").text
    tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]

    print(f"Quote: {quote_text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print("-" * 100)
