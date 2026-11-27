import os 
os.system("cls")
data = [9,3,5,1,4,3,6,7,0,2,3,3,4,1,4,5,6]
print (data)
# banyaknya angka 4 dalam list
nomor_4 = data.count(4)
print (nomor_4)

maksimal = max(data)
print (maksimal)

minimal = min(data)
print (minimal)

data2 = ["water","wind","fire","rocks"]
pos = data2.index("fire")
print (f"\n {data2} \nthe datum 'fire' at index : {pos}")

print (f"\nthe data of numbers before sorting :\n{data}\n{data2}") 
data.sort()
data2.sort()
print (f"\nthe data of numbers after sorting : \n{data}\n{data2}") 

data.reverse()
data2.reverse()
print (f"\nthe data after reverse = \n {data}\n {data2}")