#==================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Prodi/Kelas : TPL_B_P1
#==================================

#==================================
#Pertemuan 10
#gabungan latihan 1-3
#latihan 1 : BST
#===================================

# Class Node untuk membuat 1 node pada BST
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai
        self.left = None #child kiri
        self.right = None #child kanan

# Fungsi insert untuk memasukkan data ke BST
def insert(root,data):
    # jika tree masih kosong, buat node baru
    if root is None:
        return Node(data)
    
    # jika data lebih kecil dari root, masuk ke kiri
    if data < root.data:
        root.left = insert(root.left,data)
    # jika data lebih besar dari root, masuk ke kanan
    elif data > root.data:
        root.right = insert(root.right,data)

    # kembalikan root (agar tree tetap tersambung)
    return root

#program utama (mengisi data BST)
root = None  # awalnya tree kosong
data_list =[50,30.70,20,40,50,80]

#memasukkan data satu per satu ke BTS
for data in data_list:
    root = insert(root,data)

print("BST berhasil dibuat")

#==================================
#latihan 2: traversal inorder
#===================================

def inorder(root):
    if root is not None:
        inorder(root.left)          #kunjungi subtree kiri
        print(root.data, end=" ")   #tampilkan data
        inorder(root.right)         #kunjungi subtree kanan

print("hasil inorder: ")
inorder(root)

# Penjelasan:
# inorder = kiri → root → kanan
# hasilnya akan urut dari kecil ke besar

#==================================
#latihan 3: Search di BST
#penjelasan: mencari atau membandingkan angka
#===================================

def search(root, key):
    #jika tree kosong/data tidak ditemukan
    if root is None:
        return False
    
    #jika data ditemukan
    if root.data == key:
        return True
    #jika key lebih kecil, cari ke kiri
    elif key < root.data :
        return search(root.left,key)
    #jika key lebih besar,cari ke kanan
    else:
        return search (root.right,key)
    
#uji pencarian
key = 100 #data yang ingin di cari

if search(root,key):
    print("data ditemukan")
else:
    print("data tidak ditemukan")

#penjelasan
'''Alur program dimulai dari membuat tree kosong (root = None),
kemudian data dimasukkan satu per satu menggunakan fungsi insert 
sesuai aturan BST (lebih kecil ke kiri, lebih besar ke kanan).
Setelah semua data masuk, tree sudah terbentuk. 
Selanjutnya program menampilkan isi tree menggunakan traversal inorder,
yaitu mengunjungi kiri, root, lalu kanan sehingga data tampil urut.
Terakhir, program melakukan pencarian data dengan fungsi search, 
yaitu membandingkan nilai yang dicari dengan node saat ini, 
lalu bergerak ke kiri atau kanan sampai data ditemukan atau tidak ditemukan.'''