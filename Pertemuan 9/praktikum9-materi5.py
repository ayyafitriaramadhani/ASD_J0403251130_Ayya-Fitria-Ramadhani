#--------------------------------------------------
# Nama : Ayya Fitria Ramadhani
# NIM  : J0403251130
# Kelas: TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# Pertemuan 9 : Tree
# Latihan 4: Membuat Traversal Postorder
#--------------------------------------------------

# Class Node digunakan sebagai dasar pembuatan tree
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai node
        self.left = None      # child kiri
        self.right = None     # child kanan

# Fungsi traversal postorder (Left -> Right -> Root)
def postorder(node):
    if node is not None:
        postorder(node.left)   # telusuri child kiri
        postorder(node.right)  # telusuri child kanan
        print(node.data, end=" ")  # tampilkan data node

# membuat root
root = Node("A")

# level 1
root.left = Node("B")
root.right = Node("C")

# level 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal postorder
print("Hasil Traversal postorder: ")
postorder(root)

#penjelasan
'''Program ini membuat struktur tree sederhana dan melakukan traversal postorder. Traversal postorder mengunjungi node dengan urutan kiri → kanan → root, sehingga node ditampilkan mulai dari child paling kiri, kemudian kanan, dan terakhir root.
Hasil Traversal postorder:
D B E C A'''