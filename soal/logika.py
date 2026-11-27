nilai = float (input ( 'masukan nilai < 3 atau > 10 : '))
kurangdari = nilai < 3
print (kurangdari)

lebihdari = nilai > 10
print (lebihdari)

cek = kurangdari or lebihdari
print ('angka yang anda masukan :',cek)


# irirsan menggunakan and
# mengambil nilai >3 and <10
nilai = float (input ( 'masukan nilai < 3 and > 10 : '))
lebihdari = nilai > 3
print (lebihdari)

kurangdari = nilai < 10
print (kurangdari)

cek = lebihdari and kurangdari
print ('angka yang anda masukan :',cek)


nilai = float (input ( 'masukan nilai >0 and <5 or >8 and <11 : '))
lebihdari = nilai > 0 and nilai < 5
print (lebihdari)

kurangdari = nilai > 8 and nilai < 11
print (kurangdari)

cek = lebihdari or kurangdari
print ('angka yang anda masukan :',cek)

