# ========================================================== 
# TUGAS LATIHAN PRAKTIKUM PERTEMUAN 3 
# latihan 4-Buat metode untuk memggabungkan dua single linked list menjadi satu linked list baru.
# 
# Nama  : Ayya Fitria Ramadhani
# NIM   : J0403251130
# Kelas : B1
# ==========================================================
# 
# # =========================
# Class Node
# =========================
# Digunakan untuk membuat node pada linked list 
class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan nilai/data node
        self.next = None     # Pointer ke node berikutnya

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  

    def insert_at_end(self, data):
        new_node = Node(data)   #Membuat node baru
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
 
    def display(self):
        current = self.head
        if not current:
            print("kosong")
            return
        
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> null")

# Fungsi Menggabungkan
def gabung_linked_list(list1, list2):
    list_baru = LinkedList()

    # Salin List 1
    current = list1.head
    while current:
        list_baru.insert_at_end(current.data)
        current = current.next

    # Salin List 2
    current = list2.head
    while current:
        list_baru.insert_at_end(current.data)
        current = current.next

    return list_baru

#Fungsi Bantuan untuk Input
def buat_list_dari_input(urutan):
    ll = LinkedList()
    print(f"\n--- Input Linked List {urutan} ---")
    print("Masukkan angka-angka dipisahkan spasi atau koma (misal: 1 3 5).")
    print("Jika ingin kosong, langsung tekan Enter.")
    
    data_input = input(f"Masukkan elemen Linked List {urutan}: ")
    
    #Jika user langsung tekan Enter (kosong)
    if not data_input.strip():
        return ll

    # Membersihkan input (ganti koma jadi spasi, lalu split)
    angka_list = data_input.replace(',', ' ').split()
    
    for item in angka_list:
        try:
            angka = int(item)
            ll.insert_at_end(angka)
        except ValueError:
            print(f"Peringatan: '{item}' bukan angka dan dilewati.")
            
    return ll

# ==========================================
# Menjalankan program
# ==========================================

# Input untuk List Pertama
list1 = buat_list_dari_input("1")

#Input untuk List Kedua
list2 = buat_list_dari_input("2")

#Tampilkan Kondisi Awal
print("\n----------------Hasil----------------")
print("Linked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

#Proses Penggabungan
list_gabungan = gabung_linked_list(list1, list2)

#Tampilkan Hasil Akhir
print("Linked List setelah digabungkan:", end=" ")
list_gabungan.display()