import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send request to website
        response = requests.get(url)
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all headings (h1, h2, h3)
        print("\n--- Headings Found ---\n")
        for tag in soup.find_all(['h1', 'h2', 'h3']):
            print(tag.get_text().strip())

        # Example: Extract all links
        print("\n--- Links Found ---\n")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                print(href)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


# Run the scraper
url = input("Enter website URL: ")
scrape_website(url)