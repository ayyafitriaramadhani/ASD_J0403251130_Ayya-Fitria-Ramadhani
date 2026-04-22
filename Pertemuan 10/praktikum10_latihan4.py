#==================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Prodi/Kelas : TPL_B_P1
#==================================

#==================================
#Pertemuan 10
#latihan 4 : Membuat BST yang tidak seimbang  
#===================================

#class node untuk menyimpan data BST
class Node:
    def __init__(self,data):
        self.data = data #nilai pada node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi insert untuk BST
def insert(root,data):
    #jika root kosong,membuat node baru
    if root is None:
        return Node(data)
    
    #jika data lebih kecil,masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left,data)

    #jika data lebih besar, masuk ke subtree kanan
    if data > root.data:
        root.right = insert(root.right,data)

    return root

#fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

#fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" "* level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level+1, "L")
        tampil_struktur(root.right, level+1, "R")

#==================================
#Program utama
#===================================
root = None

#data dimasukkan berurutan naik
data_list = [10,20,30]

#memasukkan data ke BST satu per satu
for data in data_list:
    root = insert(root, data)

#menampilkan isi tree dengan preorder
print("preorder BTS: ")
preorder(root)

#menampilkan struktur tree
print("\n\nStruktur BTS: ")
tampil_struktur(root)

#penjelasan
'''Program dimulai dengan membuat tree kosong, lalu data `[10, 20, 30]` 
dimasukkan satu per satu ke BST sehingga tree menjadi miring ke kanan. 
Setelah itu, `preorder` digunakan untuk menampilkan urutan node, 
dan `tampil_struktur` untuk melihat bentuk tree secara jelas.'''