import random

def kelime_sec():
    kelimeler = ["python", "bilgisayar", "yazılım", "programlama", "veri", "yapayzeka"]
    return random.choice(kelimeler)

def kelime_tahmin_oyunu():
    print("Kelime Tahmin Oyununa Hoş Geldiniz!")
    
    secilen_kelime = kelime_sec()
    gorunen_kelime = ["_"] * len(secilen_kelime)
    can = 6
    tahmin_edilen_harfler = []

    while can > 0 and "_" in gorunen_kelime:
        print("\nKelime:", " ".join(gorunen_kelime))
        print(f"Kalan can: {can}")
        print(f"Şimdiye kadar tahmin edilen harfler: {', '.join(tahmin_edilen_harfler)}")

        tahmin = input("Bir harf tahmin edin: ").lower()

        if not tahmin.isalpha() or len(tahmin) != 1:
            print("Lütfen geçerli bir harf girin.")
            continue

        if tahmin in tahmin_edilen_harfler:
            print(f"{tahmin} harfini zaten tahmin ettiniz.")
            continue

        tahmin_edilen_harfler.append(tahmin)

        if tahmin in secilen_kelime:
            print(f"Tebrikler! {tahmin} harfi doğru.")
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    gorunen_kelime[i] = tahmin
        else:
            can -= 1
            print(f"Yanlış tahmin! {tahmin} harfi kelimede yok.")

    if "_" not in gorunen_kelime:
        print("\nTebrikler! Kelimeyi doğru tahmin ettiniz:", secilen_kelime)
    else:
        print("\nÜzgünüm, kaybettiniz. Doğru kelime:", secilen_kelime)

# Oyunu başlat
kelime_tahmin_oyunu()
