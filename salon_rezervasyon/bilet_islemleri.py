import dosya_islemleri

def kalan_bilet_say_bastir(k_b_say):
    print("Kalan bilet sayıları ;")
    for i in range(0, 4):
        print(i + 1, ". kategori --> ", k_b_say[i], "(", dosya_islemleri.fiyat_oku(i + 1), " tl)")

def kategori_sec(k_b_say):
    kalan_bilet_say_bastir(k_b_say)
    try:
        alinacak_kategori = int(input("Lütfen bilet almak istediğiniz kategoriyi seçiniz. Ana menüye dönmek için 0'ı tuşlayabilirsiniz :"))
    except ValueError:
        print("Lütfen sayı giriniz.")
        alinacak_kategori = -1
    while alinacak_kategori < 0 or alinacak_kategori > 4 or k_b_say[alinacak_kategori - 1] == 0:
        try:
            if alinacak_kategori < 1 or alinacak_kategori > 4:
                alinacak_kategori = int(input("Geçersiz kategori girişi yaptınız. Lütfen tekrar deneyiniz. Ana menüye dönmek için 0'ı tuşlaybilirsiniz : "))
            else:
                alinacak_kategori = int(input("Seçtiğiniz kategoride bilet kalmamıştır lütfen başka kategori seçiniz : "))
        except ValueError:
            print("Lütfen sayı giriniz.")
            alinacak_kategori = -1
    return alinacak_kategori

def bilet_sayisi_sec(k_b_say):
    max_bilet = dosya_islemleri.max_bilet_sayisi_oku()
    try:
        if k_b_say <= max_bilet:
            print("Bu kategoride kalan bilet sayısı {}.".format(k_b_say), end=" ")
        else:
            print("Tek seferde alabileceğiniz maximum bilet sayısı {}.".format(max_bilet), end=" ")
            alinacak_bilet_sayisi = int(input("Bu bilgiye göre almak istediğiniz bilet sayısını giriniz. Ana menüye dönmek için 0'ı tuşlayabilirsiniz : ".format(max_bilet)))
    except ValueError:
        print("Lütfen geçerli bir karakter giriniz.")
        alinacak_bilet_sayisi = 101

    while alinacak_bilet_sayisi > max_bilet or alinacak_bilet_sayisi > k_b_say or alinacak_bilet_sayisi < 0:
        try:
            if alinacak_bilet_sayisi > k_b_say and k_b_say <= max_bilet:
                alinacak_bilet_sayisi = int(input("Elimizde kalan bilet sayısı {}. Lütfen sınırı aşmayacak sayıda bilet talep ediniz : ".format(k_b_say)))
            elif alinacak_bilet_sayisi < 0:
                alinacak_bilet_sayisi = int(input("En az 1, en fazla yukarıda belirtilen sayı üzerine bilet sayınızı seçiniz. Ana menüye dönmek için 0'ı tuşlayabilirsiniz : "))
            else:
                alinacak_bilet_sayisi = int(input("Tek seferde alabileceğiniz bilet sayısı en fazla {} lütfen tekrar deneyiniz : ".format(max_bilet)))
        except ValueError:
            print("Lütfen geçerli bir karakter giriniz.")
            alinacak_bilet_sayisi = 101
    return alinacak_bilet_sayisi

def fiyat_hesapla(kategori, b_say):
    return (dosya_islemleri.fiyat_oku(kategori) * b_say) - (dosya_islemleri.fiyat_oku(kategori) * b_say * (
                dosya_islemleri.indirim_orani_oku(kategori, b_say) / 100))