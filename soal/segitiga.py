import os 
os.system("cls")
t = 5
n = 1
s = t - 1
while s >= 0 :
    print (" " * s + "*" * n)
    s -= 1
    n += 2
t = 5
n = 1
s = t - 1
while s >= 0 :
    print (" " * s,"*" * n)
    s -= 1
    n += 2
#tanda koma dan tambah sangat berbeda
# tanda koma otomatis ada spasi
# tanda tambah tidak ada

t = 5
n = 1
s = t - 1
while s>=0 :
    print (" " * s + "*" * n)
    s -= 1
    n += 2
while s != t-1 :
    if s == -1 :
        s += 1
        n -= 2
    s += 1
    n -= 2
    print (" " * s + "*" * n)



       
n = int (input("tinggi segitiga : "))
i = 1
while i <= n:
    print ("*" * i)
    i += 1
