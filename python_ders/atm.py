#  ATM para çekme
# Bakiye ve çekilecek tutar alınır. Tutar 10'un katı değilse, bakiyeden büyükse ya da 5000 TL’yi aşıyorsa neden belirtilerek reddedilir. 
# Aksi halde 200, 100, 50, 20 ve 10 TL’lik banknotlardan en az sayıda banknotla ödeme yapılır, kaçar adet verileceği yazılır.

# Örnek: 380 → 200×1, 100×1, 50×1, 20×1, 10×1
# Konular: // ve % zinciri, or, ayrı hata mesajları
# Test: 0, 5, 10, 380, 5000, 5010
# İpucu: her banknotta önce // ile adedi, sonra % ile kalanı bul; kalan bir sonraki banknota geçer.
bakiye = int(input("Bakiyenizi girin: "))
cekilecek_tutar = int(input("Çekilecek tutarı girin: "))
if cekilecek_tutar > bakiye or cekilecek_tutar > 5000 or cekilecek_tutar % 10 !=0:
    print("Reddedilir")
else:
    kalan = cekilecek_tutar

    adet200 = kalan // 200
    kalan = kalan % 200
    adet100 = kalan // 100
    kalan = kalan % 100
    adet50 = kalan // 50
    kalan = kalan % 50
    adet20 = kalan // 20
    kalan = kalan % 20
    adet10 = kalan // 10



    print("Banknotlar:")
    if adet200 > 0:
        print(f"200 TL x {adet200}")
    if adet100 > 0:
        print(f"100 TL x {adet100}")
    if adet50 > 0:
        print(f"50 TL x {adet50}")
    if adet20 > 0:
        print(f"20 TL x {adet20}")
    if adet10 > 0:
        print(f"10 TL x {adet10}")



