import requests
from bs4 import BeautifulSoup
import csv

# Define the base URL
base_url = "http://quotes.toscrape.com"

# Open CSV file with UTF-8 encoding to avoid unreadable characters
with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])  # Write header row

    page = 1  # Start with page 1
    while True:
        url = f"{base_url}/page/{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            break  # Stop if no quotes are found (end of pages)

        for quote_div in quotes:
            quote_text = quote_div.find("span", class_="text").text
            author = quote_div.find("small", class_="author").text
            tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]

            writer.writerow([quote_text, author, ", ".join(tags)])

        print(f"Scraped page {page}")
        page += 1  # Move to the next page

print("Scraping complete! Data saved to quotes.csv 🎉")
