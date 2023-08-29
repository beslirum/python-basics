#Bankamatik Uygulaması

RumeysaHesap = {
    'ad': 'Rumeysa',
    'hesapNo' : '4444',
    'bakiye': 3000,
    'ekHesap': 2000
}
MeteHesap = {
    'ad': 'Mete',
    'hesapNo' : '3434',
    'bakiye': 5000,
    'ekHesap': 1210
}
def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= hesap['bakiye']
        print('paranızı alabilirsiniz.')
        print(f"Kalan bakiye: {hesap['bakiye']}")


    elif hesap['bakiye'] < miktar:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
            elif ekHesapKullanimi == 'h':
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
            else:
                print('Geçersin giriş')
    else:
        print('Yetersiz bakiye')


paraCek(RumeysaHesap, 3000)

