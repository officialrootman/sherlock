# 🔍 Kullanıcı Adı Arama Tool'u

Bu tool, belirli bir kullanıcı adının farklı platformlarda olup olmadığını tespit etmek için geliştirilmiştir. 📡  
Colorama desteği sayesinde sonuçlar **renkli bir şekilde terminalde görüntülenir**, böylece arama sonuçlarını kolayca takip edebilirsiniz!  

## 🚀 Özellikler
- 🔹 **100+ popüler siteye kullanıcı adı arama desteği**
- 🔹 **Renkli çıktı (Bulunan: Yeşil, Bulunamayan: Kırmızı, Hata: Sarı)**
- 🔹 **Hızlı ve paralel aramalar (`ThreadPoolExecutor` ile)**
- 🔹 **JSON tabanlı veri deposu ile kolay genişletilebilir yapı**
- 🔹 **Otomatik JSON güncellemesi ile yeni siteler eklenebilir**

## 📦 Kurulum
Tool'u çalıştırmak için aşağıdaki adımları izleyin:

```bash
## Kurulum:
apt install py-pip
pip install colorama requests
git clone https://github.com/officialrootman/sherlock.git
cd sherlock

## Kullanım
Eğer tekli istersen:
python3 sherlock.py user123

Eğer Çoklu İstersen:
python3 sherlock.py user1 user12 user123
