#--------------------------------------------------
# Nama : Ayya Fitria Ramadhani
# NIM  : J0403251130
# Kelas: TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# Pertemuan 9
# Latihan 1: Membuat Node Tree
#--------------------------------------------------

# Class Node digunakan sebagai dasar untuk membuat struktur tree
class Node:
    def __init__(self, data):
        # atribut untuk menyimpan data pada node
        self.data = data
        
        # atribut untuk menyimpan child kiri (awal = None)
        self.left = None
        
        # atribut untuk menyimpan child kanan (awal = None)
        self.right = None

# Membuat node root (akar) dengan nilai "A"
root = Node("A")

# Menampilkan isi dari node root dan child-nya
print("Data pada root:", root.data)           # menampilkan data utama
print("Data child kiri root:", root.left)    # masih None (belum ada child)
print("Data child kanan root:", root.right)  # masih None (belum ada child)

#Penjelasan
'''Program ini membuat struktur dasar node pada tree menggunakan class Node. Setiap node memiliki data serta dua child yaitu kiri (left) dan kanan (right) yang awalnya bernilai None. Kemudian dibuat satu node sebagai root dengan nilai "A", lalu ditampilkan isi data root beserta child-nya yang masih kosong.'''