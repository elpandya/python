x = 4

nilai = 5 > x
print (nilai)

nilai2 = x > 9
print (nilai2)

nilai2 = int(nilai2)
print (nilai2)

nilai3 = x==7
print (nilai3)

nilai4 = x!=7
print (nilai4)

nilai5 = x == 4  #kurang tepat lebih baik menggunakan ==
print (nilai4)
nilai6 = x != 4 #kurang tepat lebih baik menggunakan !=
print (nilai6)

#identitas sebuah variabel atau alamat
x = 5
y = 5

print ("addres x is",hex(id(x)))
print ("addres y is",hex(id(y)))
hasil = x is y #sudah tepat karena membandingkan variabel dengan variabel
print ("bernilai", hasil)
hasil2 = x is not y #sudah tepat karena membandingkan variabel dengan variabel
print ("bernilai", hasil2)