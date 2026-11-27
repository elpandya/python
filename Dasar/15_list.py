import os
os.system("cls")

# kumpulan data numbers
data1 = [6,9,0,1,2]
print (data1)

# kumpulan data string
data2 = ["paisang", "apel", "alpukat", "per"]
print (data2)

# kumpulan data boolean
data3 = [True,False,True]
print (data3)

# kumpulan data campuran
data4 = [1945,True,False, "agustus"]
print (data4)

# cara alternatif membuat list
data5 = range (5,10)
print (data5)
data6 = list (data5)
print (data6)

print ("")
data7 = range (0,10,2)
print (data7)
data8 = list (data7)
print (data8)
# range (start, before finish, increment)

print("")
# membuat list menggunakan for
data9 = [i for i in range (0,10)]
print (data9)

data9_2 = [5 for i in range (0,10)]
print (data9_2)

data9_3 = []
for i in range(0,10):
    data9_3.append(i)
print (data9_3)


#kuadrat
data9 = [i ** 2 for i in range (0,10)]
print (data9)

print ("")
# list menggunakan for dan if
data10 = [ i for i in range (0,5) if i != 3]
print (data10)
data11 = [ i for i in range (0,10) if i % 2 == 0]
print (data11)
data12 = [ i for i in range (0,10) if i % 2 != 0]
print (data12)