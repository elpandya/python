import os
import datetime as dt
os.system("cls")

tanggal = dt.date(2007,7,14)
print (tanggal)


print (8*"<>")
print ("please enter your birthday")
date = int(input("date = "))
month = int(input("month = "))
years = int(input("years = "))
data = dt.date(years,month,date)
print (data)
print (f"hari lahirnya adalah : {data:%A}")
hari_ini = dt.date.today()
print ("today is ", hari_ini)

umur_hari = hari_ini - data
umur_tahun = umur_hari.days // 365
print (f"""umur : {umur_hari} atau
umur : {umur_tahun} tahun""")