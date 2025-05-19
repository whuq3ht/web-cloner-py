# 🕸️ Web Cloner

Basit bir Python scripti ile bir web sitesinin tüm HTML içeriğini ve medya dosyalarını (CSS, JS, görseller) local olarak indirmenizi sağlar.

---

## 📌 Özellikler

- `index.html` olarak sayfayı indirir.
- `<link>`, `<script>`, `<img>` etiketlerini tarar.
- Statik dosyaları (JS, CSS, görseller) `website_backup` klasörüne indirir.
- Dizin yapısını koruyarak yerel kopya oluşturur.

---

## 🛠️ Kullanılan Teknolojiler

| Kütüphane      | Açıklama                    |
|----------------|-----------------------------|
| `requests`     | HTTP istekleri için         |
| `os`           | Dosya ve klasör işlemleri   |
| `BeautifulSoup`| HTML parsing (bs4)          |
| `urllib.parse` | URL çözümleme işlemleri     |

---

## ⚙️ Kurulum

### Gerekli Kütüphaneler

Python 3.6+ yüklü olduğundan emin olun.

🚀 Kullanım
```
python web-cloner.py
```

## Çıktı Yapısı
site-backup/
├── index.html
├── assets/
│   ├── style.css
│   └── script.js
├── images/
│   └── logo.png


## ⚠️ Uyarılar
│ Bu araç sadece halka açık web siteler için kullanılmalıdır.

├── Telif hakkı içeren içerikleri izinsiz indirmek yasal değildir.

└── Dinamik (JavaScript ile yüklenen) içerikler bu script ile indirilemez.

