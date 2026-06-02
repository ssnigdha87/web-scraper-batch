import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os


def scrape_quotes():
    print("Starting scrape job...")

    url = "https://quotes.toscrape.com"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        data.append(
            {
                "quote": q.find("span", class_="text").text,
                "author": q.find("small", class_="author").text,
            }
        )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    os.makedirs("output", exist_ok=True)

    file_name = f"output/quotes_{timestamp}.csv"

    df = pd.DataFrame(data)

    df.to_csv(file_name, index=False)

    print(f"CSV created successfully: {file_name}")


if __name__ == "__main__":
    try:
        scrape_quotes()
        print("Job completed successfully")

    except Exception as e:
        print(f"Job failed: {e}")
        raise