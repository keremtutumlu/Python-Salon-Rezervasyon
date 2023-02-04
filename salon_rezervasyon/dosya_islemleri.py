def max_bilet_sayisi_oku():
    file = open("indirim.txt", "r")
    satir = file.readline()
    bilgiler = satir.split("-")
    file.close()
    return int(bilgiler[1])

def fiyat_oku(kategori):
    file = open("indirim.txt", "r")
    for i in range(0, kategori + 1):
        satir = file.readline()
    bilgiler = satir.split("-")
    file.close()
    return int(bilgiler[1])

def indirim_orani_oku(kategori, b_say):
    file = open("indirim.txt", "r")
    for i in range(0, (kategori * 3) + 3):
        satir = file.readline()
    bilgiler_1 = satir.split("-")
    satir = file.readline()
    bilgiler_2 = satir.split("-")
    satir = file.readline()
    bilgiler_3 = satir.split("-")
    bilgiler_3[2] = max_bilet_sayisi_oku()
    file.close()
    if b_say >= int(bilgiler_1[1]) and b_say <= int(bilgiler_1[2]):
        return int(bilgiler_1[3])
    elif b_say >= int(bilgiler_2[1]) and b_say <= int(bilgiler_2[2]):
        return int(bilgiler_2[3])
    elif b_say >= int(bilgiler_3[1]) and b_say <= int(bilgiler_3[2]):
        return int(bilgiler_3[3])
    else:
        return int(0)