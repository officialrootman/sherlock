import requests
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore

# Colorama başlat
init(autoreset=True)

# JSON'dan site listesini yükle
def load_sites():
    with open("sites.json", "r") as file:
        return json.load(file)["username_search_sites"]

# Kullanıcı adı arama
def search_username(site, username):
    url = site.format(username)
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] Bulundu: {url}")  # YEŞİL
        else:
            print(f"{Fore.RED}[-] Bulunamadı: {url}")  # KIRMIZI
    except requests.RequestException:
        print(f"{Fore.YELLOW}[!] Hata oluştu: {url}")  # SARI

# Ana işlem
def main(username):
    sites = load_sites()
    print(f"{Fore.CYAN}Kullanıcı adı aranıyor: {username}")  # MAVİ
    print("-" * 48)

    with ThreadPoolExecutor(max_workers=10) as executor:
        for site in sites:
            executor.submit(search_username, site, username)

# Komut satırı kontrolü
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Kullanım: python sherlock.py user123")
    else:
        main(sys.argv[1])
