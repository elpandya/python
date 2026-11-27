a = [107,109,18,79,64,246]
for i in range (len(a)-1):
    tukar = False
    for j in range (len(a) - i-1):
        if a[j] > a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
            tukar = True
    if not tukar:
        break
    n += 1
print ('iterasi:', n)
for i in range (len(a)):
    print (a[i])  