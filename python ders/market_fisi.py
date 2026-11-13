# 3. Market fişi
# Birim fiyat ve adet alınır. Ara toplam, %20 KDV ve genel toplam yazdırılır; hepsi 2 basamaklı olur.

# Örnek: 85.50 ve 3 → ara toplam 256.50, KDV 51.30, toplam 307.80
# Konular: f-string biçimlendirme, yüzde hesabı
birim_fiyat = float(input("Birim fiyatı giriniz: "))
adet = int(input("Adet sayısını giriniz: "))

ara_toplam = birim_fiyat * adet
kdv = ara_toplam * 0.20
genel_toplam = ara_toplam + kdv

print(f"Ara toplam: {ara_toplam:.2f} TL")
print(f"KDV (%20): {kdv:.2f} TL")
print(f"Genel toplam: {genel_toplam:.2f} TL")