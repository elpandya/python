import os 
os.system("cls")
"""
angka = int (input ("masukan nilai : "))

print (5*"<>")
if angka < 0 :
    print ("Negatif")
elif angka == 0 : 
    print ("Nol")
else :
    print ("positif")


print (5*"<>")
nilai = int (input ("masukan nilai anda (0-100) : "))

if nilai >= 90 :
    print ("A")
elif nilai >= 80 :
    print ("B")
elif nilai >= 70 :
    print ("C")
elif nilai >= 60 :
    print ("D")
else :
    print ("E")

user = input("masukan username anda : ")
password = input("masukan pasword anda : " )

if user=="admin" and password == "12345" :
    print ("Login berhasil")
elif user!="admin" and password != "12345": 
    print ("Username dan passowrd salah")
elif user != "admin" :
    print ("Username salah")
else :
    print ("Password salah")


umur = int(input("masukan umur anda : "))

if umur < 13 :
    print ("Anak")
elif umur <=17 :
    print ("Remaja")
elif umur <=59 : 
    print ("Dewasa")
else : 
    print ("Lansia")


tahun = int(input("tahun : "))
if tahun % 400 == 0 :
    print ("Kabisat")
elif tahun % 4 == 0 and tahun % 100 != 0 :
    print ("Kabisat")
else :
    print ("Bukan kabisat")


x = int(input("masukan angka pertama : "))
o = (input("operator (+,-,*,/) : "))
y = int(input("masukan angka kedua : "))

if o == "+" :
    print ("x + y :",x+y)
elif o == "-" :
    print ("x - y :",x-y)
elif o == "*" :
    print ("x * y :",x*y)
elif o == "/" :
    if y == 0 :
        print ("Tidak bisa dibagi 0")
    else :
        print ("x / y :",x/y)


nilai = int(input("masukan nilai : "))

if nilai % 3 == 0 and nilai % 5 == 0 :
    print ("FizzBuzz")
elif nilai % 3 == 0 :
    print ("Fizz")
elif nilai % 5 == 0 :
    print ("Buzz")
else : 
    print (nilai)


umur = int(input("Masukan umur : "))
hari = input("Hari kunjungan : ").lower()


if umur < 0 or umur > 100 :
    print ("Umur tidak valid")
elif umur <12 and hari == "minggu" :
    print ("Anda gratis masuk!")
else :
    if umur < 12 :
        harga = 20000
    elif umur <=17 :
        harga = 35000
    elif umur < 59 :
        harga = 50000
    else :
        harga = 30000
    if hari == "senin" :
        harga *= 0.9
    print ("Harga tiket anda: Rp", int(harga))
"""


umur = int(input("Umur : "))
tinggi = int(input("tinggi badan (cm) : "))
hari = input("hari kunjungan : ").lower()
kartu = input("punya kartu pelajar? (ya/tidak) : ").lower()

if umur < 0 or umur > 120 :
    print ("Input tidak valid")
elif tinggi < 50 or tinggi >250 :
    print ("Input tidak valid")
elif hari not in ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]:
    print("Input tidak valid")

else :
    if umur < 5 :
        tipe = "Balita"
        harga = 0
    elif umur <= 12 :
        tipe = "Anak"
        harga = 25000
    elif umur <= 17 :
        tipe = "Remaja"
        harga = 40000
    elif umur <= 59 :
        tipe = "Dewasa"
        harga = 25000
    else :
        tipe = "Lansia"
        harga = 25000
    harga_awal = harga
    diskon = "0%"
    if tinggi < 100:
        harga *= 0.5
        diskon = "50%"
    if hari == "rabu" and tinggi >=100  :
        harga *=0.9
        diskon = "10%"  
    if hari in ["sabtu","minggu"] :
        if umur <= 59 :   
            harga *=1.2
    if umur <= 17 and tinggi >=100:
        harga *= 0.85
        diskon = "15%"
                   
    print ("kategori :",tipe)
    print ("harga awal :",harga_awal)
    print ("total diskon :",diskon)
    print ("harga akhir :",int(harga))
