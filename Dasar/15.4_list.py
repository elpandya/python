import os
os.system("cls")
a = ["grape","pir","apple"] 
print (f"a = {a}")

b = a
print (f"b = {b}")

# merubah nilai a
a[1] = "banana"

# maka b otomatif berubah 
# karena alamat a dan b sama 

b.sort()
print (f"a = {a}")
print (f"b = {b}")

# hanya menduplikat data tidak termasuk alamat
c = a.copy() 
print (f"a = {hex(id(a))}")
print (f"a = {hex(id(b))}")
print (f"c = {hex(id(c))} berbeda dengan a dan b")

c[2] = "water melon"
print (f"a = {a}")
print (f"b = {b}")
print (f"c = {c}")

