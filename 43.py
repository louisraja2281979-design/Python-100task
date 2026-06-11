import requests
from bs4 import BeautifulSoup
import os

def download_image(url, folder="images"):
    os.makedirs(folder, exist_ok=True)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = os.path.join(folder, url.split("/")[-1].split("?")[0])
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")

def scrape_images(page_url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(page_url, headers=headers)

    if response.status_code != 200:
        print("Failed to access page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    image_urls = set()

    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            image_urls.add(src)

    print(f"Found {len(image_urls)} images")

    for url in image_urls:
        print(url)
        download_image(url)

if __name__ == "__main__":
    url = input("Enter public webpage URL: ")
    scrape_images(url)