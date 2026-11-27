import os 
os.system("cls")
data = []
for i in range (5) :
    x = int(input())
    data.append(x)

print (f"list asli : {data}")

genap = []
for i in data :
    if i % 2 == 0 :
        genap.append(i)
print(f"angka genap : {genap}")

jumlah = 0
for i in data :
    jumlah += i
print (f"jumlah : {jumlah}")

maksimum = data[0]
for i in data :
    if i > maksimum :
        maksimum = i
print (f"angka terbesar : {maksimum}")