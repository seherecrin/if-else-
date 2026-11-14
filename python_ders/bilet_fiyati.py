# 7. Müze bileti
# Temel fiyat 100 TL.

# 7 yaşından küçükler ve 65 yaş ve üstü ücretsizdir.
# Öğrenciyse (E/H) fiyat %50 indirimlidir.
# Hafta sonu (cumartesi/pazar), ücretli biletlere indirimden sonra +20 TL eklenir.

# Örnek: 20 yaş, öğrenci, cumartesi → 70 TL.

# Konular: iç içe if, strip().lower(), in ile gün kontrolü
# Ek görev: aynı programı and kullanarak iç içe if olmadan yaz.
 

yas = int(input("Yaşınızı giriniz: "))
ogrenci = input("Öğrenci misiniz? (E/H): ").strip().lower()
gun = input("Hangi gün? ").strip().lower()

fiyat = 100

if yas < 7 or yas >= 65:
    fiyat = 0
else:
    if ogrenci == "e":
        fiyat = fiyat * 0.5

    if gun in ["cumartesi", "pazar"]:
        fiyat = fiyat + 20

print("Bilet fiyatı:", fiyat, "TL")
