#==================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Prodi/Kelas : TPL_B_P1
#==================================

#==================================
#Pertemuan 10
#latihan 5 : Rotasi Kiri pada BST Tidak Seimbang 
#===================================
# Class Node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 
 
 
# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 
 
 
# Fungsi rotasi kiri 
def rotate_left(x): 
    # x adalah root lama 
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara 
 
    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2 
 
    # y menjadi root baru 
    return y 

# =============================
# Program utama 
# ============================= 
# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
root = Node(10) 
root.right = Node(20) 
root.right.right = Node(30) 
print("Preorder sebelum rotasi kiri:") 
preorder(root) 
print("\n\nStruktur sebelum rotasi kiri:") 
tampil_struktur(root) 
# Melakukan rotasi kiri pada root 
root = rotate_left(root) 
print("\nPreorder sesudah rotasi kiri:") 
preorder(root) 
print("\n\nStruktur sesudah rotasi kiri:") 
tampil_struktur(root)

#penjelasan
'''Program ini membuat BST yang awalnya tidak seimbang (miring ke kanan) 
dari data 10, 20, 30. Lalu dilakukan rotasi kiri supaya tree jadi lebih seimbang, 
di mana 20 jadi root, 10 di kiri, dan 30 di kanan. Program juga menampilkan isi 
dan struktur tree sebelum dan sesudah rotasi.'''