import time
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = "https://www.trendyol.com/kulaklik-x-c92?pi={}"

data = []

for page in range(1, 6):  # test için ilk 5 sayfa
    print(f"📄 Sayfa {page} çekiliyor...")
    driver.get(base_url.format(page))
    time.sleep(4)

    products = driver.find_elements(By.CLASS_NAME, "p-card-chldrn-cntnr")

    for product in products:
        try:
            title = product.find_element(By.CLASS_NAME, "prdct-desc-cntnr-name").text
            seller = product.find_element(By.CLASS_NAME, "prdct-desc-cntnr-ttl").text
            price = product.find_element(By.CLASS_NAME, "prc-box-dscntd").text
            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

            data.append({
                "product_title": title,
                "seller_name": seller,
                "price": price.replace("TL", "").strip(),
                "product_url": "https://www.trendyol.com" + link
            })
        except:
            continue

driver.quit()

os.makedirs("data/raw", exist_ok=True)
df = pd.DataFrame(data)
df.to_csv("data/raw/trendyol_kulaklik.csv", index=False, encoding="utf-8-sig")
print("✅ Veri başarıyla kaydedildi: data/raw/trendyol_kulaklik.csv")
