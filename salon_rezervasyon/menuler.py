import salon_islemleri
import bilet_islemleri

def ana_menu():
    print("--------------------\n------ANA MENÜ------\n--------------------\n1.) Rezervasyon\n2-) Salonu Yazdır\n3-) Ciro Göster\n4-) Yeni Etkinlik\n0-) Çıkış\n--------------------")

    try:
        secim = int(input("Seçiminizi sayıyla giriniz : "))
    except ValueError:
        print("Lütfen sayı giriniz.")
        secim = -1

    while secim < 0 or secim > 4:
        try:
            secim = int(input("Geçersiz giriş yaptınız lütfen tekrar deneyiniz : "))
        except ValueError:
            print("Lütfen sayı giriniz.")
            secim = -1
    return secim

def rezervasyon_menu(b_say, k_b_say, salon, s_b_koltuk, ciro):
    if b_say == 0:
        print("Boş koltuk kalmamıştır. Lütfen yeni etkinlik oluşturunuz...")
        return 0
    else:
        alinacak_kategori = bilet_islemleri.kategori_sec(k_b_say)
        if alinacak_kategori == 0:
            return alinacak_kategori
        alinacak_b_say = bilet_islemleri.bilet_sayisi_sec(k_b_say[alinacak_kategori - 1])
        if alinacak_b_say == 0:
            return 1

        k_b_say[alinacak_kategori - 1] -= alinacak_b_say
        b_say -= alinacak_b_say

        if alinacak_kategori == 1 or alinacak_kategori == 3:
            salon_islemleri.rezerve_edilen_koltuk_1(salon, s_b_koltuk[alinacak_kategori - 1], alinacak_b_say)
        else:
            salon_islemleri.rezerve_edilen_koltuk_2(salon, s_b_koltuk[alinacak_kategori - 1], alinacak_b_say)

        if alinacak_kategori == 1 or alinacak_kategori == 3:
            salon_islemleri.salona_isle_1(salon, s_b_koltuk[alinacak_kategori - 1], alinacak_b_say)
        else:
            salon_islemleri.salona_isle_2(salon, s_b_koltuk[alinacak_kategori - 1], alinacak_b_say)

        ucret = bilet_islemleri.fiyat_hesapla(alinacak_kategori, alinacak_b_say)
        ciro [alinacak_kategori - 1] = ciro[alinacak_kategori - 1] + ucret
        print("Toplam ücret {} tl'dir. İyi eğlenceler dileriz.".format(ucret))

def ciro_menusu(ciro):
    for i in range(1, 5):
        print(i, ". kategori ciro : ", ciro[i - 1])
    print("Toplam ciro : ", ciro[0] + ciro[1] + ciro[2] + ciro[3])