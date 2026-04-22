#==================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Prodi/Kelas : TPL_B_P1
#==================================

#==================================
#Pertemuan 10
#latihan 6 : Rotasi kanan pada BST Tidak Seimbang 
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
def rotate_right(y): 
    # x adalah root lama 
    x = y.left       # x adalah child kiri y 
    T2 = x.right      # subtree kanan milik x disimpan sementara 
 
    # Proses rotasi 
    x.right = y        # x menjadi child kiri dari y 
    y.left = T2      # child kiri y diganti dengan T2 
 
    # x menjadi root baru 
    return x 

# =============================
# Program utama 
# ============================= 
# Membuat tree yang tidak seimbang: 
# 30 -> 20 -> 10 
root = Node(30) 
root.left = Node(20) 
root.left.left = Node(10) 
print("Preorder sebelum rotasi kanan:") 
preorder(root) 
print("\n\nStruktur sebelum rotasi kanan:") 
tampil_struktur(root) 
# Melakukan rotasi kanan pada root 
root = rotate_right(root) 
print("\nPreorder sesudah rotasi kanan:") 
preorder(root) 
print("\n\nStruktur sesudah rotasi kanan:") 
tampil_struktur(root)

#penjelasan
''' Program ini membuat BST yang awalnya tidak seimbang (miring ke kiri) 
dari data 30, 20, 10. Lalu dilakukan rotasi kanan supaya tree jadi lebih seimbang, 
di mana 20 jadi root, 10 di kiri, dan 30 di kanan. Program juga menampilkan isi 
dan struktur tree sebelum dan sesudah rotasi biar kelihatan perubahannya.'''