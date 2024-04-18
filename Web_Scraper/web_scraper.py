import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.base_url = "https://www.openai.com/blog"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def scrape(self):
        response = requests.get(self.base_url, headers=self.headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            articles = soup.find_all("article")

            for article in articles:
                title = article.find("h2", class_="entry-title").text.strip()
                print(title)
        else:
            print(f"Failed to retrieve the webpage. HTTP Error {response.status_code}")

if __name__ == "__main__":
    scraper = WebScraper()
    scraper.scrape()
