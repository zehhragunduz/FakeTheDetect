# Veri temizleme fonksiyonları

def clean_price(price_str):
    return float(price_str.replace('TL', '').strip().replace(',', '.'))