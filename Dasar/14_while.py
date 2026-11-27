import os
os.system ("cls")

nilai = 5
iter = 1

while nilai > 1 :
    print (f"Nilai pada iterasi {iter} = {nilai}")
    nilai -= 1
    iter += 1


angka = 1
while angka < 5 :
    print (angka)
    if angka == 5:
        pass # ini tidak akan dilakukakan
    angka+= 1

print ("")
bilangan = 1
while bilangan <= 10 :
    if bilangan % 2 == 0 :
        print (f"{bilangan} adalah bilangan genap")
    else :
        print (f"{bilangan} adalah bilangan ganjil")
    bilangan += 1

# CONTINUE
print ("")
n = 1
while n < 5 :
    n += 1
    if n == 3 :
        continue
    print ("halo")

# BREAK
print ("")
x = 1 
while x < 5 :
    print (f"angka sekarang = {x}")
    x += 1
    if x == 3 :
        break
print ("selesai")

y = 0
while y <= 9 :
    y += 1
    print (y)
  
