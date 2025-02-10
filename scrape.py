import requests
from bs4 import BeautifulSoup
import os
os.system('cls' if os.name == 'nt' else 'clear')    #clear the screen

url = "http://quotes.toscrape.com"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("Successfully connected!")
else:
    print("Failed to retrieve webpage.")

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify()) # print the content of the webpage
print()
#===============================================================
# Extract the title of the webpage
title = soup.title.string
print(f"Title of the webpage: {title}")
print()
#===============================================================
# Extract all the quotes from the webpage
quotes = soup.find_all('span', class_='text')
for quote in quotes:
    print(quote.text)
print()
#===============================================================
# Extract the author of each quote
authors = soup.find_all('small', class_='author')
for author in authors:
    print(author.text)
print()
#===============================================================
# Extract all the tags
tags = soup.find_all('div', class_='tags')
for tag in tags:
    tag = tag.find_all('a', class_='tag')
    for t in tag:
        print(t.text)
print()
#===============================================================
# Extract the next page link
next_page = soup.find('li', class_='next')
next_page_link = next_page.find('a')['href']
print(f"Next page link: {url}{next_page_link}")
print()
#===============================================================
# Extract all the quotes from the next page
next_page_url = url + next_page_link
response = requests.get(next_page_url)
soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('span', class_='text')
for quote in quotes:
    print(quote.text)
print()