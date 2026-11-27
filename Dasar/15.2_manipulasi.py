import os
os.system("cls")
# operasi
# Index 0(-3)   1(-2)   2(-1)

data = ["apel","melon","pisang"]

# Mengambil data dari sebuah list
data0 = data[0]
print (data0)

data_akhir = data[-1]
print (data_akhir)

data0 = data[-3]
print (data0)

# Mengambil informasi jumlah data dalam list
panjang = len(data)
print (panjang)

print (f"\ndata awal = \n{data}")
data.insert(1,"pepaya")
# variabel.insert(index,tambahan)
print (f"data setelah ditambah = \n{data}")

data.append("nanas")
# otomatis menambahkan di akhir
#berguna untuk list dalam list
print (f"\ndata setelah ditambah = \n{data}")

# menggabungkan 2 list
hewan = ['sapi','kambing','ayam']
data.extend(hewan)
print (f"\ndata setelah digabung = \n{data}")

data[0] = "kurma"
print (f"\ndata setelah diganti (index ke 0) = \n{data}")

data.remove("pepaya")
print (f"\ndata setelah dihapus = \n{data}")

z = []
x = [1,2,3]
y = [4,5,6]
z.append(x)
z.append(y)
print (z)

