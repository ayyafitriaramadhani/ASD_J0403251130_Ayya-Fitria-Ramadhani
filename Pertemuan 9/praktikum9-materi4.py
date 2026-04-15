#--------------------------------------------------
# Nama : Ayya Fitria Ramadhani
# NIM  : J0403251130
# Kelas: TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# Pertemuan 9 
# Latihan 4: Membuat Traversal Inorder
#--------------------------------------------------

# Class Node digunakan sebagai dasar pembuatan tree
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai node
        self.left = None      # child kiri
        self.right = None     # child kanan

# Fungsi traversal inorder (Left -> Root -> Right)
def inorder(node):
    if node is not None:
        inorder(node.left)        # telusuri child kiri
        print(node.data, end=" ") # tampilkan data node
        inorder(node.right)       # telusuri child kanan

# membuat root
root = Node("A")

# level 1
root.left = Node("B")
root.right = Node("C")

# level 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal inorder
print("Hasil Traversal inorder: ")
inorder(root)

#penjelasan
'''Program ini membuat struktur tree sederhana dan melakukan traversal inorder. Traversal inorder mengunjungi node dengan urutan kiri → root → kanan, sehingga node ditampilkan mulai dari child kiri, kemudian root, lalu child kanan.
Hasil Traversal inorder:
D B A C E'''