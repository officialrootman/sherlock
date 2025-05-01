import requests
import sys
import json
from concurrent.futures import ThreadPoolExecutor

# sites.json dosyasından site listesini yükle
def load_sites():
    with open("sites.json", "r") as file:
        return json.load(file)["sites"]

# Kullanıcı adı arama
def search_username(site, username):
    url = site.format(username)
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Bulundu: {url}")
        else:
            print(f"[-] Bulunamadı: {url}")
    except requests.RequestException:
        print(f"[!] Hata oluştu: {url}")

# Ana işlem
def main(username):
    sites = load_sites()
    print(f"Kullanıcı adı aranıyor: {username}")
    print("-" * 50)

    with ThreadPoolExecutor(max_workers=10) as executor:
        for site in sites:
            executor.submit(search_username, site, username)

# Komut satırı kontrolü
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: sherlock <kullanıcı_adı>")
    else:
        main(sys.argv[1])
