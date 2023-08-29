#OBJECT ORIENTED PROGRAMMING (OOP)

# Sınıf tanımı: Bu, 'Araba' adlı bir sınıftır.
class Araba:
    # Sınıf değişkeni: Tüm Araba örnekleri için geçerlidir.
    teker_sayisi = 4

    # Başlatıcı (__init__) fonksiyonu: Araba örneği oluşturulduğunda otomatik olarak çalışır.
    def __init__(self, marka, model, renk):
        # Örnek değişkenleri: Her Araba örneği için benzersizdir.
        self.marka = marka
        self.model = model
        self.renk = renk

    # Örnek fonksiyonu: Araba örneğinin hareketini simgeler.
    def hareket_et(self):
        print(f"{self.marka} {self.model} hareket ediyor!")

# Araba sınıfından örnekler oluşturma
araba1 = Araba("Toyota", "Corolla", "Beyaz")
araba2 = Araba("BMW", "M3", "Kırmızı")

# Araba örneğinin özelliklerini ve fonksiyonlarını kullanma
print(f"Araba1 marka: {araba1.marka}")
print(f"Araba1 model: {araba1.model}")
print(f"Araba1 renk: {araba1.renk}")

araba1.hareket_et()

print(f"Araba2 marka: {araba2.marka}")
print(f"Araba2 model: {araba2.model}")
print(f"Araba2 renk: {araba2.renk}")

araba2.hareket_et()

# Sınıf değişkenine erişim
print(f"Araba teker sayısı: {Araba.teker_sayisi}")


