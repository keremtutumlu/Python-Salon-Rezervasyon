import dosya_islemleri

def rezerve_edilen_koltuk_1(salon, s_b_koltuk, b_say):
    i = s_b_koltuk[0] + 1
    j = s_b_koltuk[1] + 1
    print("Rezerve edilen koltuklar (Sıra - Koltuk) : ")
    for sayac in range(0, b_say):
        if j == 15:
            print(i, " - ", j)
            i += 1
            j = 6
        else:
            print(i, " - ", j)
            j += 1

def rezerve_edilen_koltuk_2(salon, s_b_koltuk, b_say):
    i = s_b_koltuk[0] + 1
    j = s_b_koltuk[1] + 1
    print("Rezerve edilen koltuklar (Sıra - Koltuk) : ")
    for sayac in range(0, b_say):
        if j < 6 and j >= 1:
            if j == 1:
                print(i, " - ", j)
                j = 16
            else:
                print(i, " - ", j)
                j -= 1
        else:
            if j == 20:
                print(i, " - ", j)
                i += 1
                j = 5
            else:
                print(i, " - ", j)
                j += 1

def salonu_bastir(a):
    print(end = "   ")
    for sayac in range(1, 21):
        if sayac < 10:
            print(sayac, end = "  ")
        else:
            print(sayac, end = " ")
    print()
    for i in range(0,20):
        if i < 9:
            print(i + 1, end = "  ")
        else:
            print(i + 1, end = " ")
        for j in range(0, 20):
            if a[i][j] == 0:
                print("-", end = "  ")
            else:
                print("x", end = "  ")
        print()

def salona_isle_1(salon, s_b_koltuk, b_say):
    i = s_b_koltuk[0]
    j = s_b_koltuk[1]
    for sayac in range(0, b_say):
        if j == 14:
            salon[i][j] = 1
            i += 1
            j = 5
        else:
            salon[i][j] = 1
            j += 1
        s_b_koltuk[0] = i
        s_b_koltuk[1] = j

def salona_isle_2(salon, s_b_koltuk, b_say):
    i = s_b_koltuk[0]
    j = s_b_koltuk[1]
    for sayac in range(0, b_say):
        if j < 5 and j >= 0:
            if j == 0:
                salon[i][j] = 1
                j = 15
            else:
                salon[i][j] = 1
                j -= 1
        else:
            if j == 19:
                salon[i][j] = 1
                i += 1
                j = 4
            else:
                salon[i][j] = 1
                j += 1
    s_b_koltuk[0] = i
    s_b_koltuk[1] = j

