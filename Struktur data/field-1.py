parkiran = []

def is_empty():
    return len(parkiran) == 0


def push(buku):
    parkiran.append(buku)
    print(buku, "mobil berhasil masuk parkiran")


def peek():
    if is_empty():
        return "Tidak ada mobil di dalam parkiran"

    return parkiran[-1]


def pop():
    if is_empty():
        return "Tidak ada mobil yang dapat dikeluarkan (parkiran kosong)"

    return parkiran.pop()

parkiran.append("Mobil Merah")
parkiran.append("Mobil Hitam")
parkiran.append("Mobil Coklat")
parkiran.append("Mobil Ungu")
parkiran.append("Mobil Orange")

print ("Mobil yang paling dekat dengan pintu keluar -> ",peek() )
mobil_keluar = pop()
print ("Mobil yang Keluar -> ", mobil_keluar )

print ("Mobil sekarang yang paling dekat dengan pintu keluar -> ",peek() )

print ("Parkiran Sekarang", parkiran)