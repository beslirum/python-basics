#kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet 
#alabilme durumunu kontrol et. ehliyet koşulu yaş min 18 ve eğitim durumu
#lise ya da üni olmalıdır.

'''
num = int(input("Yaşınızı giriniz: "))
education = int(input("Eğitimi durumunuz lise veya üniversite ise 1, değil ise 0'ı giriniz: "))

if education!=0 and education!=1:
    print("Eğitim bilgisi hatalı girildi, tekrar giriniz!")
    education = int(input("Eğitimi durumunuz lise veya üniversite ise 1, değil ise 0'ı giriniz: "))
elif education==0 or num<18:
    print("Ehliyet alamazsınız.")
else:
    print("Ehliyet alma koşulunu sağlıyorsunuz.") '''

#Bir öğrencinin 2 yazılı 1 sözlü ortalamasını bilgilere göre yazdır
#0-24 -> 0          25-44->1        45-54->2        55-69->3
#70-84->4           85-100->5
'''
exam1 = int(input("Enter first exam: "))
exam2=int(input("Enter second exam: " ))
quiz=int(input("Enter the quiz: "))

total = (exam1+exam2+quiz)/3

if total==0 and total==24:
    print(0)
eçlif total==25 and total==44:
    print(1)
elif total==45 and total==54:
    print(2)
elif total==55 and total==69:
    print(3)
elif total==70 and total==84:
    print(4)
else:
    print(5) '''





#Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdakine göre hesapla
#1. Bakım => 1. Yıl         2.Bakım=>2. Yıl         3.Bakım=>3. Yıl
#Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesapla
#datetime modülünü kullanmamız gerekiyor
import datetime

tarih = input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9):")
tarih=tarih.split('/')
#print(tarih[0])
#print(tarih[1])
#print(tarih[2])
trafigecikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()

fark=simdi - trafigecikis
days=fark.days
if days<=365:
    print("1. Servis aralığı")
elif days>365 and days<=365*2:
    print("2. Servis aralığında")
elif days>730 and days<=365*3:
    print("3. Servis aralığında")
else:
    print("Hatalı süre")

