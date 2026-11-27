import os
os.system("cls")
#1 
print ("\nnomer 1")
buah = ["apel","jeruk","mangga","pisang"]
for i in buah :
    print (i)

#2
print ("\nnomer 2")
angka = [10, 20, 30, 40]
angka.remove(20)
angka.append(50)

print (angka)
#3
print ("\nnomer 3")
nama = ["aaa","bbb","ccc","ddd","eee"]
print (nama)
print (f"panjang = {len(nama)}")

#4 and 5
print ("\nnomer 4 & 5")
nilai = [75, 80, 65, 90, 85]
jumlah = 0
maks = nilai[0]
for i in nilai :
    print (i)
    jumlah += i
    if i > maks :
        maks = i
print (f"jumlah     : {jumlah}")
print (f"maksimal   : {maks}")

#6
print ("\nnomer 6")
deret = [i+1 for i in range (20)]
deret2 = [i for i in deret if i % 2 != 0]
print (deret)
print (deret2)

#7
print ("\nnomer 7")
data = [1, 2, 2, 3, 4, 4, 5]
data2 = []
for i in data :
    if i not in data2 :
        data2.append(i)
print (data)
print (data2)

#8
print ("\nnomer 8")
list1 = [1, 2, 3]
list2 = [3, 4, 5]
gab = []
for i in list1 + list2 :
    if i not in gab :
        gab.append(i)
print (gab)

