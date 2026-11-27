import os
os.system("cls")
data = "menggunakan double quote"
print (data)
data = 'menggunakan single quote'
print (data)

#masalah = 'jum'at'
solusi = 'jum\'at'
print (solusi)
solusi = "jum'at"
print (solusi)

# masalah = 'C:\User\Python'
solusi = 'C:\\user\\python'
print (solusi)
solusi = "C:\\user\\python"
print (solusi)
solusi = r"C:\user\python"
print (solusi)

print ("===============")
course = "hello world"
print (len(course))
print (course[0])
print (course[-1])
print (course[0:3])
print (course[0:])
print (course[:3])
print (course[:])
print (course[5])
print (course[0:11:2])
print ("max =", max(course))
print ("min =", min(course))
#mengambil 1 huruf setiap 2 huruf


print ("===============")
first = "Elgin"
second = "Pandya"
last = "Adinata"
angka = 888.99
print (angka, type(angka))
format_string = f"{angka}"
print (format_string, type(format_string))
full = first + " " + second + " " + last
print (full)
full = f"{first} {second} {last}"
print (full)
full = f"{len(first)} {second} {8*8} hhh"
print (full)

print ("===============")
course = " python programming"
print (course.index('p',2))
#jika tidak ada huruf tersebut maka progaram akan eror
print (course.find('q'))
#jika tidak ada huruf yang dicari maka akan keluar -1
#lebih flexible, cocok untuk looping
print (course.upper())
#uppercase
print (course.lower())
#lowercase
print (course.title())
#kapital setiap pada huruf pertama sebuah kata
print (course.rstrip())
print (course.replace('p','g'))
print ("pro" in course)
print ("pro" not in course)

#mengulang string
print ('yo'*5)
print (5*'yo')

vocab =  "good day.doc"
print ("apakah vocab lower : ", vocab.islower())
print ("apakah vocab lower : ", vocab.isupper())
print ("apakah all vocab huruf: ", vocab.isalpha())
print ("apakah all vocab angka: ", vocab.isdecimal())
print ("apakah vocab ada angka dan huruf: ", vocab.isalnum())
print (vocab.isspace())
print ("apakah awal kata is 'good' : ", vocab.startswith("good"))
print ("apakah awal kata is 'day' : ", vocab.startswith("day"))
print ("apakah akhir kata is '.doc' : ", vocab.endswith(".day"))

print ("=============")
print ("")
kalimat = "saya belajar python"
hasil = kalimat.split()
print (hasil)

data = "apel,jeruk,mangga,nanas,melon"
print (data.split(','))
print (data.split('mangga'))

kata = ['saya','sedang','belajar','python']
hasil2 = " ".join(kata)
print (hasil2)

print('')
print ("=================")
tengah = "tengah".center(20)#jumlah index
print (tengah)
kiri = "kiri".ljust(20)#jumlah index
print (kiri)
kanan = "kanan".rjust(20)#jumlah index
print (kanan)