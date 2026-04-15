#--------------------------------------------------
# Nama : Ayya Fitria Ramadhani
# NIM  : J0403251130
# Kelas: TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# Pertemuan 9 
# Latihan 3: Membuat Traversal Preorder
#--------------------------------------------------

# Class Node digunakan sebagai dasar pembuatan tree
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai node
        self.left = None      # child kiri
        self.right = None     # child kanan

# Fungsi traversal preorder (Root -> Left -> Right)
def preorder(node):
    if node is not None:
        print(node.data, end=" ")  # tampilkan data node
        preorder(node.left)        # telusuri child kiri
        preorder(node.right)       # telusuri child kanan

# membuat root
root = Node("A")

# level 1
root.left = Node("B")
root.right = Node("C")

# level 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal preorder
print("Hasil Traversal preorder: ")
preorder(root)

#penjelasan
'''Program ini membuat struktur tree sederhana dan melakukan traversal preorder. Traversal preorder mengunjungi node dengan urutan root → kiri → kanan. Hasilnya, node akan ditampilkan sesuai urutan penelusuran dari akar hingga ke child.'''