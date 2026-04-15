#--------------------------------------------------
# Nama : Ayya Fitria Ramadhani
# NIM  : J0403251130
# Kelas: TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# Pertemuan 9 
# Latihan 4: Struktur Organisasi Perusahaan
#--------------------------------------------------

# Class Node digunakan sebagai dasar pembuatan tree
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nama jabatan
        self.left = None      # bawahan kiri
        self.right = None     # bawahan kanan

# Fungsi preorder (Root -> Left -> Right)
def preorder(node):
    if node is not None:
        print(node.data, end=" ")  # tampilkan data
        preorder(node.left)        # ke kiri
        preorder(node.right)       # ke kanan

# membuat root (pimpinan tertinggi)
root = Node("Direktur")

# level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# level 2
root.left.left = Node("Staff1")
root.right.right = Node("Staff2")

# data ini menimpa (overwrite) Staff2 menjadi Staff3
root.right.right = Node("Staff3")

# menjalankan traversal preorder
print("Struktur Organisasi (preorder): ")
preorder(root)

#penjelasan
'''Program ini membuat struktur organisasi perusahaan dalam bentuk tree. Setiap node merepresentasikan jabatan, mulai dari Direktur sebagai root hingga Manajer dan Staff sebagai child. Struktur ditampilkan menggunakan traversal preorder (root → kiri → kanan). Namun, terdapat penimpaan data pada Staff2 menjadi Staff3, sehingga Staff2 tidak ditampilkan.
Struktur Organisasi (preorder):
Direktur Manajer A Staff1 Manajer B Staff3'''