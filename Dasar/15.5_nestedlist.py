import os
os.system("cls")
data0 = [1,3]
data1 = [3,5,2]

normal = [1,4,6,9]
print (f"normal list = {normal}")

nested = [data0,data1,9,7,8]

print (f"nested list = {nested}")

# contoh penggunaan

peserta0 = ["aaa",25,"laki-laki"]
peserta1 = ["bbb",15,"perempuan"]
peserta2 = ["ccc",10,"laki-laki"]
listpest = [peserta0,peserta1,peserta2]
for i in listpest :
    print (f"nama   : {i[0]}")
    print (f"umur   : {i[1]}")
    print (f"gender : {i[2]}\n")

