# Elektrik faturası

# İlk 100 kWh için kWh başına 2 TL.
# 100–300 kWh arasındaki kısım için 3 TL.
# 300 kWh üzeri kısım için 4.5 TL.
# Her faturaya 25 TL sabit bedel eklenir, sonra toplama %20 KDV uygulanır.
# Negatif değer reddedilir.

# kwh = float(input("Tüketim (kWh): "))

# if kwh < 0:
#     print("Tüketim negatif olamaz")
# else:
#     if kwh <= 100:
#         enerji = kwh * 2
#     elif kwh <= 300:
#         enerji = 100 * 2 + (kwh - 100) * 3
#     else:
#         enerji = 100 * 2 + 200 * 3 + (kwh - 300) * 4.5

#     sabit = 25
#     ara_toplam = enerji + sabit
#     kdv = ara_toplam * 0.20
#     toplam = ara_toplam + kdv


#     print(f"Enerji bedeli: {enerji:.2f} TL")
#     print(f"Sabit bedel: {sabit:.2f} TL")
#     print(f"KDV (%20): {kdv:.2f} TL")
#     print(f"Ödenecek tutar: {toplam:.2f} TL")






# 10. Kargo ücreti hesaplayıcı
# En, boy, yükseklik (cm) ve gerçek ağırlık (kg) alınır.

# Desi = en × boy × yükseklik / 3000
# Ücretlendirilecek ağırlık = math.ceil(gerçek ağırlık ile desiden büyük olan)
# İlk 3 kg için 60 TL, sonraki her kg için 15 TL
# Şehir dışına (E/H) %30 eklenir
# 30 kg üstü paket kabul edilmez, kullanıcıya nedeni yazılır

# Örnek: 40×30×25 cm, 4.2 kg, şehir dışı → desi 10, ücret 165 TL, şehir dışıyla 214.50 TL.

# Konular: hacim hesabı, math.ceil, max(), if/elif/else, isdigit ile girdi denetimi, f-string
# Ek görev: sonucu ayri_mesaj mantığıyla yaz; reddedilen paketler için neden belirt.
import math
en = float(input("Kargonun enini alın: "))
boy = float(input("Kargonun boyunu alın: "))
yükseklik = float(input("Kargonun yüksekliğini alın: "))
gerçek_ağırlık = float(input("Kargonun gerçek ağırlığını alın: "))
desi = en * boy * yükseklik / 3000
math.ceil
sehir_disi = input("Şehir dışında mı? (E/H): ").strip().lower()
kilo =math.ceil(max(gercek_agirlik, desi))

if kilo> 30:
    print("30kilo üstü kabul edilmez!")
else:
    if kilo <= 3:
        ucret = 60
    else:
        ucret = 60 + (kilo-3) * 15
    if sehir_disi == "e":
        ucret = ucret * 1.30    

    print(f"Desi: {desi:.2f}")
    print(f"Ücretlendirilen ağırlık: {kilo} kg")
    print(f"Ücret: {ucret:.2f} TL")    