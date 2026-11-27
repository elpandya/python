antrian = []
n = int (input ("Jumlah Pelanggan: "))

for i in range (n):
    x = input ("Enter nama: ")
    antrian.append(x)

print (antrian)
for i in range (n):
    keluar = antrian.pop()
    print (f"{keluar}, keluar")

print (antrian)