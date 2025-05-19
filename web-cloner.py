import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def download_file(url, folder):
    try:
        local_filename = os.path.join(folder, urlparse(url).path.lstrip('/'))
        os.makedirs(os.path.dirname(local_filename), exist_ok=True)
        response = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"[✓] İndirildi: {local_filename}")
    except Exception as e:
        print(f"[!] Hata: {url} - {e}")

def scrape_site(base_url, output_dir="website_backup"):
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # index.html olarak kaydet
    index_path = os.path.join(output_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    print("[✓] Anasayfa indirildi.")

    tags = {
        "link": "href",
        "script": "src",
        "img": "src",
    }

    for tag, attr in tags.items():
        for element in soup.find_all(tag):
            file_url = element.get(attr)
            if file_url:
                full_url = urljoin(base_url, file_url)
                download_file(full_url, output_dir)

# Kullanım
if __name__ == "__main__":
    hedef_url = input("URL girin (örn: whuq'un cuku): ")
    dizin = input("Kaydedilecek klasör ismi (örn: klasor_ismi): ")
    scrape_site(hedef_url, dizin)
