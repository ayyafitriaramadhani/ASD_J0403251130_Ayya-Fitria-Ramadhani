#--------------------------------------------------
# Nama : Ayya Fitria Ramadhani
# NIM  : J0403251130
# Kelas: TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# Pertemuan 9
# Latihan 2: membuat binary search tree sederhana
#--------------------------------------------------

# Class Node digunakan untuk membuat struktur tree
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai pada node
        self.left = None      # child kiri (awal kosong)
        self.right = None     # child kanan (awal kosong)

# membuat root (akar tree)
root = Node("A")

# level 1 (child dari root)
root.left = Node("B")   # child kiri A
root.right = Node("C")  # child kanan A

# level 2 (child dari B)
root.left.left = Node("D")   # child kiri B
root.left.right = Node("E")  # child kanan B

# level 3 (child dari C)
root.right.left = Node("F")   # child kiri C
root.right.right = Node("G")  # child kanan C

# menampilkan isi tree
print("Data pada root", root.data)
print("Child kiri root", root.left.data)
print("Child kanan root", root.right.data)
print("Child kiri dari B:", root.left.left.data)
print("Child kanan dari B:", root.left.right.data)
print("Child kiri dari C:", root.right.left.data)
print("Child kanan dari C:", root.right.right.data)

#penjelasan
'''Program ini membuat struktur tree sederhana menggunakan class Node. Dimulai dari root "A", kemudian ditambahkan child kiri dan kanan hingga membentuk beberapa level (B, C, D, E, F, G). Setelah itu, program menampilkan data pada setiap node untuk menunjukkan hubungan antar node dalam tree.'''