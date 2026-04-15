#==============================================================
#Nama : Ayya Fitria Ramadhani
#NIM : J0403251130
#Kelas : TPL-B1
#==============================================================
#Implementasi Dasar :Queue Berbasis linked list
#==============================================================

#membuat class node ()
class node :
    def __init__(self, data ): #konstruktor (bisa di tambahkan parameter yang di butuhkan(contohnya: self (, pake koma) data))
        self.data = data #untuk menyimpan nilai/data
        self.next = None #untuk pointer ke note berikutnya

#Queue dengan 2 pointer : front dan rear /head and tail
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        #Mengembalikan True jika Front adalaj None(Queue kosong)
        return self.front is None

    def enqueue (self,data):
        #menambah data di belakang (rear)
        nodebaru = node(data)

        #Jika queue kosong, front and rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodebaru
            self.rear = nodebaru
            return
        
        #Jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodebaru

        #Rear pindah ke node baru
        self.rear = nodebaru

    def dequeue (self):
        #Menghapus data dari depan
         
        #1)lihat data yang paling depan
        data_terhapus = self.front.data

        #2)Geser front ke node berikutnya 
        self.front = self.front.next

        #3)Jika setelah di geser front menjadi None, maka Queue kosong
        #rear juga harus non
        if self .front is None :
            self.rear= None

        return data_terhapus
    

    def tampilkan (self):

        current = self.front
        print("Front ->", end="->")
        while current is not None :
            print(current.data, end="->")
            current= current.next
        print("Node - Rear di node terakhir")

#Instantiasi objek class QueueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan ()

q.dequeue()
q.tampilkan()