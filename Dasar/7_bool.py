a = True
b = not a
print (a)
print (b)

# OR
a = True
b = False
c = a or b
print (a, ' or' ,b, '=', c)
a = False
b = False
c = a or b
print (a, 'or' ,b, '=', c)
a = False
b = True
c = a or b
print (a, 'or' ,b, ' =', c)
a = True
b = True
c = a or b
print (a, ' or' ,b, ' =', c)
# kesimpulannya
# jika salah satu variabel atau keduanya
# bernilai true, maka akan bernilai true
print ('')
print ('=====================')
print ('  =================')
print ('    =============')
print ('      =========')
print ('        =====')
print ('          =')
# AND
a = True
b = False
c = a and b
print (a, ' and' ,b, '=', c)
a = False
b = False
c = a and b
print (a, 'and' ,b, '=', c)
a = False
b = True
c = a and b
print (a, 'and' ,b, ' =', c)
a = True
b = True
c = a and b
print (a, ' and' ,b, ' =', c)
# selalu bernilai False
# kecuali keduanya bernilai true


# XOR
a = True
b = False
c = a ^ b
print (a, ' XOR' ,b, '=', c)
a = False
b = False
c = a ^ b
print (a, 'XOR' ,b, '=', c)
a = False
b = True
c = a ^ b
print (a, 'XOR' ,b, ' =', c)
a = True
b = True
c = a ^ b
print (a, ' XOR' ,b, ' =', c)
# kesimpulannya
# XOR akan bernilai true jika
# salah satunya bernilai true 