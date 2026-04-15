#==============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#Implementasi Dasar : Node Pada Linked List
#==============================================================

#membuat class node ()
class node :
    def __init__(self, data ): #konstruktor (bisa di tambahkan parameter yang di butuhkan(contohnya: self (, pake koma) data))
        self.data = data #untuk menyimpan nilai/data
        self.next = None #untuk pointer ke note berikutnya

#Membuat konstruktor satu persatu
nodeA = node ("A")#proses memanggil konstruktor dengan memanggil  nama class
nodeB = node ("B")
nodeC = node ("C")

# menghubungkan node : A -> B -> C -> None
nodeA.next = nodeB # node a next adalah node B / variable nodeB ada pada nodeA
nodeB.next = nodeC

# Menentukan node pertama(head)
head = nodeA

#Traversal : menelusuri dari head sampai none
current = head
while current is not None :
    print(current.data)     #Menampilkan data pada node saat ini
    current = current.next  # pindah ke node berikutnya

#==============================================================
#Implementasi Dasar : linked list + insert awal
#==============================================================

class linkedlist: #oprasional (class implementasi stack)
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self,data): #push dalam stack
        # buat node baru
        nodebaru = node (data) #panggil class node

        # node baru menunjuk ke head lama
        nodebaru.next = self.head

        #head pindah ke node baru
        self.head = nodebaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #cara agar terhapus dengan menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah :", data_terhapus)

    def tampilkan(self): # implementasi travelsal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("======LIST BARU=====")
ll = linkedlist()  # instantiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()