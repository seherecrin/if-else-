import math
yaricap = float(input("Yarıçapı giriniz: "))
yukselik = float(input("Yüksekliği giriniz: "))
hacim_m3 = math.pi * yaricap ** 2 * yukselik
litre_m3 = hacim_m3 * 1000
dolu = litre_m3 * 0.80
print(f"Hacim: {litre_m3:.2f} lt")
print(f"Doluluk: {dolu:.2f} lt")

