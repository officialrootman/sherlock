import requests
import sys
import json
from concurrent.futures import ThreadPoolExecutor

# sites.json dosyasından site listesini yükle
def load_sites():
    with open("sites.json", "r") as file:
        return json.load(file)["sites"]

# Kullanıcı adı arama
def search_username(site, username, results):
    url = site.format(username)
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            results.append(f"[+] Bulundu: {url}")
        else:
            results.append(f"[-] Bulunamadı: {url}")
    except requests.RequestException:
        results.append(f"[!] Hata oluştu: {url}")

# Ana işlem
def main(username):
    sites = load_sites()
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for site in sites:
            executor.submit(search_username, site, username, results)
    
    # Sonuçları dosyaya kaydet
    with open("info.txt", "w") as file:
        file.write("\n".join(results))
    print("\nSonuçlar kaydedildi: results.txt")

# Komut satırı kontrolü
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: sherlock <kullanıcı_adı>")
    else:
        main(sys.argv[1])
