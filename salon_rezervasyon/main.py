import numpy as np
import salon_islemleri
import menuler

salon = np.zeros((20,20))
bilet_sayisi = int(400)
kategori_b_say = [100, 100, 100, 100]
son_bos_koltuk = [[0, 5], [0, 4], [10, 5], [10, 4]]
cikis_kontrolu = int(1)
ciro = [0, 0, 0, 0]

while cikis_kontrolu != 0:
    cikis_kontrolu = menuler.ana_menu()
    if cikis_kontrolu == 1:
        menuler.rezervasyon_menu(bilet_sayisi, kategori_b_say, salon, son_bos_koltuk, ciro)
        continue

    elif cikis_kontrolu == 2:
        salon_islemleri.salonu_bastir(salon)

    elif cikis_kontrolu == 3:
        menuler.ciro_menusu(ciro)

    elif cikis_kontrolu == 4:
        salon = np.zeros((20, 20))
        bilet_sayisi = int(400)
        kategori_b_say = [100, 100, 100, 100]
        son_bos_koltuk = [[0, 5], [0, 4], [10, 5], [10, 4]]
        ciro = [0, 0, 0, 0]
        print("Yeni etkinlik oluşturuldu...")