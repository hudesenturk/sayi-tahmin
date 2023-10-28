from sayi_bulma_ses import SesliAsistan
import random

asistan = SesliAsistan()

def sayi_tahmin_oyunu():
    sayi = random.randint(1, 100)
    print("1 ile 100 arasında bir sayı tahmin et.")
    asistan.konus("1 ile 100 arasında bir sayı tahmin et.")
    tahmin_edildi = False

    while not tahmin_edildi:
        tahmin = asistan.dinle()

        try:
            tahmin = int(tahmin)
            print(tahmin)
            if tahmin == sayi:
                print("Tebrikler! Doğru.")
                asistan.konus("Tebrikler! Doğru.")
                tahmin_edildi = True
            elif tahmin < sayi:
                print("Daha yüksek bir sayı söyleyin.")
                asistan.konus("Daha yüksek bir sayı söyleyin.")
            else:
                print("Daha düşük bir sayı söyleyin.")
                asistan.konus("Daha düşük bir sayı söyleyin.")
        except ValueError:
            print("Geçerli bir sayı söyleyin.")
            asistan.konus("Geçerli bir sayı söyleyin.")

sayi_tahmin_oyunu()