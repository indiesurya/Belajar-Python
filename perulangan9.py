terus_tanya = True
while (terus_tanya) :
    inputan = input("masukan angka kurang dari 10! :")
    angka = int(inputan)

    if (angka < 10) :
        terus_tanya = True
    else :
        terus_tanya = False