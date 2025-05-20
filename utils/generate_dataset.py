import pandas as pd
import random
import os

# Örnek ürün ve satıcı listeleri
titles = [
    "Baseus W04 Pro Kulaklık", "JBL T110 Kulaklık", "Xiaomi Redmi Buds 4",
    "Anker Soundcore Life P2", "Samsung Level U2", "Haylou GT1 Pro",
    "Philips TAT1235BK", "Sony WH-CH510", "Huawei Freebuds SE", "Pioneer SE-C3T"
]

sellers = [
    "Baseus Official Store", "JBL Türkiye", "Mi Market", "Anker Türkiye",
    "Samsung Mağazası", "Haylou Teknoloji", "Philips Ses Sistemleri",
    "Sony Center", "Huawei Satıcısı", "Pioneer Ses"
]

urls = [
    "https://www.trendyol.com/baseus-w04", "https://www.trendyol.com/jbl-t110",
    "https://www.trendyol.com/xiaomi-redmi-buds4", "https://www.trendyol.com/anker-p2",
    "https://www.trendyol.com/samsung-level-u2", "https://www.trendyol.com/haylou-gt1",
    "https://www.trendyol.com/philips-tat1235", "https://www.trendyol.com/sony-wh510",
    "https://www.trendyol.com/huawei-freebuds-se", "https://www.trendyol.com/pioneer-sec3t"
]

# Veri üretimi
data = []
for _ in range(600):
    idx = random.randint(0, 9)
    title = titles[idx]
    seller = sellers[idx]
    price = round(random.uniform(249.0, 799.9), 2)
    url = urls[idx]

    # Etiketleme (is_fake)
    seller_lower = seller.lower()
    is_fake = int(price < 350 and not any(k in seller_lower for k in ["official", "mağaza", "store", "center"]))

    data.append({
        "product_title": title,
        "seller_name": seller,
        "price": price,
        "product_url": url,
        "is_fake": is_fake
    })

df = pd.DataFrame(data)

# Klasör ve dosya oluştur
os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/trendyol_kulaklik_600_tagged.csv", index=False, encoding="utf-8-sig")

print("✅ Etiketli veri başarıyla oluşturuldu: data/raw/trendyol_kulaklik_600_tagged.csv")
