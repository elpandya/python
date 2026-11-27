
stack = []

def is_empty():
    """Memeriksa apakah stack kosong."""
    return len(stack) == 0


def push(buku):
    """Memasukkan buku ke bagian atas stack."""
    stack.append(buku)
    print(buku, "berhasil dimasukkan")


def peek():
    """Melihat buku teratas tanpa menghapusnya."""
    if is_empty():
        return "Tidak ada buku di dalam stack"

    return stack[-1]


def pop():
    """Mengambil dan menghapus buku teratas."""
    if is_empty():
        return "Tidak ada buku yang dapat diambil"

    return stack.pop()

# Menggunakan fungsi push
push("Buku Merah")
push("Buku Hijau")
push("Buku Biru")

print("\nIsi stack:", stack)

# Menggunakan fungsi peek
print("Buku paling atas:", peek())
print("Isi setelah peek:", stack)

# Menggunakan fungsi pop
print("\nBuku keluar:", pop())
print("Isi setelah pop:", stack)

# Menggunakan fungsi is_empty
print("\nApakah stack kosong?", is_empty())

# Mengambil semua buku yang tersisa
print("Buku keluar:", pop())
print("Buku keluar:", pop())

print("Apakah stack kosong?", is_empty())

# Mencoba pop saat kosong
print(pop())
