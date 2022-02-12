print ('masukan dua buah angka')
print ("dan anda akan check hubungan kedua angka tersebut")

angka1 = input("masukan angka pertama: ")
angka1 = int(angka1)

angka2 = input("masukan angka kedua: ")
angka2 = int(angka2)

if (angka1 == angka2) :
    print("%d sama dengan %d"%(angka1,angka2))
if (angka1 != angka2) :
    print("%d tidak sama dengan %d"%(angka1,angka2))
if (angka1 < angka2) :
    print("%d kurang dari %d"%(angka1,angka2))
if (angka1 > angka2) :
    print("%d lebih dari %d"%(angka1,angka2))
if (angka1 <= angka2) :
    print("%d kurang dari sama dengan %d"%(angka1,angka2))
if (angka1 >= angka2) :
    print("%d lebih dari sama dengan %d"%(angka1, angka2))